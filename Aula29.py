carros=['HRV','AUDI','FOCUS','PALIO','FUSION']

itCarros=iter(carros)

while itCarros:
    try:
        print(next(itCarros))
    except StopIteration:
        break
         
    