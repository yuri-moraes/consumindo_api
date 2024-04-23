import requests 

get_github_name = input('Qual o seu usuário no github?\nR: ')

url = f'https://api.github.com/users/{get_github_name}'

response = requests.get(url, timeout=3)
data = response.json()

print("\nGithub profile\n")

if response.status_code == 200:
    print(f'Nome: {data["name"]}')
    print(f'Localização: {data["location"]}')
    print(f'Bios: {data["bio"]}')
    print(f'Seguidores: {data["followers"]}')
    print(f'Seguindo: {data["following"]}')
    
    
else:
    print("Não foi possível acessar a conta.")
