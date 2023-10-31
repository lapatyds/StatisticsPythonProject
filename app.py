import math as mt
import os
import json
import requests
import xlsxwriter
from msgraph import GraphServiceClient


print('El número PI es:', mt.pi)
response = requests.get('https://api.github.com')
print(response)

"""
workbook = xlsxwriter.Workbook("hello_world.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1", "Hello world")

workbook.close() 

"""
for f in os.listdir("/app"):
    print(f)
# Abrir el archivo example.json
f = open("/app/example.json", "r")
datos = json.load(f)

print(datos)
print(datos["pedido"]["tamano"])
print(datos["pedido"]["precio"])
print(datos["pedido"]["toppings"])
print(datos["pedido"]["cliente"])

