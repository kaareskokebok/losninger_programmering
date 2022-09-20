#Oppgave 4.2
import random
tall = random.randint(1, 6)
print(tall)

if tall == 6:
    print(f"Fantastisk du fikk en {tall}-er")
    
if tall < 5:
    print("Du fikk mindre enn 5")
    
if tall > 2:
    print("Du fikk noe større enn 2")