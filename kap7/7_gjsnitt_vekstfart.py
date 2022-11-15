def g(x):
    return x**3-4*x
a=float(input("Velg et start av intervall: "))
b=float(input("Velg et sluttt av intervall: "))
def gvf_g(a,b):
    """Regner ut gjennomsnittlig vekstfart til g(x)
    i intervallet [a,b]"""
    dx=b-a
    dy=g(b)-g(a)
    return dy/dx
print (gvf_g(a,b))
