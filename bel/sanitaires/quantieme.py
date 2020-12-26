import datetime
from datetime import datetime


#lot = "SC2941D"

def calcul_date_prod(lot):
    verif = str(lot[0])
    nombres = "0123456789"
    if verif not in nombres:
        try:
            quantieme = str(lot[2:-2]) # str() car l'objet pandas est series
            quantieme_converti = datetime.strptime(quantieme, '%j')
            newformat = quantieme_converti.strftime('%d/%m/')
            annee_auj = datetime.now().year
            prod_initiale = newformat + str(annee_auj)
            date_auj = datetime.now()
            date_auj = date_auj.strftime('%d/%m/%Y')

            #remise des dates en objets date :
            prod_deux = datetime.strptime(prod_initiale, '%d/%m/%Y')
            date_auj = datetime.strptime(date_auj, '%d/%m/%Y')

            if date_auj > prod_deux:
                return(prod_initiale)
            else :
                annee_moins_un = annee_auj - 1
                prod_moins_un = newformat + str(annee_moins_un)
                return(prod_moins_un)
        
        except:
            return("erreur")
    else:
        return("erreur")
