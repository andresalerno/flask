from flask import Flask # flask em minusculo é o pacote e o maisuclo é o recurso/classe
from flask_restful import Api
from resources.hotel import Hoteis, Hotel #criamos o nosso próprio recurso/resource e/ou biblioteca

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///banco.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)

@app.before_first_request
def cria_banco():
    banco.create_all()

# adicionar o nosso recurso
api.add_resource(Hoteis, '/hoteis')
api.add_resource(Hotel, '/hoteis/<string:hotel_id>')

if __name__ == '__main__':
    from sql_alchemy import banco
    banco.init_app(app) #se ele for chamado do app.py ele será executado
    app.run(debug=True)

#http://127.0.0.1:5000/hoteis #acabamos de criar um recurso que vai se estender para hoteis. Se tudo estiver certo nós vamos receber um json com essa informação (lista de hoteis)
