python -m grpc_tools.protoc -I. --python_out=../protos --grpc_python_out=../protos \
  companhiaAerea.proto \
  locadoraCarro.proto \
  redeHoteleira.proto


cp ../protos/companhiaAerea*.py ../agenciaViagem/
cp ../protos/locadoraCarro*.py ../agenciaViagem/
cp ../protos/redeHoteleira*.py ../agenciaViagem/

cp ../protos/companhiaAerea*.py ../companhiaAerea/
cp ../protos/locadoraCarro*.py ../locadoraCarro/
cp ../protos/redeHoteleira*.py ../redeHoteleira/

rm -rf ../protos/*.py
