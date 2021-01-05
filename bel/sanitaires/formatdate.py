import datetime
from datetime import datetime

# date_pandas = "05/01/21" (ex : date de chargement ou DLUO)

def format_europeen(date_pandas):
    ma_date = str(date_pandas)
    ma_date = datetime.strptime(ma_date, '%d/%m/%y')
    return ma_date.strftime('%d/%m/%Y')
