code_erreurs = [404, 500]

def lire_fichier_log(le_fichier_log):

    logs = []

    try:
        with open(le_fichier_log, "r", encoding="utf-8") as fichier:
            for ligne in fichier:
                ligne = ligne.strip()
                donnees = ligne.split("|")

                if len(donnees) != 6:
                    print(f"Format de ligne incorrect: {ligne}")
                    continue
                else:
                    try:
                        date = donnees[0].strip()
                        adresse_ip = donnees[1].strip()
                        methode = donnees[2].strip()
                        url = donnees[3].strip()
                        code = int(donnees[4].strip())
                        temps = int(donnees[5].strip().replace("ms", ""))

                        donnees_log = {
                            "date": date,
                            "ip": adresse_ip,
                            "methode": methode,
                            "code": code,
                            "temps": temps,
                            "url": url
                        }

                        logs.append(donnees_log)

                    except ValueError:
                        print("La valeur est incorrecte sur une ligne")

                    except:
                        print("klk chose s est dans fichier")

    except FileNotFoundError:
        print("Fichier non trouve")

    return logs




def affiche_stat(logs):

    requests_total = len(logs)
    nombres_get = 0
    nombres_post = 0
    nombres_erreurs = 0
    somme_tps = 0
    moyen_temps = 0

    for log in logs:
        if log["methode"] == "GET":
            nombres_get += 1
        elif log["methode"] == "POST":
            nombres_post += 1

        if log["code"] in code_erreurs:
            nombres_erreurs += 1

        somme_tps += log["temps"]

    if requests_total > 0:
        moyen_temps = somme_tps / requests_total

    statistique = f"\nStatistique\nNombres de total de requetes : {requests_total}\n\
Nombre de requeste GET : {nombres_get}, Nombre de requeste POST : {nombres_post}\n\
Nombre d erreurs : {nombres_erreurs}\nTemps moyen : {moyen_temps:.2f} ms"

    print(statistique)



def securite_analyse(logs):
    ip_suspecte_trouve = False
    erreur_ip = {}
    tentatives_connexion = 0

    for log in logs:
        if log["code"] in code_erreurs:
            adresse_ip = log["ip"]
            erreur_ip[adresse_ip] = erreur_ip.get(adresse_ip, 0) + 1

        if log["methode"] == "POST" and log["url"] == "/login":
            tentatives_connexion += 1

    print("\nAnalyse de securite")

    for ip, nombre_essaie in erreur_ip.items():
        if nombre_essaie >= 2:
            print(f"{ip} est suspecte")
            ip_suspecte_trouve = True

    if not ip_suspecte_trouve:
        print("Aucun IP suspecte")

    print(f"Nombre de tentatives de connexion : {tentatives_connexion}")

    return tentatives_connexion




def analyse_avancee(logs):
    compteur_url = {}
    requeste_plus_lente = None

    if len(logs) == 0:
        print("Aucune donnee valide a analyser")
        return None, None

    for log in logs:
        url = log["url"]
        compteur_url[url] = compteur_url.get(url, 0) + 1

        if requeste_plus_lente is None or log["temps"] > requeste_plus_lente["temps"]:
            requeste_plus_lente = log

    lien = None
    value = 0

    for url, nb in compteur_url.items():
        if nb > value:
            value = nb
            lien = url

    print(f"Le url plus demande est : {lien}")
    print(f"La requeste la plus lente est faite au {requeste_plus_lente['date']} sur url {requeste_plus_lente['url']}")

    return lien, requeste_plus_lente




def generer_rapport(logs):

    requests_total = len(logs)
    nombres_get = 0
    nombres_post = 0
    nombres_erreurs = 0
    somme_tps = 0
    moyen_temps = 0

    erreur_ip = {}
    tentatives_connexion = 0
    ip_suspectes = []

    compteur_url = {}
    requeste_plus_lente = None
    lien_plus_demande = None

    if len(logs) == 0:
        print("Aucune donnee a mettre dans le rapport")
        return

    for log in logs:
        if log["methode"] == "GET":
            nombres_get += 1
        elif log["methode"] == "POST":
            nombres_post += 1

        if log["code"] in code_erreurs:
            nombres_erreurs += 1
            adresse_ip = log["ip"]
            erreur_ip[adresse_ip] = erreur_ip.get(adresse_ip, 0) + 1

        if log["methode"] == "POST" and log["url"] == "/login":
            tentatives_connexion += 1

        somme_tps += log["temps"]

        url = log["url"]
        compteur_url[url] = compteur_url.get(url, 0) + 1

        if requeste_plus_lente is None or log["temps"] > requeste_plus_lente["temps"]:
            requeste_plus_lente = log

    if requests_total > 0:
        moyen_temps = somme_tps / requests_total

    for ip, nombre_essaie in erreur_ip.items():
        if nombre_essaie >= 2:
            ip_suspectes.append(ip)

    lien = None
    value = 0
    for url, nb in compteur_url.items():
        if nb > value:
            value = nb
            lien = url

    lien_plus_demande = lien

    with open("rapport.txt", "w", encoding="utf-8") as fichier:
        fichier.write("Rapport d analyse des logs\n")
        fichier.write("==========================\n\n")

        fichier.write("Statistique\n")
        fichier.write(f"Nombres de total de requetes : {requests_total}\n")
        fichier.write(f"Nombre de requeste GET : {nombres_get}\n")
        fichier.write(f"Nombre de requeste POST : {nombres_post}\n")
        fichier.write(f"Nombre d erreurs : {nombres_erreurs}\n")
        fichier.write(f"Temps moyen : {moyen_temps:.2f} ms\n\n")

        fichier.write("Analyse de securite\n")
        if len(ip_suspectes) > 0:
            for ip in ip_suspectes:
                fichier.write(f"{ip} est suspecte\n")
        else:
            fichier.write("Aucun IP suspecte\n")

        fichier.write(f"Nombre de tentatives de connexion : {tentatives_connexion}\n\n")

        fichier.write("Analyse avancee\n")
        fichier.write(f"Le url plus demande est : {lien_plus_demande}\n")

        if requeste_plus_lente is not None:
            fichier.write(f"La requeste la plus lente est faite au {requeste_plus_lente['date']} sur url {requeste_plus_lente['url']}\n")

    print("Rapport genere dans rapport.txt")




def main():

    les_donnees = lire_fichier_log("logs.txt")

    if len(les_donnees) == 0:
        print("Aucune donnee chargee. Fin du programme.")
        exit()

    while True:
        print("\n\tListe des choix 1 a 5")
        print("\t1. Statistiques")
        print("\t2. Analyse de sécurité")
        print("\t3. Analyse avancée")
        print("\t4. Génération de rapport")
        print("\t5. Quitter\n")

        choix = input("\tFait ton choix : ")

        if choix == "1":
            affiche_stat(les_donnees)
        elif choix == "2":
            securite_analyse(les_donnees)
        elif choix == "3":
            analyse_avancee(les_donnees)
        elif choix == "4":
            generer_rapport(les_donnees)
        elif choix == "5":
            print("\tFin et merci...")
            exit()
        else:
            print("\tChoix invalide et choisir entre 1 et 5")



if __name__ == '__main__':
    main()