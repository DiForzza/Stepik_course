import openpyxl
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from openpyxl import load_workbook


def get_items():
    try:
        wb = load_workbook('FWUO.xlsx')
        ws = wb.active
        if ws['Z1'].value != int(datetime.now().strftime('%H')):
            url = 'https://www.fwuo.ru/vendors/?query=*&vendor=all'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            results = soup.find_all('td')
            results.pop(0)
            results.pop(0)
            results.pop(0)
            results.pop(0)
            count = 0
            counter = 1
            id = 0
            trade_list = ()
            all_list = list()
            for result in results:
                if count == 0:
                    trade_list = {'id': int(id), 'Vendor': result.text}
                if count == 1:
                    trade_list['Name'] = result.text
                if count == 2:
                    trade_list['Count'] = int(result.text)
                if count == 3:
                    trade_list['Price'] = int(result.text)
                    count = -1
                id += 0.25
                count += 1
                counter += 1
                if counter == 4:
                    all_list.append(trade_list)
                    counter = 0
            list_id = []
            list_vendor = []
            list_name = []
            list_count = []
            list_price = []
            sorted_list = sorted(all_list, key=lambda d: d['Price'])
            for i in range(0, len(sorted_list)):
                list_id.append(sorted_list[i].get('id'))
                list_vendor.append(sorted_list[i].get('Vendor'))
                list_name.append(sorted_list[i].get('Name'))
                list_count.append(sorted_list[i].get('Count'))
                list_price.append(sorted_list[i].get('Price'))
            data = {'list_id': list_id, 'list_vendor': list_vendor, 'list_name': list_name, 'list_count': list_count,
                    'list_price': list_price}
            df = pd.DataFrame(data)
            df.to_excel('FWUO.xlsx')

            wb = load_workbook('FWUO.xlsx')
            ws = wb.active
            ws.insert_rows(0, 1)
            ws['A1'] = datetime.now().strftime('%d/%m/%y %H:%M')
            ws['Z1'] = int(datetime.now().strftime('%H'))
            wb.save('FWUO.xlsx')
            print('Данные успешно обновлены.')
        else:
            print('Обновлять можно раз в час.')
    except IOError:
        filepath = 'FWUO.xlsx'
        wb = openpyxl.Workbook()
        wb.save(filepath)
        print('Пустой файл создан. Запустите программу еще раз.')


get_items()