import pandas


def quotes_xlsx(data):
    dict_data = {
        'Код': [],
        'Название': [],
        'Цена': [],
        'Дата катировки': [], 
        'Номинал': []
    }
    
    for row in data:
        dict_data['Код'].append(row[1])
        dict_data['Название'].append(row[2])
        dict_data['Цена'].append(row[3])
        dict_data['Дата катировки'].append(row[4])
        dict_data['Номинал'].append(row[5])
        
    data_frame = pandas.DataFrame(dict_data)
    
    data_frame.to_excel('exportfiles/curr_quotes.xlsx')