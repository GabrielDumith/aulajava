pin="123456"
x=input("digite sua senha:")
tentativas=1
while x!=pin:
    x=input("digite sua senha novamente")
    tentativas+=1
    if pin==x:
      print("bem-vindo")

    if tentativas>2:
        print("senha bloqueada")
        break



