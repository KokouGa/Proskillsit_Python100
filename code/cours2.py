import requests


url = "https://jsonplaceholder.typicode.com/users/"

response = requests.get(url)
donnees = response.json()
print("=" * 40)
print(donnees)
print("=" * 40)

print(len(donnees))


"""print(f"keys: {donnees.keys()}")
print("=" * 40)
print(f"values: {donnees.values() }")
print("=" * 40)
print(f"items: {donnees.items() }")
"""
print(donnees[0])
print("\n----------\n")
for user in donnees:
    print(f"Name: {user['name']}, Email: {user['email']}")
    
print("\n----------\n")

print(donnees[0:2])