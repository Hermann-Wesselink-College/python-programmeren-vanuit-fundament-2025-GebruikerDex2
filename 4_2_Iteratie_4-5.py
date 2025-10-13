#Opdrachten 4 en 5 van paragraaf 4.2 
	jaar = 0
saldo = 100
while saldo < 400: 
    saldo = saldo * 1.1
    jaar = jaar + 1
print("Jaar is: " + str(jaar))
print("Saldo is: " + str(saldo))
 
saldo = 100000
opname = 5000
jaar = 0
 
while ((saldo * 1.04) - opname) > 0:
  saldo = saldo * 1.04
  saldo = saldo - opname
  jaar = jaar + 1
  
  if jaar >= 100:
    break
  
if jaar >= 100:
  print("Dat kan je hele leven!")
else:
  print("Dit kan " + str(jaar) + " jaar")
