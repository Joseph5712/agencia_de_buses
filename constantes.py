import sqlite3 as sql

# Lista de constantes
adminRole = 'admin'
role = 'pasajero'
db = sql.connect('buses_system.db')
lugares = ["San José","Alajuela","Heredia","Cartago","San Carlos","Puntarenas","Limón"]
placaLetras ="QWRTYPSDFGHJKLZXCVBNM"
placaNumbers = "0123456879"
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'