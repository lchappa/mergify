import pandas as pd
double = 0
triple = 0
dataset=pd.read_fwf('input.txt', names=["ID"])      #Place le fichier de données dans une DataFrame avec Id en index de colonne.
for row_num, obj in zip(dataset.index, dataset["ID"].str.findall(r'(.)(?=.+\1)')):   #Dans cette DataFrame, on recherche dans chaque ligne les caractères présents plusieurs fois. row_num contient le numéro de la ligne et obj contient chaque lettre présente plusieurs fois dans cette ligne.
    doubleFound = False #Initialisation/Remise à la valeur par défaut de deux variables booléennes 
    tripleFound = False
    ID = str(dataset.loc[int(row_num)].values[0])   #Récupération de l'ID 
    i = 0
    for i in range (0, len(obj)-1): #Comme la taille du tableau obj est variable, une boucle for est placée pour éviter des erreurs d'index. La fonction len() donnant le nombre de lettres présentes dans le tableau, on retire 1 pour compenser le départ du tableau à l'index 0.
        letter = obj[i]
        a = 0
        for letters in ID:    #On compare chaque lettre dans l'ID aux lettres présentes dans le tableau obj. Si les lettres correspondent, alors on incrémente a.
            if(letters == letter):
                a=a+1
        match a:              #Une fois la lettre comparée à l'entièreté du string ID, on regarde la valeur de a.
            case 2:           #Si a = 2, on incrémente double, puis on met doubleFound en True pour éviter qu'une autre lettre du même string ID n'incrémente double à son tour, faussant le calcul.
                if not doubleFound:     
                    double = double+1
                    doubleFound = True
            case 3:           #Même chose si a = 3 avec triple et tripleFound.
                if not tripleFound:
                    triple = triple+1
                    tripleFound = True
print("Checksum = "+ str(double*triple))    #Calcul du checksum en multipliant le nombre de doubles par le nombre de triples.

#---------------------------------------------------------------------------    Part 2  ---------------------------------------------------------------------------------------------------------------------------

for i in range(len(dataset)):
    for j in range(i + 1, len(dataset)):    #On compare chaque ligne du tableau à toutes les autres
        if sum(a != b for a, b in zip(dataset.loc[i].values[0], dataset.loc[j].values[0])) == 1:    #On compte le nombre de caractères différents
            pos = 0     #On initialise une variable pour avoir la position de la lettre différente
            for a, b in zip(dataset.loc[i].values[0], dataset.loc[j].values[0]):    #On compare les lettres des deux IDs pour trouver la lettre différente
                if a != b:
                    common_letters = dataset.loc[i].values[0][:pos] + "" + dataset.loc[i].values[0][pos+1:] #On prend l'ID jusqu'à la position de la lettre, on la remplace par rien puis on prend la suite de l'ID
                    print(common_letters) #Renvoie toutes les lettres communes aux deux ID
                    exit()
                pos +=1     #On incrémente la variable après la boucle if pour qu'au premier passage, pos soit égal à 0 et non à 1, ce qui décalerait tout de 1 caractère.