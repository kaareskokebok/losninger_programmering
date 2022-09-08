klokka_naa = 14
timer = 51
ankomst = klokka_naa + timer
hele_dager = ankomst//24
klokka_ankomst = ankomst%24
print(f'din venn kommer om {hele_dager} dager.')
print('klokka' ,klokka_ankomst)