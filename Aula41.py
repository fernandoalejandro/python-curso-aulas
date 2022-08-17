import re

texto = "curso de python do cfb cursos, canal do youtube"

resultado = re.search('curso',texto)

pi=resultado.start()
pf=resultado.end()
tamanho = pf - pi


print(resultado.start)
print(resultado.end)
print(tamanho)

