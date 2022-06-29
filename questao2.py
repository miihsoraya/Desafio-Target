def f(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return f(n-1) + f(n-2)
        
def verif():
  n = int(input('Digite o numero para verificacao:\n' ))
  for i in range(1,8+1): #exibe ate a seq 8
    if(n == (f(i))):
      print("Numero pertence a sequencia\n")
      return
  print("Numero NAO pertence a sequencia\n")

while True:
  verif()
