import requests

try:
    response = requests.get('https://jsonplaceholder.typicode.com/users', timeout=10)
    response.raise_for_status()
    
    users = response.json()
    
    print(f"Succes. Code : {response.status_code}")
    print(f"Total : {len(users)} utilisateurs\n")
    
    for user in users[:3]:
        print(f"Nom: {user['name']} (@{user['username']})")
        print(f"Email: {user['email']}")
        print(f"Ville: {user['address']['city']}")
        print()

except requests.exceptions.Timeout:
    print("Erreur : La requete a expire")
except requests.exceptions.ConnectionError:
    print("Erreur : Probleme de connexion")
except requests.exceptions.HTTPError as e:
    print(f"Erreur HTTP : {e}")
except Exception as e:
    print(f"Erreur : {e}")