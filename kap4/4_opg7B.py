
print("Du kan velge mellom dagskort(d) eller 3-timers kort(k).")
billettype = input("Oppgi ønsket bilettype d/k:  ")
if billettype == "d":
    alder = int(input("Oppgi alder: "))
    if alder < 16:
        print("Din totale bilettpris er 200")
    else:
        print("Din totale bilettpris er 420")
elif billettype == "k":
    alder = int(input("Oppgi alder: "))
    if alder < 16:
        print("Din totale bilettpris er 120")
    else:
        print("Din totale bilettpris er 250")
