import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com/"
START_URL = "https://books.toscrape.com/catalogue/page-1.html"


def rating_to_number(rating_class: str) -> int:
    """Convertit la note textuelle en entier."""
    ratings = {
        "One": 1,
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5
    }
    return ratings.get(rating_class, 0)


def get_soup(url: str) -> BeautifulSoup:
    """Télécharge une page et retourne un objet BeautifulSoup."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return BeautifulSoup(response.text, "html.parser")


def extract_books_from_page(soup: BeautifulSoup) -> list[dict]:
    """Extrait les informations des livres d'une page."""
    books = []
    articles = soup.find_all("article", class_="product_pod")

    for article in articles:
        h3 = article.find("h3")
        a_tag = h3.find("a") if h3 else None

        title = a_tag["title"].strip() if a_tag and a_tag.has_attr("title") else "Titre inconnu"
        relative_link = a_tag["href"] if a_tag and a_tag.has_attr("href") else ""
        book_link = urljoin(BASE_URL + "catalogue/", relative_link)

        price_tag = article.find("p", class_="price_color")
        price = price_tag.get_text(strip=True) if price_tag else "Prix inconnu"

        availability_tag = article.find("p", class_="instock availability")
        availability = availability_tag.get_text(strip=True) if availability_tag else "Disponibilité inconnue"

        rating_tag = article.find("p", class_="star-rating")
        rating_class = ""
        if rating_tag:
            classes = rating_tag.get("class", [])
            if len(classes) > 1:
                rating_class = classes[1]
        rating = rating_to_number(rating_class)

        books.append({
            "title": title,
            "price": price,
            "availability": availability,
            "rating": rating,
            "link": book_link
        })

    return books


def scrape_books(max_pages: int = 5) -> list[dict]:
    """
    Scrape plusieurs pages du site.
    max_pages=5 veut dire qu'on prend les 5 premières pages.
    """
    all_books = []

    for page_num in range(1, max_pages + 1):
        url = f"https://books.toscrape.com/catalogue/page-{page_num}.html"
        print(f"Scraping : {url}")

        try:
            soup = get_soup(url)
            books = extract_books_from_page(soup)
            all_books.extend(books)
        except requests.RequestException as e:
            print(f"Erreur lors de la récupération de la page {page_num} : {e}")

    return all_books


def save_to_csv(data: list[dict], filename: str = "books.csv") -> None:
    """Sauvegarde les données dans un fichier CSV."""
    if not data:
        print("Aucune donnée à enregistrer.")
        return

    fieldnames = ["title", "price", "availability", "rating", "link"]

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Données enregistrées dans {filename}")


def main() -> None:
    books = scrape_books(max_pages=5)
    print(f"Nombre total de livres récupérés : {len(books)}")

    for book in books[:5]:
        print(book)

    save_to_csv(books)


if __name__ == "__main__":
    main()