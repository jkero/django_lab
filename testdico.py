outer = ['a', 'b', 'c']
inner = [[1,2,3],[4,5,6],[7,8,9]]
dico = {}
for o in outer:
    if o not in dico:
        nouv = {o:[]}
        dico.update(nouv)
        list_c = []
    for i in inner:
        list_c.append(i)
        dico[o].append(list_c)

print(dico)
