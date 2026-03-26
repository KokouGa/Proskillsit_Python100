code_erreurs = [404, 500]

def lire_fichier_log(le_fichier_log):

    logs = []

    with open(le_fichier_log, "r", encoding="utf-8") as fichier:
        for ligne in fichier:
            ligne = ligne.strip()
            donnees = ligne.split("|")

            if len(donnees) != 6:
                print(f"Format de ligne incorrect: {ligne}")
                continue
            else:
                date = donnees[0].strip()
                adresse_ip = donnees[1].strip()
                methode = donnees[2].strip()
                url = donnees[3].strip()
                code = int(donnees[4].strip())
                temps = int(donnees[5].strip().replace("ms", ""))
                #print(temps)

                donnees_log = {
                     "date": date,
                     "ip" : adresse_ip,
                     "methode": methode,
                     "code": code,
                     "temps": temps,
                     "url" : url
                 }

                logs.append(donnees_log)

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
        #if log.get("method") == "GET":
            nombres_get += 1
        elif log["methode"] == "POST":
            nombres_post += 1

        if log["code"] in code_erreurs:
            nombres_erreurs += 1

        somme_tps += log["temps"]


    
    if requests_total > 0 :
        moyen_temps = somme_tps / requests_total


    statistique = f"\n Statistique\n Nombres de total de requetes : {requests_total}\n\
    Nombre de requeste GET : {nombres_get}, Nombre de requeste POST : {nombres_post}" 

    
    print(statistique)



#n dict() .get() et []

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


    for ip, nombre_essaie in erreur_ip.items():
        #print(ip, nombre_essaie)
        if nombre_essaie >= 2:
            print(f"{ip} est suspecte")
            ip_suspecte_trouve = True

    if not ip_suspecte_trouve:
        print("Aucun IP suspecte")

    return tentatives_connexion


    

def analyse_avancee(logs):
    compteur_url = {}
    requeste_plus_lente = None


    for log in logs:
        url = log["url"]
        compteur_url[url] = compteur_url.get(url, 0) + 1

    #diction = {1:3, 6:1, 3:6}
    




    lien_plus_demande = max(compteur_url, key=compteur_url.get)


    lien = None 
    value = 0 
    for url, nb in compteur_url.items():
        if nb > value:
            value = nb 
            lien = url


    print(lien, value)



    return  lien_plus_demande



    pass

def main():
    les_donnees = lire_fichier_log("logs.txt")
    affiche_stat(les_donnees)

    tentatives_connexions = securite_analyse(les_donnees)
    compteur_lien = analyse_avancee(les_donnees)
    print(compteur_lien)
    print(tentatives_connexions)


main()



def ma_fonction(a, b, r=0):
    pass


ma_fonction(4, 5,6)