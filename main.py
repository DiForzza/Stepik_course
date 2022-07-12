import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_items():
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
    df.to_excel('dict1.xlsx')


get_items()

# list_id = []
# list_vendor = []
# list_name = []
# list_count = []
# list_price = []
# example = [{'id': 3177, 'Vendor': 'X', 'Name': 'BYS BRAS NEW', 'Count': 1, 'Price': 7000000},
#            {'id': 3422, 'Vendor': 'ZzZ', 'Name': 'Magic Apron of Carpenter crafted by HapkoMaH', 'Count': 1,
#             'Price': 7500000},
#            {'id': 2500, 'Vendor': 'RAR', 'Name': 'Rename tools', 'Count': 1, 'Price': 7777777},
#            {'id': 1890, 'Vendor': 'Moscow', 'Name': 'Unicorn', 'Count': 1, 'Price': 9000000},
#            {'id': 1193, 'Vendor': 'God', 'Name': 'Nightmare', 'Count': 1, 'Price': 9999991},
#            {'id': 2139, 'Vendor': 'OrDa', 'Name': 'BUS 37Hp BRAS 42Hp', 'Count': 1, 'Price': 10000000},
#            {'id': 3217, 'Vendor': 'XCV', 'Name': 'Genie', 'Count': 1, 'Price': 10000000},
#            {'id': 3155, 'Vendor': 'War', 'Name': 'Light Wood Crossbow ( Aucion 2021)', 'Count': 1, 'Price': 12000000},
#            {'id': 1215, 'Vendor': 'God', 'Name': '100 Meteorite Ingot', 'Count': 1, 'Price': 13000000},
#            {'id': 1216, 'Vendor': 'God', 'Name': '100 Meteorite Ingot', 'Count': 1, 'Price': 13000000}]
#
#
#
