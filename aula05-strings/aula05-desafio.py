nomes = ["Ana", "Maria", "Enzo", "Leo"]

for n in range(len(nomes)):
    for j in range(n+1, len(nomes)):
        print(nomes[n], nomes[j])
