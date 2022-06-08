MonFichier=open('Compte.csv','r')
Texte=MonFichier.read()
MonFichier.close()
Tableau=Texte.split('\n')
print(Tableau)
NbLignes=len(Tableau)
for i in range(NbLignes):
    Tableau.insert(3,'Paul'+';'+'14')
    print('***************')
    print(Tableau[i])
    MonFichier=open('Compte.csv','w')
    MonFichier.write(Tableau[i])
    MonFichier.close()

