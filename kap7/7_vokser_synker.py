def g(x):
    return x**2-4*x+3

x=-0.5
while x<4:
    x=x+0.5
    dy=(g(x+0.01)-g(x))
    #print(f"x={x}")
    if dy>0:
        print(f"x={x}, g(x) vokser")

    elif dy<0:
        print(f"x={x}, g(x) synker")
        
    elif dy==0:
        print(f"x={x}, g(x) verken vokser eller synker")
