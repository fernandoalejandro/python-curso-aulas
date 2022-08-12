r = lambda x,func:x+func(x)

result = r(2,lambda x:x*x)
print(result)