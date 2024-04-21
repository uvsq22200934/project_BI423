import matplotlib.pyplot as plt
import gradio as gr


def lire_fichier(file):
    with open(file, 'r') as f:
        seq = ''
        fasta = f.readline()
        ligne = f.readline()
        while ligne != '':
            seq += ligne.strip().replace(' ', '').upper()
            ligne = f.readline()
        for nucleotide in seq:
            if nucleotide not in 'ATGC':
                print(nucleotide)
                raise ValueError("Le fichier contient des caractères invalides")
    return seq


def point_inversion(seq, fen, pas):
    ratios = []
    pts_inv = []

    for i in range(0, len(seq), pas):
        fenetre = seq[i:i + min(fen, len(seq) - i)]
        nbC = fenetre.count('C')
        nbG = fenetre.count('G')
        total = nbC + nbG

        if total > 0:
            ratio = (nbC - nbG) / total
        else:
            ratio = 0
        ratios.extend([ratio] * min(pas, len(seq) - i))

    i = 0
    while i < len(seq) - 1:
        pas = min(pas, len(seq) - i - 1)
        if (ratios[i] < 0 and ratios[i + pas] > 0) or (ratios[i] > 0 and ratios[i + pas] < 0):
            pts_inv.append((i + pas // 2, abs(ratios[i] - ratios[i + pas])))
        i += pas

    return pts_inv, ratios


def plot_graph(file):
    sequence = lire_fichier(file.name)
    fenetre = 8000
    points_inv, ratios_GC = point_inversion(sequence, fenetre, fenetre // 2 + fenetre // 3)
    position = max(points_inv, key=lambda x: x[1])[0]
    print(position)

    plt.figure(figsize=(10, 6))
    plt.plot(range(len(sequence)), [ratios_GC[i] for i in range(len(sequence))], label='Ratio GC', color='blue')
    plt.scatter(position, 0, color='red', s=200, label="Point d'inversion")
    plt.xlabel('Position dans la séquence')
    plt.ylabel('Ratio GC')
    plt.title("Représentation du point d'inversion par rapport au ratio GC")
    plt.legend()
    plt.savefig('plot.png')
    return 'plot.png'


interface = gr.Interface(fn=plot_graph, inputs="file", outputs="image", title="Recherche du point d'inversion dans une séquence d'ADN")
interface.launch()


# staphylococcus_aureus.fasta
