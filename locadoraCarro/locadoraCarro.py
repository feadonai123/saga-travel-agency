import os
import random
import grpc
from concurrent import futures
import locadoraCarro_pb2
import locadoraCarro_pb2_grpc
from dotenv import load_dotenv
from databaseManager import DatabaseManager

load_dotenv()

db = DatabaseManager()

PORCENTAGEM_ERRO = 0

class LocadoraCarroServicer(locadoraCarro_pb2_grpc.LocadoraCarroServicer):
    def BookCar(self, request, context):
        car_model = request.car_model
        start_date = request.start_date
        end_date = request.end_date
        
        record_id = -1
        has_error = (random.randint(0, 100) <= PORCENTAGEM_ERRO)
        if(has_error):
            sucess = False
            message = "Carro não disponível"
        else:
            record_id = db.insert("carro", {
                "car_model": car_model,
                "start_date": start_date,
                "end_date": end_date,
            })
            sucess = True
            message = "Carro agendado com sucesso"
        print(message)
        return locadoraCarro_pb2.BookCarResponse(sucess=sucess, message=message, id=record_id)
    
    def CancelBookCar(self, request, context):
        id = request.id
        
        db.delete("carro", id)
        
        sucess = True
        message = "Carro cancelado com sucesso"
        print(message)
        return locadoraCarro_pb2.CancelBookCarResponse(sucess=sucess, message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    locadoraCarro_pb2_grpc.add_LocadoraCarroServicer_to_server(LocadoraCarroServicer(), server)
    server.add_insecure_port("[::]:" + os.getenv("PORT"))
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
