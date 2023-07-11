import currcency
import Rate
from Employee import Employee, Awards
from Designer import Designer


url = "https://www.cbr-xml-daily.ru/daily_json.js"
dict = currcency.json_to_dict(url)
#Задание 1
max_curr = currcency.find_max_value(dict)
print(max_curr['Name'])
#Задание 2
r = Rate.Rate()
print(r.currency_rate(Rate.currcodes.BYN.value, diff_=True))
#Задание 3
p = Designer('Аристарх', [Awards.international, Awards.international], 17)
for i in range (20):
    p.pass_qualification()





