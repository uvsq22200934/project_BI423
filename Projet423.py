# staphylococcus_aureus.fasta


import matplotlib.pyplot as plt
import gradio as gr


''' Fonction de lecture d'un fichier'''


def lire_fichier(file):
    with open(file, 'r') as f:  # On ouvre un fichier en mode lecture
        seq = ''  # On crée une variable seq pour stocker la séquence
        fasta = f.readline()  # On enlève la première ligne du fichier qui est au format fasta

        ligne = f.readline()
        while ligne != '':  # Tant qu'il existe des lignes dans le fichier
            seq += ligne.strip().replace(' ', '').upper()  # On stocke les lignes dans la variable seq
            ligne = f.readline()  # On passe à la ligne suivante

        for nucleotide in seq:  # On vérifie que chaque lettre de la séquence est un nucléotide d'ADN
            if nucleotide not in 'ATGC':
                print(nucleotide)
                raise ValueError("Le fichier contient des caractères invalides")  # S'il y a un caractère non compatible, on affiche une erreur

    return seq  # On renvoie la variable seq qui correspond à la séquence d'intérêt sous forme de chaîne de caractères


''' Fonction de calcul de ratio'''


def ratios(seq, fen, pas):
    ratios = []  # On crée une liste vide pour stocker tous les ratios

    for i in range(0, len(seq), pas):  # On parcourt la séquence entière en avançant par pas
        fenetre = seq[i:i + min(fen, len(seq) - i)]  # On ajuste la fenêtre avec la plus petite valeur entre la fenêtre donnée et la longueur de séquence qu'il reste à parcourir
        nbC = fenetre.count('C')  # On compte dans la fenêtre de nombre de C
        nbG = fenetre.count('G')  # Pareil pour G
        total = nbC + nbG  # On fait la somme des deux

        if total > 0:  # S'il en existe, on calcul le ratio
            ratio = (nbC - nbG) / total
        else:
            ratio = 0  # Sinon le ratio est nul
        ratios.extend([ratio] * min(pas, len(seq) - i))  # On ajoute pour toutes les positions de la fenêtre la valeur du ratio

    return ratios  # On renvoie la liste des ratios qui contient un ratio pour chaque position de la séquence


''' Fonction de calcule d'inversion'''


def calcul_inv(ratios, len_fen):
    if ratios[0] < 0:  # On attribue une valeur de -1 si le premier ratio est négatif ou de 1 s'il est positif
        valeur = -1
    else:
        valeur = 1

    for i in range(1, len(ratios)):  # On parcourt la liste des ratios
        if valeur == -1:  # Si on a la valeur de -1 (ratio négatif)
            if ratios[i] > 0:
                cpt = 0
                for j in range(1, 10*len_fen+1, len_fen):
                    if ratios[i+j] > 0:  # On regarde si les ratios des 10 fenêtres suivants sont positifs
                        cpt += 1  # Si oui, on ajoute 1 au compteur
                if cpt >= 8:  # Si on a le compteur à au moins 8
                    return i  # On renvoie la position du point d'inversion
        else:  # Si on avait une valeur de 1 (ratio positif)
            if ratios[i] < 0:
                cpt = 0
                for j in range(1, 10*len_fen+1, len_fen):
                    if ratios[i+j] < 0:  # On regarde si les ratios suivants sont négatifs
                        cpt += 1
                if cpt >= 8:
                    return i


''' Fonction tracé graphique'''


def plot_graph(file):

    sequence = lire_fichier(file.name)  # On récupère la séquence dans la variable sequence
    fenetre = 8000  # On choisit une fenêtre de 8000 qui fonctionne le mieux pour les organismes dans l'ordre de grandeur de 10^6 bp comme notre organisme d'intérêt
    pas = 6750  # On choisit un pas un peu plus petit que la fenêtre
    ratios_GC = ratios(sequence, fenetre, pas)  # On récupère la liste des ratios calculés sur notre séquence avec notre fenêtre et notre pas
    point_inv = calcul_inv(ratios_GC, fenetre)  # On passe le tout dans la fonction de calcul dub point d'inversion

    plt.figure(figsize=(10, 6))  # Creation du graphique
    plt.plot(range(len(sequence)), [ratios_GC[i] for i in range(len(sequence))], label='Ratio GC', color='blue')  # On crée chaque point avec pour abscisse la position dans la séqence et comme ordonnée le ratio associé à cette position
    plt.scatter(point_inv+(fenetre/2), 0, color='red', s=200, label="Point d'inversion")  # On crée en rouge le point d'inversion pour faciliter la visualisation
    x_labels = [i for i in range(0, len(sequence), len(sequence) // 5)]  # On ajoute des positions dans la séquence pour l'axe des abscisses
    x_labels.append(int(point_inv + (fenetre / 2)))  # On ajoute la position du point d'inversion
    x_labels.sort()  # On remet les étiquettes dans l'ordre
    plt.xticks(x_labels, [str(label) for label in x_labels], color='black')  # On crée les étiquettes de l'axe des abscisses
    plt.xlabel('Position dans la séquence')
    plt.ylabel('Ratio GC')
    plt.title("Représentation du point d'inversion par rapport au ratio GC")
    plt.axvline(point_inv+(fenetre/2), color='r', linestyle='--', label='Premier nucléotide de la fenêtre contenant le point d\'inversion')  # On crée une ligne rouge qui coupe l'axe des abscisses à la position du point d'inversion
    plt.legend()
    plt.savefig('plot.png')  # On enregistre l'image du graphique

    return 'plot.png'


interface = gr.Interface(fn=plot_graph, inputs="file", outputs="image", title="Recherche du point d'inversion dans une séquence d'ADN")  # On crée une interface graphique sur gradio qui prend en entrée un fichier et donne en sortie une image qui est le graphique
interface.launch()  # On lance l'interface
