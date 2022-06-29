frase = input("Qual a frase: \n")
l=[]
for i in frase:
  l.append(i)
  
tamanho=len(l)

for n in range(tamanho):
  print(l.pop(),end="")
