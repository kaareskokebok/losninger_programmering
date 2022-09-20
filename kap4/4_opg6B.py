import random as r

tall1 = r.randint(1,4)
tall2 = r.randint(1,4)

if tall1 == tall2:
    print(f"{tall1} og {tall2}, tallene er like")
else:
    print(f"{tall1} og {tall2}, ikke like")