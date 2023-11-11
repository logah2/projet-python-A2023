"""ce programme permet de faire fonctionner le projet 1"""

from phase1 import analyser_commande, produire_historique

if __name__ == "__main__":
    args = analyser_commande()
    for symbole in args.symbole:
        if args.début is None:
            produire_historique(symbole, args.fin, args.fin, args.valeur)

        else:
            produire_historique(symbole, args.début, args.fin, args.valeur)
