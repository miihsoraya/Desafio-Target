import json

with open('dados.json') as f:
  data = json.load(f)
f.close()
####################################################
soma=0
maior = data[0]['valor']
menor = data[0]['valor']

for v in data:
  valor = v.get('valor')    #armazenando valor do arquivo em variavel
  if valor >= maior:
    maior = valor
  if valor <= menor:
    menor = valor
  soma += valor    #somando tdos os valores da lista
  print(v.get('dia'),": ",valor)  #Printando lista
  
media = soma/(len(data)-8)    #8 dias referentes aos finais de semana do mes
print("\nMenor valor de faturamento do mês: ",menor)
print("Maior faturamento do mês foi: ",maior)
print('Média dos faturamentos: {:.2f}'.format(media))
print('Dias em que o faturamento foi superior a media mensal: ')

for v in data:
  if v.get('valor') > media:    #verificando dias que o valor é maior q a media
    print(v.get('dia'),end=",")
