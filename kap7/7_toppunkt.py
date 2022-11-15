def f(x):
    """Regn ut overskuddet i kr ved x enheter"""
    return -0.015*x**2+12*x-400
help(f)
overskudd=f(288)
if overskudd >=0:
    print(f"Et overskudd på {overskudd:.2f}kr")