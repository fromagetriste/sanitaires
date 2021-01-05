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
            quantieme = str(lot[2:-2]) # on isole 294
            annee_auj = str(datetime.now().year) # = 2021
            quantieme_et_annee_auj = quantieme + "/" + annee_auj   # on obtient "294/2021"
            lot_un = datetime.strptime(quantieme_et_annee_auj, '%j/%Y') #%j = day of the year
            
            if date_auj > lot_un:
                return lot_un.strftime('%d/%m/%Y') # on recrée en objet date avec le format voulu
                
            else: # pour les dates de prod postérieures à la dates du jour
                annee_auj_moins_un = int(annee_auj) - 1
                quantieme_et_annee_moins_un = quantieme + "/" + str(annee_auj_moins_un)
                lot_deux = datetime.strptime(quantieme_et_annee_moins_un, '%j/%Y')
                return lot_deux.strftime('%d/%m/%Y')   

        except:
            return("MMBE")
            
    else:
        return("MMBE")

