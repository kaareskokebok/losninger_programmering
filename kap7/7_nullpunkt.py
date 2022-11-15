def g(x):
    return -23.4+(7/3)*x

a=1
while g(a)<0:
    a+=0.00001
    
print(f"x-verdien til nullpunktet er {a:.3f}")