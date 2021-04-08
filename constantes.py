import sqlite3 as sql

# Lista de constantes
adminRole = 'admin'
role = 'pasajero'
db = sql.connect('buses_system.db')
lugares = ["San José","Alajuela","Heredia","Cartago","San Carlos","Puntarenas","Limón"]