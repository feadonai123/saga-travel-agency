1. Buildar protos:
```
cd protos && ./build.sh
```

2. Rodar agencia viagem
```
cd agenciaViagem && python agenciaViagem.py
```

3. Rodar companhia aérea
```
cd companhiaAerea && python companhiaAearea.py
```

4. Rodar locadora Carro
```
cd locadoraCarro && python locadoraCarro.py
```

5. Rodar rede hoteleria
```
cd redeHoteleira && python redeHoteleria.py
```

## Teste:
### Chamar rota POST http://localhost:3000/process HTTP/1.1

Exemplo de payload:

```
{
  "trip_type": "ida_volta",
  "date_ida": "2021-10-10",
  "date_volta": "2021-10-20",
  "origin": "São Paulo",
  "destination": "Rio de Janeiro",
  "qtd_passengers": 2,
  "hotel_qtd_days": 10,
  "hotel_name": "Copacabana Palace",
  "car_model": "Fiat Uno",
  "car_start_date": "2021-10-10",
  "car_end_date": "2021-10-20"
}
```