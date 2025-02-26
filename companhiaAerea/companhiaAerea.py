import os
import random
import grpc
from concurrent import futures
import companhiaAerea_pb2
import companhiaAerea_pb2_grpc
from dotenv import load_dotenv
from databaseManager import DatabaseManager

load_dotenv()

db = DatabaseManager()

PORCENTAGEM_ERRO = 0

class CompanhiaAereaServicer(companhiaAerea_pb2_grpc.CompanhiaAereaServicer):
    def BookFly(self, request, context):
        date = request.date
        origin = request.origin
        destination = request.destination
        qtd_passengers = request.qtd_passengers
        
        record_id = -1
        has_error = (random.randint(0, 100) <= PORCENTAGEM_ERRO)
        if(has_error):
            sucess = False
            message = "Voo indisponível"
        else:
            record_id = db.insert("viagem", {
                "date": date,
                "origin": origin,
                "destination": destination,
                "qtd_passengers": qtd_passengers  
            })
            sucess = True
            message = "Voo agendado com sucesso"
        print(message)
        return companhiaAerea_pb2.BookFlyResponse(sucess=sucess, message=message, id=record_id)
    
    def CancelBookFly(self, request, context):
        id = request.id
        
        db.delete("viagem", id)
        
        sucess = True
        message = "Voo cancelado com sucesso"
        print(message)
        return companhiaAerea_pb2.CancelBookFlyResponse(sucess=sucess, message=message)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    companhiaAerea_pb2_grpc.add_CompanhiaAereaServicer_to_server(CompanhiaAereaServicer(), server)
    server.add_insecure_port("[::]:" + os.getenv("PORT"))
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
