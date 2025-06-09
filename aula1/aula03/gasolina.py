from selectors import SelectSelector

litros=float(input("quantos litros voce abasteceu"))
tipo=input(f"qual o tipo de gasolina/n"
           "g é para gasolina"
           "e para gasolina")
vGAS=5.8
VETA=4.9
if tipo == "g" or "G":

    valor=litros*vGAS
    print(f"sua gasolina vai ser {valor}")

else:
    valor2=litros*VETA
    print(f"o valor da sua gasolina sera {valor2}")


