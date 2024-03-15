# project_BI423
Projet BI 423 - Analyse des génomes

Sujet N°1 
Prédiction d’une origine de réplication chez bactérie (recherche de "point de rebroussement" ou « point d’inversion ») 

Faire une interface graphique pour présenter les résultats. Le rapport présentera :  
une explication générale du sujet (question biologique 1 à 2 pages), 
du programme python (décrit en détail) 
et le résultat d’une application sur un plasmide bactérien

1. Première partie :
Faire 1 à 2 pages sur la partie « biologie » pour bien comprendre la question posée et son objectif ainsi que la stratégie que vous adopterez ainsi que l’exemple (à rendre pour le vendredi 22 mars maximum). 
2. Deuxième partie : 
Rapport final à rendre (date à définir) : partie biologie (corrigée) + exemple d’intérêt traité + programme python (annoté) en annexe.


Partie Biologie : explication 

L’analyse des génomes représente un aspect fondamental de la biologie moléculaire, permettant notamment de faire avancer notre savoir sur les gènes et leur impact au sein de l’organisme. Cette discipline requiert une connaissance de tous les processus ayant lieu sur l’ADN qui permettent aux gènes qu’il contient de s’exprimer. 

Une des étapes primordiales consiste en la réplication de l’ADN. Les origines de réplication sont les sites où l'ADN commence à se répliquer, initiant ainsi le processus de duplication de l'information génétique. La prédiction de ces origines est essentielle pour comprendre la dynamique de réplication, ainsi que la structure des plasmides et les diverses applications que l’on peut en tirer en biotechnologie.

L'objectif principal de notre projet est de développer un outil informatique permettant de prédire les emplacements des origines de réplication chez les bactéries. Ces prédictions sont basées sur des caractéristiques spécifiques des séquences d'ADN, telles que les motifs de nucléotides. 

Pour prédire les origines de réplication, nous adoptons une approche basée sur la recherche de “point de rebroussement” ou “point d’inversion”. 
Un point de rebroussement fait référence à une région dans une séquence d'ADN où la direction de la séquence change brusquement. Cela signifie que la séquence est lue dans une direction donnée, puis elle est inversée et lue dans la direction opposée.
Étant donnée la circularité de l’ADN bactérien, la réplication démarre au niveau de l’origine de réplication puis se poursuit dans les 2 sens, jusqu’au point où les deux se rencontrent qui est le point d’inversion. 


Ce point remarquable sur une séquence d’ADN peut être trouvé par différentes méthodes : la première consiste à observer la modification du pourcentage de nucléotide G et C calculé, la deuxième se calcule en prenant la courbe ratio nbC-nbG /nbC+nbG) le long d'une séquence d'ADN inverse. 

La prédiction n’est pas exacte, mais permet de se concentrer sur une partie de séquence à partir du point d’inversion, pour rechercher l’origine de réplication.







Potentiels exemples d'application : 
pBR322 : C'est l'un des plasmides les plus largement utilisés en biologie moléculaire. Il contient plusieurs sites de restriction bien caractérisés et a été largement séquencé, ce qui le rend idéal pour les expériences de clonage et de génie génétique.


pUC19 : Ce plasmide est souvent utilisé comme vecteur de clonage. Il contient une origine de réplication d'origine bactérienne (ori), ce qui en fait un bon candidat pour votre projet de prédiction des origines de réplication.


pET28a : Ce plasmide est largement utilisé pour l'expression de protéines recombinantes dans Escherichia coli. Il contient également une origine de réplication bactérienne bien caractérisée.


pACYC184 : Un autre plasmide couramment utilisé en biologie moléculaire. Il possède des origines de réplication bien définies et a été largement étudié.


ColE1 : Ce plasmide est très utilisé dans la recherche en biologie moléculaire. Il est connu pour son origine de réplication de type ColE1, qui est bien caractérisée.


