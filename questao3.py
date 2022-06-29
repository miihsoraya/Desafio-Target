import json

with open('dados.json') as f:
  data = json.load(f)
f.close()
########################################

maior = data[0]['valor']
menor = data[0]['valor']
soma=0

for i in range(len(data)):
  if data[i]['valor'] >= maior:
    maior = data[i]['valor']
  if data[i]['valor'] <= menor:
    menor = data[i]['valor']
  soma += data[i]['valor']
  media = soma/(len(data)-8)
  print(i+1,": ",data[i]['valor'])



print("Menor valor de faturamento do mês: ",menor)
print("Maior faturamento do mês foi: ",maior)
print('{:.2f}'.format(soma))
