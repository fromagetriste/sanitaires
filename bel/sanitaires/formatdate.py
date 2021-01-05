import datetime
from datetime import datetime


# sert à changer les 05/01/21 en 05/01/2021 pour la date chargement et la DLUO
# date_pandas = "05/01/21" (ex : date de chargement ou DLUO)

def format_europeen(date_pandas):
    try:
        ma_date = str(date_pandas)
        ma_date = datetime.strptime(ma_date, '%d/%m/%y')
        return ma_date.strftime('%d/%m/%Y')
    except:
        pass
