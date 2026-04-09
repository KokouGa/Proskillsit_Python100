import requests

# Inscription
signup_data = {
    "name": "Jean Dupont",
    "email": "jean@example.com",
    "password": "monMotDePasse123"
}
response = requests.post('https://fakeauth.api.demo/signup', json=signup_data)
print(response.json())
# Retourne: {"name": "Jean Dupont", "email": "jean@example.com", "id": "...", "tokenId": "..."}

# Connexion
login_data = {
    "email": "jean@example.com",
    "password": "monMotDePasse123"
}
response = requests.post('https://fakeauth.api.demo/login', json=login_data)
token = response.json()['tokenId']
print(f"Token reçu: {token}")

# Requête authentifiée
headers = {'Authorization': f'tcr {token}'}
response = requests.get('https://fakeauth.api.demo/users', headers=headers)
print(response.json())



