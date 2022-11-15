def f(x):
    """Regn ut overskuddet i kr ved x enheter"""
    return -0.015*x**2+12*x-400
maks=f(288)
a=2
while f(a)<maks:
    a+=1
print(a,f(a))
