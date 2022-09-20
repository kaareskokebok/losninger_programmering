tall1 = float(input("Skriv et tall."))
tall2 = float(input("Skriv et nytt tall."))

if tall1 == tall2:
    print("Tallene er like store")
elif tall1 > tall2:
    print(f"{tall1} er større enn {tall2}")
else:
    print(f"{tall2} er større enn {tall1}")