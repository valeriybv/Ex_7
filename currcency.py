import urllib.request, json

#Преобразует json в словарь, вырезает часть с валютами
def json_to_dict (input_data):
    with urllib.request.urlopen(input_data) as url:
        dict = json.load(url)
        return dict['Valute']

#Возвращает валюту с максимальным Value.
def find_max_value(valutes):
    #max_value = max(d_i['Value'] for d_i in valutes.values())
    max_value = 0
    for k, v in valutes.items():
        if max_value < v['Value']:
            max_value = v['Value']
            v_max = v
    return v_max