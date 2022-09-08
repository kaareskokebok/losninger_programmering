sek=15333
timer=(sek/60)//60
minutter=(sek-timer*60*60)//60
sekunder=sek-timer*60*60-minutter*60
print(sek,"sekunder er ", timer,"timer ",minutter,"minutter og ",sekunder,"sekunder.")