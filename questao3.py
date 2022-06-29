import json

with open('dados.json') as f:
  data = json.load(f)
f.close()
#################################################

maior = data[0]['valor']
menor = data[0]['valor']
soma=0

for i in range(len(data)):
  if data[i]['valor'] >= maior:
    maior = data[i]['valor']
  if data[i]['valor'] <= menor:
    menor = data[i]['valor']
  soma += data[i]['valor']
  print(i+1,": ",data[i]['valor'])  #Printando lista
  
media = soma/(len(data)-8)
print("\nMenor valor de faturamento do mês: ",menor)
print("Maior faturamento do mês foi: ",maior)
print('Média dos faturamentos: {:.2f}'.format(media))
print('Dias em que o faturamento foi superior a media mensal: ')

for i in range(len(data)):
  if data[i]['valor'] > media:
    print(data[i]['dia'],end=",")
