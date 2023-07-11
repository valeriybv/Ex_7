import requests
from enum import Enum


#Я решл вместо 100 копипастных методов сделать одно перечисление с указанием кода валюты.
# Соответственно, метод по расчету курса принимает в кач-ве параметра код из этого перечисления
# Тогда, в случае изменения логики выполнения метода нужно будет изменить только один метод
# В случае изменения набора валют, мы не будем лезть в методы класса, а работать только со словарем
class currcodes(Enum):
    AUD = 'AUD'
    AZN = 'AZN'
    GBP = 'GBP'
    AMD = 'AMD'
    BYN = 'BYN'
    BGN = 'BGN'
    BRL = 'BRL'
    HUF = 'HUF'
    VND = 'VND'
    HKD = 'HKD'
    GEL = 'GEL'
    DKK = 'DKK'
    AED = 'AED'
    USD = 'USD'
    EUR = 'EUR'
    EGP = 'EGP'
    INR = 'INR'
    IDR = 'IDR'
    KZT = 'KZT'
    CAD = 'CAD'
    QAR = 'QAR'


class Rate(object):
    def __init__(self, format_ = 'value'):
        self.format = format_

    @staticmethod
    def exchange_rates():
        rate = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        return rate.json()['Valute']

    def make_format(self, currency, diff_):
        response = self.exchange_rates()
        if currency in response:
            if self.format == 'full':
                return response[currency]

            if self.format == 'value':
                #Для задания 2 - если  diff_ = True, вычисляем разницу.
                if diff_ == True:
                    diff = round(response[currency]['Value'] - response[currency]['Previous'], 2)
                    return diff
                else:
                    return response[currency]['Value']

    def currency_rate(self, currency_, diff_):
        '''
        :param currency_:
        принимает код валюты из перечисления в виде currcodes.<name>.value
        :return:
        возвращает курс указанной валюты
        '''
        return Rate.make_format(self, currency_, diff_)

