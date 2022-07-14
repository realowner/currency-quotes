import csv


def quotes_csv(data):
    list_data = [
        ['Код', 'Название', 'Цена', 'Дата катировки', 'Номинал']
    ]
    
    for row in data:
        new_list = [row[1], row[2], str(row[3]), str(row[4]), str(row[5])]
        list_data.append(new_list)
        
    with open('exportfiles/curr_quotes.csv', 'w', encoding='cp1251') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerows(list_data)