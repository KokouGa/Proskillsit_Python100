import requests

def tester_basic_auth():
    """
    Teste l'authentification Basic Auth avec HTTPBin.
    URL attendue : https://httpbin.org/basic-auth/user/passwd
    Identifiants attendus : username = user, password = passwd
    """
    url = "https://httpbin.org/basic-auth/user/passwd"
    username = "user"
    password = "passwd"

    try:
        response = requests.get(url, auth=(username, password), timeout=10)

        print("\n===== TEST BASIC AUTH =====")
        print(f"Code HTTP : {response.status_code}")

        if response.status_code == 200:
            print("Authentification reussie.")
            print("Reponse JSON :")
            print(response.json())
        else:
            print("Echec de l'authentification.")

    except requests.exceptions.RequestException as e:
        print("\nErreur lors du test Basic Auth :")
        print(e)


def tester_basic_auth_invalide():
    """
    Teste Basic Auth avec un mauvais mot de passe.
    """
    url = "https://httpbin.org/basic-auth/user/passwd"
    username = "user"
    password = "mauvais_mot_de_passe"

    try:
        response = requests.get(url, auth=(username, password), timeout=10)

        print("\n===== TEST BASIC AUTH INVALIDE =====")
        print(f"Code HTTP : {response.status_code}")

        if response.status_code == 200:
            print("Authentification reussie (comportement inattendu).")
        else:
            print("Authentification refusee (comportement normal).")

    except requests.exceptions.RequestException as e:
        print("\nErreur lors du test Basic Auth invalide :")
        print(e)


def tester_bearer_token():
    """
    Teste l'authentification Bearer Token avec HTTPBin.
    """
    url = "https://httpbin.org/bearer"
    token = "mon_token_123"

    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        print("\n===== TEST BEARER TOKEN =====")
        print(f"Code HTTP : {response.status_code}")

        if response.status_code == 200:
            print("Token accepte.")
            print("Reponse JSON :")
            print(response.json())
        else:
            print("Token refuse.")

    except requests.exceptions.RequestException as e:
        print("\nErreur lors du test Bearer Token :")
        print(e)


def tester_bearer_sans_token():
    """
    Teste l'acces a l'endpoint Bearer sans envoyer de token.
    """
    url = "https://httpbin.org/bearer"

    try:
        response = requests.get(url, timeout=10)

        print("\n===== TEST BEARER SANS TOKEN =====")
        print(f"Code HTTP : {response.status_code}")

        if response.status_code == 200:
            print("Acces autorise (comportement inattendu).")
        else:
            print("Acces refuse (comportement normal).")

    except requests.exceptions.RequestException as e:
        print("\nErreur lors du test Bearer sans token :")
        print(e)


def main():
    print("Demonstration HTTPBin : Basic Auth et Bearer Token")
    tester_basic_auth()
    tester_basic_auth_invalide()
    tester_bearer_token()
    tester_bearer_sans_token()


if __name__ == "__main__":
    main()