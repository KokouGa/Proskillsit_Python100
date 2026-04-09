import requests
from requests.exceptions import ConnectionError, Timeout, RequestException

def inscription():
    signup_data = {
        "name": "Jean Dupont",
        "email": "jean@example.com",
        "password": "monMotDePasse123"
    }
    
    try:
        response = requests.post('https://fakeauth.api.demo/signup', 
                                json=signup_data, 
                                timeout=5)
        print(response.json())
        
    except ConnectionError:
        print("Erreur: Impossible de se connecter au serveur.")
        print("Verifiez que l'API existe et que vous avez une connexion internet.")
        
    except Timeout:
        print("Erreur: La requete a expire (plus de 5 secondes).")
        
    except RequestException as e:
        print(f"Erreur lors de la requete: {e}")
        
    except Exception as e:
        print(f"Erreur inattendue: {e}")

def connexion():
    login_data = {
        "email": "jean@example.com",
        "password": "monMotDePasse123"
    }
    
    try:
        response = requests.post('https://fakeauth.api.demo/login', 
                                json=login_data, 
                                timeout=5)
        
        if response.status_code == 200:
            token = response.json()['tokenId']
            print(f"Token recu: {token}")
            return token
        else:
            print(f"Erreur HTTP: {response.status_code}")
            return None
            
    except ConnectionError:
        print("Erreur: Serveur injoignable. L'API fakeauth.api.demo n'existe pas.")
        return None
        
    except Timeout:
        print("Erreur: La requete a expire")
        return None
        
    except RequestException as e:
        print(f"Erreur: {e}")
        return None

if __name__ == "__main__":
    print("Test avec une API qui n'existe pas:")
    inscription()
    
    print("\nTest de connexion:")
    connexion()