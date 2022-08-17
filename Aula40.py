import re #RegEx

texto = 'curso de python do cfb cursos , canal do youtube'


pesq = input('Pesquisar: ')
res = re.findall(pesq,texto)

print(res)
qtde=res.count
print('Qtde: ',qtde)

for t in res:
    print(t)