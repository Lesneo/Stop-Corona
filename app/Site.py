#Importation de l'extention 'tkinter'
from tkinter import*
#Importation de l'extention 'time'
from time import*

#Ouverture d'une fenêtre
site = Tk()
site.title("Stop Corona")
site.config(width=800,height=850)

#Création d'un canevas
canevas = Canvas(site, bg='#B0E0E6')
canevas.place(width=800,height=850)

#Variable des produits et de la souris
connecter = False
produit_masque_petit = None
produit_masque_grand = None
produit_gel_petit = None
produit_masque_petit_lot = None
produit_masque_grand_lot = None
produit_gel_grand = None
bouger_la_souris = None
moove = False

#Système de déconnection au bout de 60 secondes d'innactivité
def Delog():
    global connecter
    if moove is False:
        connecter = False
        site.title('Stop Corona')
def Bouger(moove):
    moove = True
    site.after(60000,Delog)
def Deco():
    global moove
    moove=False
    site.after(1,Deco)
site.after(1,Deco)



#Interaction avec les icones du compte et du panier
def clicG(event):
    """Défini les actions du clic gauche de la souris sur les emplacements qui ne sont pas des boutons tel que :
    l'icone compte, panier."""
    global tableau
    print(event.x, event.y)
    #Event compte
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    tableau=texte.split('\n')
    if 750 < event.x < 793:
        if 12 < event.y < 64:
            #Fenêtre du compte
            compte = Toplevel()
            compte.title("compte")
            compte.config(width=400,height=250)
            #Fenetre en mode pop-up
            compte.grab_set()
            compte.transient(compte.master)
            #Identifiant
            utilisateur = Label(compte, text='Identifiant :')
            utilisateur.config(font= ('verdana' ,12 ,'normal' ))
            utilisateur.place(x=5,y=3)
            entry_utilisateur = Entry(compte)
            entry_utilisateur.place(x=115,y=5)
            #Mot de passe
            mot_de_passe = Label(compte, text='Mot de passe :')
            mot_de_passe.config(font= ('verdana' ,12,'normal'))
            mot_de_passe.place(x=5,y=50)
            entry_mot_de_passe = Entry(compte)
            entry_mot_de_passe.place(x=140,y=52)
            #Connection
            def connection_compte():
                """Permet de récupérer les logs (pseudo et mot de passe) et de se connecté au compte lié à ces logs"""
                global connecter
                mon_fichier=open('compte.csv','r')
                texte=mon_fichier.read()
                mon_fichier.close()
                tableau=texte.split('\n')
                entree_utilisateur = entry_utilisateur.get()
                entree_mot_de_passe = entry_mot_de_passe.get()
                Login = entree_utilisateur+';'+entree_mot_de_passe
                print(Login)
                if Login in tableau:
                    compte.destroy()
                    site.title('Stop Corona, compte : '+ entree_utilisateur)
                    connecter = True
                    print(connecter)
                else:
                    erreur_login = Label(compte, text="Erreur, l identifiant ne correspond pas au mot de passe \nou ce compte n existe pas veuiller vous créer un compte")
                    erreur_login.config(font=('verdana', 10,'normal'))
                    erreur_login.place(x=5,y=150)
            #fenetre de creation de compte
            def creer_account():
                """Crée une fenêtre en pop-up pour créer un compte"""
                creation_compte = Toplevel()
                creation_compte.title("Creation du compte")
                creation_compte.config(width=400,height=250)
                creation_compte.grab_set()
                creation_compte.transient(compte.master)
                def creer_le_compte():
                    """Permet de créer un compte et de placer les logs dans un fichier csv"""
                    mon_fichier=open('compte.csv','r')
                    texte=mon_fichier.read()
                    mon_fichier.close()
                    tableau=texte.split('\n')
                    entree_utilisateur = creer_entry_utilisateur.get()
                    entree_mot_de_passe = creer_entry_mot_de_passe.get()
                    entree_conf_mot_de_passe = conf_entry_mot_de_passe.get()
                    if entree_utilisateur+';'+entree_mot_de_passe in tableau:
                        erreur_identifiant = Label(creation_compte, text='L identifiant est déjà utiliser')
                        erreur_identifiant.config(font= ('verdana' ,12,'normal'))
                        erreur_identifiant.place(x=5,y=170)
                    else:
                        if entree_mot_de_passe == entree_conf_mot_de_passe:
                            print(tableau)
                            nombre_ligne=len(tableau)
                            tableau.insert(nombre_ligne,entree_utilisateur+';'+entree_mot_de_passe)
                            print('***************')
                            print(tableau)
                            nombre_ligne=len(tableau)
                            for i in range(nombre_ligne):
                                print(tableau[i])
                                mon_fichier=open('compte.csv','w')
                                mon_fichier.write(texte+'\n'+tableau[i])
                                mon_fichier.close()
                        else:
                            erreur_mot_de_passe = Label(creation_compte, text='Le mot de passe ne correspond pas')
                            erreur_mot_de_passe.config(font= ('verdana' ,12,'normal'))
                            erreur_mot_de_passe.place(x=5,y=150)
                #Identifiant
                creer_utilisateur = Label(creation_compte, text='Identifiant :')
                creer_utilisateur.config(font= ('verdana' ,12 ,'normal' ))
                creer_utilisateur.place(x=5,y=3)
                creer_entry_utilisateur = Entry(creation_compte)
                creer_entry_utilisateur.place(x=140,y=5)
                #Mot de passe
                creer_mot_de_passe = Label(creation_compte, text='Mot de passe :')
                creer_mot_de_passe.config(font= ('verdana' ,12,'normal'))
                creer_mot_de_passe.place(x=5,y=50)
                creer_entry_mot_de_passe = Entry(creation_compte)
                creer_entry_mot_de_passe.place(x=140,y=52)
                conf_mot_de_passe = Label(creation_compte, text='Confirmer :')
                conf_mot_de_passe.config(font= ('verdana' ,12,'normal'))
                conf_mot_de_passe.place(x=5,y=83)
                conf_entry_mot_de_passe = Entry(creation_compte)
                conf_entry_mot_de_passe.place(x=140,y=85)
                creer_le_compte = Button(creation_compte, text='CréerLecompte', command=creer_le_compte)
                creer_le_compte.config(bg='orange')
                creer_le_compte.place(x=10,y=120)
                compte.mainloop()
            #Bouton Connection et Création de compte
            Connection = Button(compte, text='Connection',command=connection_compte)
            Connection.config(bg='orange')
            Connection.place(x=5,y=90)
            creer_compte = Button(compte, text='Creer un compte',command=creer_account)
            creer_compte.config(bg='blue')
            creer_compte.place(x=95,y=90)
            compte.mainloop()
    #Panier
    if 665 < event.x < 715:
        if 15 < event.y < 60:
            #Fenetre du panier
            Panier = Toplevel()
            Panier.title("Panier")
            Panier.config(width=425,height=500)
            #Fenetre en mode pop-up
            Panier.grab_set()
            Panier.transient(Panier.master)
            if connecter is True:
                print('no')
            else:
                print(produit_masque_grand)
                #Masque chirurgical prix
                if produit_masque_petit is None:
                    masquepetit = Label(Panier, text='Masque chirurgical : X'+str(0)+', Prix : '+str(0))
                    masquepetit.config(font= ('verdana' ,12 ,'normal' ))
                    masquepetit.place(x=5,y=5)
                else:
                    prix_produit_masque_petit = float(produit_masque_petit)*4.95
                    masquepetit = Label(Panier, text='Masque chirurgical : X'+str(produit_masque_petit)+', Prix : '+str(format(prix_produit_masque_petit,'.2f'))+' €')
                    masquepetit.config(font= ('verdana' ,12 ,'normal' ))
                    masquepetit.place(x=5,y=5)
                #Masque SURPuissant prix
                if produit_masque_grand is None:
                    masquegrand = Label(Panier, text='Masque SURPuissant : X'+str(0)+', Prix : '+str(0))
                    masquegrand.config(font= ('verdana' ,12 ,'normal' ))
                    masquegrand.place(x=5,y=35)
                else:
                    prix_produit_masque_grand = float(produit_masque_grand)*17.95
                    masquegrand = Label(Panier, text='Masque SURPuissant : X'+str(produit_masque_grand)+', Prix : '+str(format(prix_produit_masque_grand,'.2f'))+' €')
                    masquegrand.config(font= ('verdana' ,12 ,'normal' ))
                    masquegrand.place(x=5,y=35)
                #Gel 100mL prix
                if produit_gel_petit is None:
                    gelpetit = Label(Panier, text='Gel 100mL : X'+str(0)+', Prix : '+str(0))
                    gelpetit.config(font= ('verdana' ,12 ,'normal' ))
                    gelpetit.place(x=5,y=65)
                else:
                    prix_produit_gel_petit = float(produit_gel_petit)*7.95
                    gelpetit = Label(Panier, text='Gel 100mL : X'+str(produit_gel_petit)+', Prix : '+str(format(prix_produit_gel_petit,'.2f'))+' €')
                    gelpetit.config(font= ('verdana' ,12 ,'normal' ))
                    gelpetit.place(x=5,y=65)
                #Masque chirurgical Lot prix
                if produit_masque_petit_lot is None:
                    masquepetit_lot = Label(Panier, text='Masque chirurgical (X10) : X'+str(0)+', Prix : '+str(0))
                    masquepetit_lot.config(font= ('verdana' ,12 ,'normal' ))
                    masquepetit_lot.place(x=5,y=95)
                else:
                    prix_produit_masque_petit_lot = float(produit_masque_petit_lot)*7.95
                    masquepetit_lot = Label(Panier, text='Masque chirurgical (X10) : X'+str(produit_masque_petit_lot)+', Prix : '+str(format(prix_produit_masque_petit_lot,'.2f'))+' €')
                    masquepetit_lot.config(font= ('verdana' ,12 ,'normal' ))
                    masquepetit_lot.place(x=5,y=95)
                #Masque SurPuissant Lot prix
                if produit_masque_grand_lot is None:
                    masquegrand_lot = Label(Panier, text='Masque SURPuissant (X10) : X'+str(0)+', Prix : '+str(0))
                    masquegrand_lot.config(font= ('verdana' ,12 ,'normal' ))
                    masquegrand_lot.place(x=5,y=125)
                else:
                    prix_produit_masque_grand_lot = float(produit_masque_grand_lot)*7.95
                    masquegrand_lot = Label(Panier, text='Masque SURPuissant (X10) : X'+str(produit_masque_grand_lot)+', Prix : '+str(format(prix_produit_masque_grand_lot,'.2f'))+' €')
                    masquegrand_lot.config(font= ('verdana' ,12 ,'normal' ))
                    masquegrand_lot.place(x=5,y=125)
                #Gel 500mL prix
                if produit_gel_grand is None:
                    gelgrand = Label(Panier, text='Gel 500mL : X'+str(0)+', Prix : '+str(0))
                    gelgrand.config(font= ('verdana' ,12 ,'normal' ))
                    gelgrand.place(x=5,y=155)
                else:
                    prix_produit_gel_grand = float(produit_gel_grand)*7.95
                    gelgrand = Label(Panier, text='Gel 500mL : X'+str(produit_gel_grand)+', Prix : '+str(format(prix_produit_gel_grand,'.2f'))+' €')
                    gelgrand.config(font= ('verdana' ,12 ,'normal' ))
                    gelgrand.place(x=5,y=155)

#Création de l'image du panier
fichier_panier = PhotoImage(file='Panier1.png')
image_panier = canevas.create_image(690, 40, image=fichier_panier)

#Création de l'image du profil
fichier_profil = PhotoImage (file = 'profil.png')
image_profil = canevas.create_image (767, 40, image=fichier_profil)

#Création de l'icone du site
fichiericone = PhotoImage (file = 'Coronavirus.png')
image_icone = canevas.create_image (75, 60, image=fichiericone)



#Article n°1: Masque chirurgical
#Image du masque chirurgical artc.n°1
fichier_masque_petit = PhotoImage(file = 'masquepetit.png')
image_masque_petit = canevas.create_image (125, 250, image=fichier_masque_petit)

#Carré de présentation
carre_article = canevas.create_rectangle (40, 175, 215, 430, width=2.5)

#texte d'article
texte_masque_petit = canevas.create_text(130,325, text='Masque Chirurgical')
canevas.itemconfig(texte_masque_petit, font= ('verdana' ,12 ,'normal' ))
texte_masque_petit_prix = canevas.create_text(130,357, text='4.95€')
canevas.itemconfig(texte_masque_petit_prix, font=('verdana', 12,'normal'), fill='blue')


#Bouton AjouterPanier pour artc.n°1
def ajouter_masque_petit():
    """Permet d'ajouter le nombre de masque chirurgicale"""
    global texte
    global produit_masque_petit
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    produit_masque_petit = int(entry_masque_petit.get())
    if connecter is True:
        print('yes')
bouton_masque_petit = Button(site, text='Ajouter', command=ajouter_masque_petit)
bouton_masque_petit.config(width=6, height=2, bg='orange')
bouton_masque_petit.place(x=155, y=375)
#Bouton + Article n°1
#Action du bouton
def plus_masque_petit():
    """Permet d'ajouter un masque chirurgicale"""
    entree_masque_petit = int(entry_masque_petit.get())
    entree_masque_petit = entree_masque_petit + 1
    entry_masque_petit.delete(0,END)
    entry_masque_petit.insert(0,entree_masque_petit)
#Création du Bouton
bouton_plus_masque_petit = Button(site, text='+', command=plus_masque_petit)
bouton_plus_masque_petit.config(width=3, height=1, bg='blue')
bouton_plus_masque_petit.place(x=67,y=370)
#Bouton - Article n°1
#Action du Bouton
def moins_masque_petit():
    """Permet de reduire d'un masque chirurgicale"""
    entree_masque_petit = int(entry_masque_petit.get())
    if entree_masque_petit > 1:
        entree_masque_petit = entree_masque_petit - 1
        entry_masque_petit.delete(0,END)
        entry_masque_petit.insert(0,entree_masque_petit)
#Création du Bouton
bouton_moins_masque_petit = Button(site, text='-', command=moins_masque_petit)
bouton_moins_masque_petit.config(width=3, height=1, bg='red')
bouton_moins_masque_petit.place(x=67,y=395)
#Entrer du nombre d'article
entry_masque_petit = Entry()
entry_masque_petit.place(x=105, y=385)
entry_masque_petit.config(width=7)
entry_masque_petit.insert(0,'1')


#Article n°2: Masque SurPuissant
#Image du masque SurPuissant artc.n°2
fichier_masque_grand = PhotoImage(file = 'masquegrand.png')
image_masque_grand = canevas.create_image (347, 250, image=fichier_masque_grand)

#Carré de présentation
carre_article = canevas.create_rectangle (260, 175, 435, 430, width=2.5)

#texte d'article
texte_masque_grand = canevas.create_text(347,325, text='Masque SURPuissant')
canevas.itemconfig(texte_masque_grand, font=('verdana',12,'normal'))
texte_masque_grand_prix = canevas.create_text(350,357, text=('17.95€'))
canevas.itemconfig(texte_masque_grand_prix, font= ('verdana' ,12 ,'normal' ), fill='blue')


#Bouton AjouterPanier pour artc.n°2
def ajouter_masque_grand():
    """Permet d'ajouter le nombre de masque SURPuissant"""
    global texte
    global produit_masque_grand
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    produit_masque_grand = int(entry_masque_grand.get())
    if connecter is True:
        print('yes')
bouton_masque_grand = Button(site, text='Ajouter', command=ajouter_masque_grand)
bouton_masque_grand.config(width=6, height=2, bg='orange')
bouton_masque_grand.place(x=375, y=375)
#Bouton + Article n°2
#Action du bouton
def plus_masque_grand():
    """Permet d'ajouter un masque SURPuissant"""
    entree_masque_grand = int(entry_masque_grand.get())
    entree_masque_grand = entree_masque_grand + 1
    entry_masque_grand.delete(0,END)
    entry_masque_grand.insert(0,entree_masque_grand)
#Création du Bouton
bouton_plus_masque_grand = Button(site, text='+', command=plus_masque_grand)
bouton_plus_masque_grand.config(width=3, height=1, bg='blue')
bouton_plus_masque_grand.place(x=287,y=370)
#Bouton - Article n°2
#Action du Bouton
def moins_masque_grand():
    """Permet de reduire d'un masque SURPuissant"""
    entree_masque_grand = int(entry_masque_grand.get())
    if entree_masque_grand > 1:
        entree_masque_grand = entree_masque_grand - 1 
        entry_masque_grand.delete(0,END)
        entry_masque_grand.insert(0,entree_masque_grand)
#Création du Bouton
bouton_moins_masque_grand = Button(site, text='-', command=moins_masque_grand)
bouton_moins_masque_grand.config(width=3, height=1, bg='red')
bouton_moins_masque_grand.place(x=287,y=395)
#Entrer du nombre d'article
entry_masque_grand = Entry()
entry_masque_grand.place(x=325, y=385)
entry_masque_grand.config(width=7)
entry_masque_grand.insert(0,'1')



#Article n°3: gel hydroalcoolique 75 ml
#Image du masque chirurgical artc.n°3
fichier_gel_petit = PhotoImage(file = 'gelpetit.png')
image_gel_petit = canevas.create_image (570, 250, image=fichier_gel_petit)

#Carré de présentation
carre_article = canevas.create_rectangle (480, 175, 655, 430, width=2.5)

#texte d'article
textegelpetit = canevas.create_text(567,325, text='Gel Hydroalcoolique')
canevas.itemconfig(textegelpetit, font=('verdana',12,'normal'))
textegelpetit_quant = canevas.create_text(570,340, text='(100mL)')
canevas.itemconfig(textegelpetit_quant, font=('verdana',8,'normal'))
textegelpetit_prix = canevas.create_text(570,357, text='7.95€')
canevas.itemconfig(textegelpetit_prix, font=('verdana',12,'normal'), fill='blue')

#Bouton AjouterPanier pour artc.n°3
def ajouter_gel_petit():
    """Permet d'ajouter le nombre de gel hydroalcoolique (100mL)"""
    global texte
    global produit_gel_petit
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    produit_gel_petit = int(entry_gel_petit.get())
    if connecter is True:
        print('yes')
bouton_gel_petit = Button(site, text='Ajouter', command=ajouter_gel_petit)
bouton_gel_petit.config(width=6, height=2, bg='orange')
bouton_gel_petit.place(x=595, y=375)
#Bouton + Article n°3
#Action du bouton
def plus_gel_petit():
    """Permet d'ajouter un gel hydroalcoolique (100mL)"""
    entree_gel_petit = int(entry_gel_petit.get())
    entree_gel_petit = entree_gel_petit + 1
    entry_gel_petit.delete(0,END)
    entry_gel_petit.insert(0,entree_gel_petit)
#Création du Bouton
bouton_plus_gel_petit = Button(site, text='+', command=plus_gel_petit)
bouton_plus_gel_petit.config(width=3, height=1, bg='blue')
bouton_plus_gel_petit.place(x=507,y=370)
#Bouton - Article n°3
#Action du Bouton
def moins_gel_petit():
    """Permet de soustraire d'un gel hydroalcoolique (100mL)"""
    entree_gel_petit = int(entry_gel_petit.get())
    if entree_gel_petit > 1:
        entree_gel_petit = entree_gel_petit - 1 
        entry_gel_petit.delete(0,END)
        entry_gel_petit.insert(0,entree_gel_petit)
#Création du Bouton
bouton_moins_gel_petit = Button(site, text='-', command=moins_gel_petit)
bouton_moins_gel_petit.config(width=3, height=1, bg='red')
bouton_moins_gel_petit.place(x=507,y=395)
#Entrer du nombre d'article
entry_gel_petit = Entry()
entry_gel_petit.place(x=545, y=385)
entry_gel_petit.config(width=7)
entry_gel_petit.insert(0,'1')


#Article n°4: Masque chirurgical en lot
#Image du masque chirurgical artc.n°4
fichier_masque_petit_lot = PhotoImage(file = 'masquepetit.png')
image_masque_petit_lot = canevas.create_image (125, 567, image=fichier_masque_petit_lot)

#Carré de présentation
carre_article = canevas.create_rectangle (40, 495, 215, 750, width=2.5)

#texte d'article
texte_masque_petit_lot = Label(site, text='Masque Chirurgical', fg='black')
texte_masque_petit_lot = canevas.create_text(130,645, text='Masque Chirurgical')
canevas.itemconfig(texte_masque_petit_lot, font= ('verdana' ,12 ,'normal' ))
texte_masque_petit_lot_quant = canevas.create_text(130,660, text='(X10)')
canevas.itemconfig(texte_masque_petit_lot_quant, font=('verdana',8,'normal'))
texte_masque_petit_lot_prix = canevas.create_text(130,677, text='39.95€')
canevas.itemconfig(texte_masque_petit_lot_prix, font=('verdana',12,'normal'), fill='blue')

#Bouton AjouterPanier pour artc.n°4
def ajouter_masque_petit_lot():
    """Permet d'ajouter au nombre de masque chirurgical(X10)"""
    global texte
    global produit_masque_petit_lot
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    produit_masque_petit_lot = int(entry_masque_petit_lot.get())
    if connecter is True:
        print('yes')
bouton_masque_petit_lot = Button(site, text='Ajouter', command=ajouter_masque_petit_lot)
bouton_masque_petit_lot.config(width=6, height=2, bg='orange')
bouton_masque_petit_lot.place(x=155, y=695)
#Bouton + Article n°4
#Action du bouton
def plus_masque_petit_lot():
    """Permet d'ajouter un masque chirurgical(X10)"""
    entree_masque_petit_lot = int(entry_masque_petit_lot.get())
    entree_masque_petit_lot = entree_masque_petit_lot + 1
    entry_masque_petit_lot.delete(0,END)
    entry_masque_petit_lot.insert(0,entree_masque_petit_lot)
#Création du Bouton
bouton_plus_masque_petit_lot = Button(site, text='+',command= plus_masque_petit_lot)
bouton_plus_masque_petit_lot.config(width=3, height=1, bg='blue')
bouton_plus_masque_petit_lot.place(x=67,y=690)
#Bouton - Article n°4
#Action du Bouton
def moins_masque_petit_lot():
    """Permet de reduire d'un masque chirurgical(X10)"""
    entree_masque_petit_lot = int(entry_masque_petit_lot.get())
    if entree_masque_petit_lot > 1:
        entree_masque_petit_lot = entree_masque_petit_lot - 1 
        entry_masque_petit_lot.delete(0,END)
        entry_masque_petit_lot.insert(0,entree_masque_petit_lot)
#Création du Bouton
bouton_moins_masque_petit_lot = Button(site, text='-',command=moins_masque_petit_lot)
bouton_moins_masque_petit_lot.config(width=3, height=1, bg='red')
bouton_moins_masque_petit_lot.place(x=67,y=715)
#Entrer du nombre d'article
entry_masque_petit_lot = Entry()
entry_masque_petit_lot.place(x=105, y=705)
entry_masque_petit_lot.config(width=7)
entry_masque_petit_lot.insert(0,'1')


#Article n°5: Masque SurPuissant en lot
#Image du masque chirurgical artc.n°1
fichier_masque_grand_lot = PhotoImage(file = 'masquegrand.png')
image_masque_grand_lot = canevas.create_image (347, 567, image=fichier_masque_grand)

#Carré de présentation
carre_article = canevas.create_rectangle (260, 495, 435, 750, width=2.5)

#texte d'article
texte_masque_grand_lot = canevas.create_text(347,645, text='Masque SURPuissant')
canevas.itemconfig(texte_masque_grand_lot, font=('verdana',12,'normal'))
texte_masque_grand_lot_quant = canevas.create_text(350,660, text='(X5)')
canevas.itemconfig(texte_masque_grand_lot_quant, font=('verdana',8,'normal'))
texte_masque_grand_prix_lot = canevas.create_text(350,677, text='69.95€')
canevas.itemconfig(texte_masque_grand_prix_lot, font=('verdana',12,'normal'), fill='blue')


#Bouton AjouterPanier pour artc.n°5
def ajouter_masque_grand_lot():
    """Permet d'ajouter au nombre de masque SURPuissant(X5)"""
    global texte
    global produit_masque_grand_lot
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    produit_masque_grand_lot = int(entry_masque_grand_lot.get())
    if connecter is True:
        print('yes')
bouton_masque_grand_lot = Button(site, text='Ajouter',command=ajouter_masque_grand_lot)
bouton_masque_grand_lot.config(width=6, height=2, bg='orange')
bouton_masque_grand_lot.place(x=375, y=695)
#Bouton + Article n°5
def plus_masque_grand_lot():
    """Permet d'ajouter un masque SURPuissant(X5)"""
    entree_masque_grand_lot = int(entry_masque_grand_lot.get())
    entree_masque_grand_lot = entree_masque_grand_lot + 1
    entry_masque_grand_lot.delete(0,END)
    entry_masque_grand_lot.insert(0,entree_masque_grand_lot)
#Création du Bouton
bouton_plus_masque_grand_lot = Button(site, text='+', command=plus_masque_grand_lot)
bouton_plus_masque_grand_lot.config(width=3, height=1, bg='blue')
bouton_plus_masque_grand_lot.place(x=287,y=690)
#Bouton - Article n°5
#Action du Bouton
def moins_masque_grand_lot():
    """Permet de reduire d'un masque SURPuissant(X5)"""
    entree_masque_grand_lot = int(entry_masque_grand_lot.get())
    if entree_masque_grand_lot > 1:
        entree_masque_grand_lot = entree_masque_grand_lot - 1 
        entry_masque_grand_lot.delete(0,END)
        entry_masque_grand_lot.insert(0,entree_masque_grand_lot)
#Création du Bouton
bouton_moins_masque_grand_lot = Button(site, text='-', command=moins_masque_grand_lot)
bouton_moins_masque_grand_lot.config(width=3, height=1, bg='red')
bouton_moins_masque_grand_lot.place(x=287,y=715)
#Entrer du nombre d'article
entry_masque_grand_lot = Entry()
entry_masque_grand_lot.place(x=325, y=705)
entry_masque_grand_lot.config(width=7)
entry_masque_grand_lot.insert(0,'1')



#Article n°6: gel hydroalcoolique 500 ml
#Image du masque chirurgical artc.n°3
fichiergelgrand = PhotoImage(file = 'gelgrand.png')
ImageGelgrand = canevas.create_image (580, 567, image=fichiergelgrand)

#Carré de présentation
carre_article = canevas.create_rectangle (480, 495, 655, 750, width=2.5)

#texte d'article
textegelgrand = canevas.create_text(567,645, text='Gel Hydroalcoolique')
canevas.itemconfig(textegelgrand, font=('verdana',12,'normal'))
textegelgrand_quant = canevas.create_text(567,660, text='(500mL)')
canevas.itemconfig(textegelgrand_quant, font=('verdana',8,'normal'))
textegelgrand_prix = canevas.create_text(537,677, text='16.95€')
canevas.itemconfig(textegelgrand_prix, font=('verdana',12,'normal'), fill='blue')


#Bouton AjouterPanier pour artc.n°6
def AjouterGelGrand():
    """Permet d'ajouter au nombre de gel hydroalcoolique (500mL)"""
    global texte
    global produit_gel_grand
    mon_fichier=open('compte.csv','r')
    texte=mon_fichier.read()
    mon_fichier.close()
    produit_gel_grand = int(entry_gel_grand.get())
    if connecter is True:
        print('yes')
bouton_gel_grand = Button(site, text='Ajouter',command=AjouterGelGrand)
bouton_gel_grand.config(width=6, height=2, bg='orange')
bouton_gel_grand.place(x=595, y=695)
#Bouton + Article n°6
def plus_gel_grand():
    """Permet d'ajouter un gel hydroalcoolique (500mL)"""
    entree_gel_grand = int(entry_gel_grand.get())
    entree_gel_grand = entree_gel_grand + 1
    entry_gel_grand.delete(0,END)
    entry_gel_grand.insert(0,entree_gel_grand)
#Création du Bouton
bouton_plus_gel_grand = Button(site, text='+', command=plus_gel_grand)
bouton_plus_gel_grand.config(width=3, height=1, bg='blue')
bouton_plus_gel_grand.place(x=507,y=690)
#Bouton - Article n°6
#Action du Bouton
def MoinsGelGrand():
    """Permet de soustraire d'un gel hydroalcoolique (500mL)"""
    entree_gel_grand = int(entry_gel_grand.get())
    if entree_gel_grand > 1:
        entree_gel_grand = entree_gel_grand - 1 
        entry_gel_grand.delete(0,END)
        entry_gel_grand.insert(0,entree_gel_grand)
#Création du Bouton
bouton_moins_gel_grand = Button(site, text='-', command=MoinsGelGrand)
bouton_moins_gel_grand.config(width=3, height=1, bg='red')
bouton_moins_gel_grand.place(x=507,y=715)
#Entrer du nombre d'article
entry_gel_grand = Entry()
entry_gel_grand.place(x=545, y=705)
entry_gel_grand.config(width=7)
entry_gel_grand.insert(0,'1')


#Titre
Titre = canevas.create_text(400,45, text='Stop CORONA')
canevas.itemconfig(Titre, font=('times',40,'bold'), fill='red')

#Definition de bouger et du clic gauche de la souris
site.bind('<Motion>', Bouger)
site.bind('<Button-1>', clicG)
site.mainloop()