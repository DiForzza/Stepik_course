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

    sorted_list = sorted(all_list, key=lambda d: d['Price'])
    print(sorted_list)

    #df = pd.DataFrame(data=sorted_list, index=[0])
    df = pd.Series({'test': sorted_list})
    df = df.T
    print(df)
    df.to_excel('dict1.xlsx')

get_items()