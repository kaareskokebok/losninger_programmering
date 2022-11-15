def h(x):
    return x**2-4*x

print("x...h(x)")
for i in range(-2,5):
    print(f"{i:4}{h(i):>3}")