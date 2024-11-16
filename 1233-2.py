#####
#
# Recherche des nombres du i*i+j*j=1*100+j. exemple 1233 = 12*12+33*33
# Auteur : silanoc
# date : 5 octbre 2014
#
#####




#Fonction menu
def menu():
  choix=input("Votre choix")
  return(choix)

#Afficher l'intro
print ("""
#######################################################################
#                                                                     #
#  Petit logiciel pour recherche des nombres du type i*i+j*j=1*100+j  #
#  Exemple : 1233 = 12*12+33*33                                       #
#                                                                     #
#######################################################################
""")

#Demander l'amplitude de la recherche
print("""
Voulez vous lancer la recherche entre
1) 1-99
2) 100-999
3) 1000-9999
4) 10000-99999 ! Attention, plusieurs heures sont nécessaires !
------------
5) A propos
""")
choixtaille=menu()

#Donner des information (A propos) et/ou définir les valeurs des bornes la recherche
if choixtaille=="5":
    print ("""
  Codage par Silanoc le 5 octobre 2014
  L'idée m'est venue par la lecture du noméro 18 du "monde des mathématiques"
  Cela semble être des nombres narcissiques
  http://www.recreomath.qc.ca/dict_narcissique_n.htm
  http://mathafou.free.fr/pba/sol019b.html
  """)
    input(" Appuyez sur une touche pour continuer avec une recherhce de niveau 1.")
    bornemoins=1
    borneplus=99
elif choixtaille=="1":
    bornemoins=1
    borneplus=99
elif choixtaille=="2":
    bornemoins=10
    borneplus=999
elif choixtaille=="3":
    bornemoins=100
    borneplus=9999
elif choixtaille=="4":
    bornemoins=1000
    borneplus=99999   


print ("Résultat(s) :")
#La recherche ebn elle-même
for i in range (bornemoins,borneplus):
    for j in range (bornemoins,borneplus):
        if ((i*i+j*j)==(i*(borneplus+1)+j)):
            print (i , j)
        
            

##
# Attention les choix 3 est long et le 4 est très long à calculer
##

'''
Les résultats calculé sont
12-33
88-33

10-100
990-100

558-2353
9412-2353

17650 38125
25840 43776
74160 43776
82350 38125
99010 9901

idée trouver dans le livre "le monde des maths N°18 - nombres remarquables

'''


