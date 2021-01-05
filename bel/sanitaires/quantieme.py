import datetime
from datetime import datetime

# -------------------------------------------------------------------
# lot = "SC2941D" (quantième 294, soit 20 Octobre, servira d'exemple)
# -------------------------------------------------------------------


def calcul_date_prod(lot):
    
    lot_premier_caractere = str(lot[0]) 
    chiffres = "0123456789"
    date_auj = datetime.now()


    if lot_premier_caractere not in chiffres: 

        try:
            quantieme = str(lot[2:-2])
            annee_auj = str(datetime.now().year)
            quantieme_et_annee_auj = quantieme + "/" + annee_auj
            lot_un = datetime.strptime(quantieme_et_annee_auj, '%j/%Y')
            
            if date_auj > lot_un:
                return lot_un.strftime('%d/%m/%Y')
                
            else:
                annee_auj_moins_un = int(annee_auj) - 1
                quantieme_et_annee_moins_un = quantieme + "/" + str(annee_auj_moins_un)
                lot_deux = datetime.strptime(quantieme_et_annee_moins_un, '%j/%Y')
                return lot_deux.strftime('%d/%m/%Y')   

        except:
            return("MMBE")
            
    else:
        return("MMBE")




'''
def calcul_date_prod(lot):
    lot_premier_caractere = str(lot[0]) # premier élément du lot
    chiffres = "0123456789"
    # on s'assure que le lot commence par une lettres et non un chiffre : 
    if lot_premier_caractere not in chiffres: 
    # sinon, certains lots comme "171612" remplissent la condition et renvoient une date prod erronée
        try:
            quantieme = str(lot[2:-2]) # on isole 294, sans 'SC' et '1D' [str() car l'objet pandas est series]
            quantieme_converti = datetime.strptime(quantieme, '%j') #%j = format for day of the year, default year = 1900
            newformat = quantieme_converti.strftime('%d/%m/') # converts date object in string object, on obtient "20/10/"
            annee_auj = datetime.now().year # renvoie l'année d'aujourd'hui
            prod_initiale = newformat + str(annee_auj) # "20/10/" + "2020" = "20/10/2020"
            date_auj = datetime.now()
            date_auj = date_auj.strftime('%d/%m/%Y') # date du jour en objet str et au format jj/mm/aaaa

            #remise des deux dates en objets date :
            prod_deux = datetime.strptime(prod_initiale, '%d/%m/%Y')
            date_auj = datetime.strptime(date_auj, '%d/%m/%Y')

            if date_auj > prod_deux:
                return(prod_initiale)
            else :
                annee_moins_un = annee_auj - 1 # si la date de production est postérieure à auj, on retire 1 an à la date de prod
                prod_moins_un = newformat + str(annee_moins_un)
                return(prod_moins_un)
        
        except:
            return("MMBE")
    else:
        return("MMBE")
'''
