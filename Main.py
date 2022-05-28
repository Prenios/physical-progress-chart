#Definitions des fonctions
def avancement_maximal(a,n_Ai,b,n_Bi):
    x_max=min(n_Ai/a, n_Bi/b)
    return x_max

def etat_final(a,n_Ai,b,n_Bi,x_max):
    n_A=n_Ai-a*x_max
    n_B=n_Bi-b*x_max
    
    if (n_A<1E-10 and n_B<1E-10):
        print("Nous sommes dans les conditions stoechiométriques")
        print("x_max = {0:1.2E} mol.".format(x_max))
    elif n_A<1E-10 :
        n_A=0
        print("A est le réactif limitant.")
        print("x_max = {0:1.2E} mol.".format(x_max))
        print("A la fin de la transformation, il n'y a plus de A.")
        print("Il reste {0:1.2E} mol de B.".format(n_B))
    else :
        n_B=0
        print("B est le réactif limitant.")
        print("x_max = {0:1.2E} mol.".format(x_max))
        print("A la fin de la transformation, il n'y a plus de B.")
        print("Il reste {0:1.2E} mol de A.".format(n_A))

#Partie principale du programme
#Equations
a=float(input("Entrez le nombre stoechiométrique a :"))
n_Ai=float(input("n_Ai = "))
b=float(input("Entrez le nombre stoechiométrique b :"))
n_Bi=float(input("n_Bi = "))
x_max=avancement_maximal(a,n_Ai,b,n_Bi)
etat_final(a,n_Ai,b,n_Bi,x_max)
