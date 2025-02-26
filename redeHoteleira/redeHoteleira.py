import os
import random
import grpc
from concurrent import futures
import redeHoteleira_pb2
import redeHoteleira_pb2_grpc
from dotenv import load_dotenv
from databaseManager import DatabaseManager

load_dotenv()

db = DatabaseManager()

PORCENTAGEM_ERRO = 0

class RedeHoteleiraServicer(redeHoteleira_pb2_grpc.RedeHoteleiraServicer):
    def BookHotel(self, request, context):
        hotel_name = request.hotel_name
        qtd_days = request.qtd_days
        qtd_guests = request.qtd_guests
        
        record_id = -1
        has_error = (random.randint(0, 100) <= PORCENTAGEM_ERRO)
        if(has_error):
            sucess = False
            message = "Hotel sem disponibilidade"
        else:
            record_id = db.insert("hotel", {
                "hotel_name": hotel_name,
                "qtd_days": qtd_days,
                "qtd_guests": qtd_guests,
            })
            sucess = True
            message = "Hotel agendado com sucesso"
        print(message)
        return redeHoteleira_pb2.BookHotelResponse(sucess=sucess, message=message, id=record_id)
    
    def CancelBookHotel(self, request, context):
        id = request.id
        
        db.delete("hotel", id)
        
        sucess = True
        message = "Hotel cancelado com sucesso"
        print(message)
        return redeHoteleira_pb2.CancelBookHotelResponse(sucess=sucess, message=message)
    
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    redeHoteleira_pb2_grpc.add_RedeHoteleiraServicer_to_server(RedeHoteleiraServicer(), server)
    server.add_insecure_port("[::]:" + os.getenv("PORT"))
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
