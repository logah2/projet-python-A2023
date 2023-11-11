# projet-python-A2023
Le code de la phase 1 du projet du cours GLO-1901 de la session A2023

Il y a 2 module:
-projet1.py
  - Sert à faire marcher le programme
    
-phase1.py
  - Contient le code de la phase 1. Le code possède 2 fonction analyser_commande et produire_historique.

Le programme fonction en appelant une commande dans le terminal. Cette commande à sa forme la plus simple prend cette écriture:
"python3 projet1.py goog" ou celle-ci avec plus d'info donnée "python3 projet1.py -d=2020-06-23 -f=2021-06-23 -v=volume aapl"

Le symbole d'action est obligatoire pour faire fonctionner le programme, mais il peux y en avoir plusieurs pour aller chercher les infos de plusieurs compagnies en même temps.
Les acronymes des compagnies suivantes sont acceptés:

  -A – Agilent Technologies
  -AAPL – Apple
  -C – Citigroup
  -GOOG – Alphabet (parent company of Google)
  -HOG – Harley-Davidson
  -HPQ - Hewlett-Packard
  -INTC – Intel
  -IBM – International Business Machines
  -LUV - Southwest Airlines (after their main hub at Love Field)
  -MMM – 3M (originally known as Minnesota Mining and Manufacturing)
  -MSFT – Microsoft
  -T - AT&T
  -TGT – Target Corporation
  -TXN – Texas Instruments
  -XOM - ExxonMobil
  -WMT – Walmart
  -

  D'autres informations optionnelles peuvent aussi être entré:
  -Une date de début (date la plus ancienne) qui prend la forme "%Y-%m-%d" par exemple "2020-06-23" / Si aucune n'est donné seul la date de fin sera pris en compte
  -Une date de fin (date la plus récente) qui prend la forme "%Y-%m-%d" par exemple "2021-06-23" / Si aucune n'est donné seul la date d'aujourd'hui sera pris en compte
  -Un type d'information pour les periodes demandée parmis les suivant / si aucune n'est donnée la valeur "fermeture" sera utilisée: 
    - "fermeture" : montant de l'action à la fermeture de la bourse
    - "ouverture" : montant de l'action à l'ouverture de la bourse
    _ "min" : Montant minimal de l'action 
    - "max" : Montant maximal de l'action dans la journée
    - "volume" : volume d'action dans la journée
    


    



  
