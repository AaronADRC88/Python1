__author__ = 'aferreiradominguez'
#un diccionario d e unha estructura condicional
d={1:"a",2:"b"}
print (d[1])
if d[1]==("b"):
    print ("chachi")
elif d[1]==("a"):
    print ("BEEEN!!!")
else:
    print ("merda")
valor= "par" if (d[1]== "b") else "impar"
print (valor)
idade=20
while idade>15:
    idade=idade+1
    break
print ("felices "+str(idade))
while True:
    if idade==28:
        break
    idade=idade+1
    print ("felices "+str(idade))
for ele in d :
    print (ele,d[ele])
