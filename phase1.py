"""phase 1 du projet python
analyseur de command eet chercheur d'historique"""

import argparse, requests, json, datetime
from datetime import datetime

def analyser_commande():
    """Génère un interpréteur de commande.

    Returns:
    Namespace: Un objet Namespace tel que retourné par `parser.parse_args()`.
                Cet objet a trois attributs: « idul » représentant l'idul
                du joueur, « parties » qui est un booléen `True`/`False`
                et « local » qui est un booléen `True`/`False`.
    """
    parser = argparse.ArgumentParser(description =
                "Extraction de valeurs historiques pour un ou plusieurs symboles boursiers.")
    parser.add_argument('symbole', nargs='+', help = "Nom d'un symbole boursier")

    parser.add_argument(
        '-d', '--début', dest = 'début', metavar= 'DATE',
        help = 'Date recherchée la plus ancienne (format: AAAA-MM-JJ)')

    parser.add_argument(
        '-f', '--fin', dest = 'fin',metavar='DATE', default= datetime.today().date().strftime("%Y-%m-%d"),
        help = "Date recherchée la plus récente (format: AAAA-MM-JJ)")

    parser.add_argument(
        '-v', '--valeur',
        help = "La valeur désirée (par défaut: fermeture)",
        default= 'fermeture',
        choices=['fermeture', 'ouverture', 'min', 'max', 'volume'])

    return parser.parse_args()

def produire_historique(symbole, date_debut, date_fin, info_demande):
    """Génere un historique selon le symbole et date demandé"""

    url = f'https://pax.ulaval.ca/action/{symbole}/historique/'
    timeline = {"début":date_debut, "fin": date_fin}
    reponse = json.loads(requests.get(url, timeline).text)
    historique = []
    for keys in reponse["historique"]:
        historique.append((datetime.strptime(keys, "%Y-%m-%d").date() ,
                            reponse["historique"][keys][info_demande]))
    print(f'titre={symbole}: valeur={info_demande}, début={datetime.strptime(date_debut, "%Y-%m-%d").date()}, fin={datetime.strptime(date_fin, "%Y-%m-%d").date()}')
    print(historique)
