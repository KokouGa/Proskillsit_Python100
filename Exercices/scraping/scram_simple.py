import csv
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"


def convertir_note(note_texte):
    if note_texte == "One":
        return 1
    elif note_texte == "Two":
        return 2
    elif note_texte == "Three":
        return 3
    elif note_texte == "Four":
        return 4
    elif note_texte == "Five":
        return 5
    else:
        return 0


def lire_page(url):
    reponse = requests.get(url)
    reponse.raise_for_status()
    return BeautifulSoup(reponse.text, "html.parser")


def extraire_livres(soup):
    livres = []
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        titre = article.h3.a["title"]
        lien = article.h3.a["href"]
        prix = article.find("p", class_="price_color").text.strip()
        disponibilite = article.find("p", class_="instock availability").text.strip()

        classes_note = article.find("p", class_="star-rating")["class"]
        note_texte = classes_note[1]
        note = convertir_note(note_texte)

        livres.append([titre, prix, disponibilite, note, lien])

    return livres


def sauvegarder_csv(livres, nom_fichier):
    with open(nom_fichier, "w", newline="", encoding="utf-8") as fichier:
        writer = csv.writer(fichier)
        writer.writerow(["Titre", "Prix", "Disponibilite", "Note", "Lien"])

        for livre in livres:
            writer.writerow(livre)


def main():
    tous_les_livres = []

    for numero_page in range(1, 50):
        url = BASE_URL.format(numero_page)
        print("Lecture de la page :", url)

        soup = lire_page(url)
        livres = extraire_livres(soup)

        for livre in livres:
            tous_les_livres.append(livre)

    print("Nombre total de livres :", len(tous_les_livres))

    for livre in tous_les_livres[:5]:
        print(livre)

    sauvegarder_csv(tous_les_livres, "books.csv")
    print("Fichier books.csv créé avec succès")


if __name__ == "__main__":
    main()