import matplotlib.pyplot as plt
import gradio as gr

''' fonction de lecture d'un fichier'''
def lire_fichier(file):
    with open(file, 'r') as f: #on ouvre un fichier en mode lecture
        seq = ''
        fasta = f.readline() #si fichier fasta on enleve la première ligne
        ligne = f.readline()
        while ligne != '': #tant qu'il existe des lignes dans le fichier
            seq += ligne.strip().replace(' ', '').upper() #on stocke les lignes en sequence
            ligne = f.readline()
        for nucleotide in seq: #on verifie que chaque lettre de la séquence est un nucléotide d'ADN
            if nucleotide not in 'ATGC':
                print(nucleotide)
                raise ValueError("Le fichier contient des caractères invalides")
    return seq

''' fonction de calcule de ratio'''
def ratios(seq, fen, pas):
    ratios = [] # on crée une liste vide

    for i in range(0, len(seq), pas): 
        fenetre = seq[i:i + min(fen, len(seq) - i)] #creation d'une fenetre en fonction de i
        nbC = fenetre.count('C') #on compte dans la fenêtre de nombre de C
        nbG = fenetre.count('G') #pareil pour G
        total = nbC + nbG #on fait la somme

        if total > 0: #si il en existe on fait un ratio
            ratio = (nbC - nbG) / total
        else:
            ratio = 0 #sinon le ratio est nul
        ratios.extend([ratio] * min(pas, len(seq) - i))

    return ratios

''' fonction de calcule d'inversion'''
def calcul_inv(ratios, len_fen):
    if ratios[0] < 0: #on initialise le point d'inversion
        point_inv = -1
    else:
        point_inv = 1 #on détecte le changement de signe
    for i in range(1, len(ratios)):
        if point_inv == -1:
            if ratios[i] > 0:
                counter = 0 #on verifie dans chaque fenêtre
                for j in range(1,10*len_fen+1, len_fen):
                    if ratios[i+j] > 0:
                        counter += 1
                if counter >= 8: #on retourne l'index d'inversion
                    return i
        else:
            if ratios[i] < 0:
                counter = 0
                for j in range(1,10*len_fen+1, len_fen):
                    if ratios[i+j] < 0:
                        counter += 1
                if counter >= 8:
                    return i

''' fonction fenetre graphique'''
def plot_graph(file):

    sequence = lire_fichier(file.name)
    fenetre = 8000
    pas = 6750
    ratios_GC = ratios(sequence, fenetre, pas)
    point_inv = calcul_inv(ratios_GC, fenetre)
    print(point_inv)

    plt.figure(figsize=(10, 6)) #creation du graphique
    plt.plot(range(len(sequence)), [ratios_GC[i] for i in range(len(sequence))], label='Ratio GC', color='blue')

    plt.scatter(point_inv+(fenetre/2), 0, color='red', s=200, label="Point d'inversion")
    x_labels = [i for i in range(0, len(sequence), len(sequence) // 5)]  # Positions des étiquettes
    x_labels.append(point_inv + (fenetre / 2))  # Ajouter la position du point d'inversion
    x_labels.sort()  # Assurer que les étiquettes sont triées
    plt.xticks(x_labels, [str(label) for label in x_labels], color='black')  # Étiquettes en noir


    plt.xlabel('Position dans la séquence')
    plt.ylabel('Ratio GC')
    plt.title("Représentation du point d'inversion par rapport au ratio GC")
    plt.axvline(point_inv+(fenetre/2), color='r', linestyle='--', label='Premier nucléotide de la fenêtre contenant le point d\'inversion')
    plt.legend()
    plt.savefig('plot.png')
    return 'plot.png'


interface = gr.Interface(fn=plot_graph, inputs="file", outputs="image", title="Recherche du point d'inversion dans une séquence d'ADN")
interface.launch()


# staphylococcus_aureus.fasta
