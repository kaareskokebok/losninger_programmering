import random

forseint = random.random() < 0.4
glemt_konfekt = random.random() < 0.5

if glemt_konfekt or forseint:
    print("Lønnstrekk!")
else:
    print("Alt bra, ingen lønnstrekk")
