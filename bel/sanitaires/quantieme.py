import datetime
from datetime import datetime


#lot = "SC2941D"

def calcul_date_prod(lot):
    lot_premier_caractere = str(lot[0])
    chiffres = "0123456789"
    # on s'assure que le lot commence par une lettres et non un chiffre : 
    if lot_premier_caractere not in chiffres: 
    # sinon, certains lots comme "171612" remplissent la condition et renvoient une date prod erronée
        try:
            quantieme = str(lot[2:-2]) # str() car l'objet pandas est series
            quantieme_converti = datetime.strptime(quantieme, '%j') #%j = format for day of the year, default year = 1900
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
            return("MMBE")
    else:
        return("MMBE")
