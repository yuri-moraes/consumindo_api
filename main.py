import requests 
import json

url = 'https://teste-2aa7c-default-rtdb.firebaseio.com/.json'

response = requests.get(url)
data = response.json()

with open('Python3_Udemy/awesome_api/data.json','w') as file:
    json.dump(data, file, indent=4)

def get_extremes(data,key):
    maximum = max(data, key=lambda x:x[key])
    minimum = min(data,key=lambda x:x[key])
    return maximum, minimum

highest_salary, minimum_salary = get_extremes(data, 'salary')
highest_time, minimum_time = get_extremes(data, 'admission')

print(f'Empregado com o maior salário: {highest_salary["name"]} | Salário: R${highest_salary["salary"]}')
print(f'Empregado com o menor salário: {minimum_salary["name"]} | Salário: R${minimum_salary["salary"]}')
print(f'Empregado com o maior tempo de casa: {highest_time["name"]} | Admissão: R${highest_time["admission"]}')
print(f'Empregado com o menor tempo de casa: {minimum_time["name"]} | Admissão: R${minimum_time["admission"]}')

