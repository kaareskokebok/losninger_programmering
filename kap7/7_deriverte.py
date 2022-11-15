def g(x):
    return x**3 - 4*x

def derivert_g(x):
    """Regner ut derivert til g(x)"""
    dx=0.0001
    dy=g(x+dx)-g(x)
    return dy/dx
for i in range (-3,4):
    d_g=derivert_g(i)
    if d_g>0:
        print(f"x={i} Den deriverte er {d_g:.1f}, g vokser")
    if d_g<0:
         print(f"x={i} Den deriverte er {d_g:.1f}, g minker")
