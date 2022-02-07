from flask_restful import Resource, reqparse #reqpaser: para receber os elementos JSON da nossa requisição
from models.hotel import HotelModel

hoteis = [
    {
    'hotel_id': 'alpha',
    'nome': 'Alpha Hotel',
    'estrelas': 4.3,
    'diaria': 420.34,
    'cidade': 'Rio de Janeiro'
    },
    {
    'hotel_id': 'bravo',
    'nome': 'Bravo Hotel',
    'estrelas': 4.4,
    'diaria': 380.90,
    'cidade': 'Santa Catarina'
    },
    {
    'hotel_id': 'charlie',
    'nome': 'Charlie Hotel',
    'estrelas': 3.9,
    'diaria': 320.20,
    'cidade': 'Santa Catarina'
    }
]



class Hoteis(Resource): #vai ser um recurso dessa Api
    def get(self):
        return {'hoteis': [hotel.json() for hotel in HotelModel.query.all()]} #SELECT * FROM hoteis

#estamos criando o CRUD
class Hotel(Resource):

    atributos = reqparse.RequestParser() #instanciar um request parser
    atributos.add_argument('nome', type=str, required=True, help="This field 'nome' cannot be left blank") #PEGA OS ARGUMENTOS DA REQUISIÇÃO POST
    atributos.add_argument('estrelas', type=float, required=True, help="The field 'estrelas' cannot be left blank")
    atributos.add_argument('diaria')
    atributos.add_argument('cidade')

    def get(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            return hotel.json()
        return {'message': 'Hotel not found.'}, 404

    def post(self, hotel_id):
        if HotelModel.find_hotel(hotel_id):
            return {"message": "Hotel id '{}' already exists.".format(hotel_id)}, 400

        dados = Hotel.atributos.parse_args() #cria um construtor. chave e valor de todos os argumentos passados
        hotel = HotelModel(hotel_id, **dados)
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json()
#        novo_hotel = hotel_objeto.json() #linhas de codigo excluidas conforme aula 43 cerca de 9 minutos
#        hoteis.append(novo_hotel) #linhas de codigo excluidas conforme aula 43 cerca de 9 minutos
#        return novo_hotel, 201 #linhas de codigo excluidas conforme aula 43 cerca de 9 minutos

    def put(self, hotel_id):

        dados = Hotel.atributos.parse_args() #cria um construtor. chave e valor de todos os argumentos passados
    #    hotel = HotelModel(hotel_id, **dados) #retirada essa criação da instancia na aula 45 cerca de 2m30s
        hotel_encontrado = HotelModel.find_hotel(hotel_id)
        if hotel_encontrado:
            hotel_encontrado.update_hotel(**dados) #atualizado aula 45 cerca de 1m30s
            hotel_encontrado.save_hotel()
            return hotel_encontrado.json(), 200
        hotel = HotelModel(hotel_id, **dados) # se o hotel nao foi encontrado nós iremos cria-lo
        try:
            hotel.save_hotel()
        except:
            return {'message': 'An internal error ocurred trying to save hotel.'}, 500
        return hotel.json(), 201 #created

    def delete(self, hotel_id):
        hotel = HotelModel.find_hotel(hotel_id)
        if hotel:
            try:
                hotel.delete_hotel()
            except:
                return {'message': 'An error ocurred trying to delete hotel.'}, 500
            return {'message': 'Hotel deleted.'}
        return {'message': 'Hotel not found'}, 404
