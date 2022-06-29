sp = int(6783643)
rj = int(3667866)
mg = int(2922988)
es = int(2716548)
out = int(1984953)
#######################
soma = sp + rj + mg + es + out
print("percentual total mensal da distribuidora:\n",soma)

psp = ((sp/soma)*100)
prj = ((rj/soma)*100)
pmg = ((mg/soma)*100)
pes = ((es/soma)*100)
pout = ((out/soma)*100)

print('Porcentagem de SP {:.2f}%'.format(psp))
print('Porcentagem de RJ {:.2f}%'.format(prj))
print('Porcentagem de MG {:.2f}%'.format(pmg))
print('Porcentagem de ES {:.2f}%'.format(pes))
print('Porcentagem de OUT {:.2f}%'.format(pout))
