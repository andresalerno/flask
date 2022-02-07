import sqlite3

connection = sqlite3.connect('banco.db')
cursor = connection.cursor() #seleciona alguma coisa

cria_tabela = "CREATE TABLE IF NOT EXISTS hoteis (hotel_id text PRIMARY KEY, \
    nome text, estrelas real, diaria real, cidade text)"


cria_hotel = "INSERT INTO hoteis VALUES ('alpha', 'Alpha Hotel', 4.3, 345.30, 'Rio de Janeiro')"

cursor.execute(cria_tabela)
cursor.execute(cria_hotel)

connection.commit()
connection.close()

# na aula 43 cerca de 7 minutos ele exclui esse arquivo.
