import os
import grpc
import companhiaAerea_pb2
import companhiaAerea_pb2_grpc
import locadoraCarro_pb2
import locadoraCarro_pb2_grpc
import redeHoteleira_pb2
import redeHoteleira_pb2_grpc
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from databaseManager import DatabaseManager

load_dotenv()

db = DatabaseManager()

def executeRollbackActions(rollbacks):
    reverse = rollbacks[::-1]
    for rollback in reverse:
        print(f"Rollbacking {rollback[0]}")
        rollback[1]()

def handleAgendarViagem(data):
    roolbackActions = []
    
    channel1 = grpc.insecure_channel(os.getenv("URL_COMPANHIA_AEREA"))
    stub1 = companhiaAerea_pb2_grpc.CompanhiaAereaStub(channel1)
    response1 = stub1.BookFly(companhiaAerea_pb2.BookFlyRequest(
        date=data["date_ida"],
        origin=data["origin"],
        destination=data["destination"],
        qtd_passengers=data["qtd_passengers"]
    ))
    
    print("response bookFly", response1)
    
    if(response1.sucess == False):
        executeRollbackActions(roolbackActions)
        return {"sucess": False, "message": response1.message}
    else:
        roolbackActions.append(("bookFly", lambda: stub1.CancelBookFly(companhiaAerea_pb2.CancelBookFlyRequest(id=response1.id))))
        
    channel2 = grpc.insecure_channel(os.getenv("URL_REDE_HOTELEIRA"))
    stub2 = redeHoteleira_pb2_grpc.RedeHoteleiraStub(channel2)
    response2 = stub2.BookHotel(redeHoteleira_pb2.BookHotelRequest(
        hotel_name = data["hotel_name"],
        qtd_days = data["hotel_qtd_days"],
        qtd_guests = data["qtd_passengers"]
    ))
    
    print("response bookHotel", response2)
    
    if(response2.sucess == False):
        executeRollbackActions(roolbackActions)
        return {"sucess": False, "message": response2.message}
    else:
        roolbackActions.append(("bookHotel", lambda: stub2.CancelBookHotel(redeHoteleira_pb2.CancelBookHotelRequest(id=response2.id))))
    
    
    channel3 = grpc.insecure_channel(os.getenv("URL_LOCADORA_CARRO"))
    stub3 = locadoraCarro_pb2_grpc.LocadoraCarroStub(channel3)
    response3 = stub3.BookCar(locadoraCarro_pb2.BookCarRequest(
        car_model = data["car_model"],
        start_date = data["car_start_date"],
        end_date = data["car_end_date"]
    ))
    
    print("response bookCar", response3)
    
    if(response3.sucess == False):
        executeRollbackActions(roolbackActions)
        return {"sucess": False, "message": response3.message}
    else:
        roolbackActions.append(("bookCar", lambda: stub3.CancelBookCar(locadoraCarro_pb2.CancelBookCarRequest(id=response3.id))))
    
    db.insert("viagem", {
        "id_voo": response1.id,
        "id_hotel": response2.id,
        "id_carro": response3.id
    })

    summary = f"{response1.message}, {response2.message}, {response3.message}"
    return {"sucess": True, "message": summary}


app = Flask(__name__)

def getPayloadErrors(data):
    errors = []
    if not data:
        errors.append("Nenhum dado enviado")
    
    trip_type = data.get("trip_type")
    if not trip_type:
        errors.append("Tipo de viagem não informado")
    
    if trip_type not in ["ida", "ida_volta"]:
        errors.append("Tipo de viagem inválido")
    
    dateIda = data.get("date_ida")
    if not dateIda:
        errors.append("Data de ida não informada")
    
    if trip_type == "ida_volta":
        dateVolta = data.get("date_volta")
        if not dateVolta:
            errors.append("Data de volta não informada")
        
    origin = data.get("origin")
    if not origin:
        errors.append("Origem não informada")
    
    destination = data.get("destination")
    if not destination:
        errors.append("Destino não informado")
    
    qtd_passengers = data.get("qtd_passengers")
    if not qtd_passengers:
        errors.append("Quantidade de passageiros não informada")
        
    hotel_name = data.get("hotel_name")
    if not hotel_name:
        errors.append("Nome do hotel não informado")
        
    hotel_qtd_days = data.get("hotel_qtd_days")
    if not hotel_qtd_days:
        errors.append("Quantidade de dias no hotel não informada")
        
    car_model = data.get("car_model")
    if not car_model:
        errors.append("Modelo do carro não informado")
        
    car_start_date = data.get("car_start_date")
    if not car_start_date:
        errors.append("Data de retirada do carro não informada")
        
    car_end_date = data.get("car_end_date")
    if not car_end_date:
        errors.append("Data de devolução do carro não informada")
    
    return errors

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    errors = getPayloadErrors(data)
    if errors:
        return jsonify({"errors": errors}), 400
    
    response = handleAgendarViagem(data)
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.getenv("PORT"), debug=True)
