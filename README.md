# project_BI423
Projet BI 423 - Analyse des génomes

Sujet N°1 
Prédiction d’une origine de réplication chez bactérie (recherche de "point de rebroussement" ou « point d’inversion ») 

Faire une interface graphique pour présenter les résultats. Le rapport présentera :  
une explication générale du sujet (question biologique 1 à 2 pages), 
du programme python (décrit en détail) 
et le résultat d’une application sur un plasmide bactérien

1. Première partie :
Faire 1 à 2 pages sur la partie « biologie » pour bien comprendre la question posée et son objectif ainsi que la stratégie que vous adopterez ainsi que l’exemple. 
2. Deuxième partie : 
Rapport final à rendre : partie biologie (corrigée) + exemple d’intérêt traité + programme python (annoté) en annexe.


Partie Biologie : explication 

L'étude des génomes représente un aspect fondamental de la biologie moléculaire, permettant de progresser dans notre compréhension des gènes et de leur fonctionnement au sein des organismes. Cette discipline nécessite une bonne connaissance des processus se déroulant sur l'ADN.

Une étape cruciale de ces processus est la réplication de l'ADN, au cours de laquelle l'information génétique est dupliquée. Chez les bactéries, la réplication débute à un seul endroit sur le chromosome qui est circulaire, appelé origine de réplication (oriC), puis se poursuit dans les deux sens à partir de ce point.

La capacité à prédire avec précision l'emplacement de l'origine de réplication est essentielle pour comprendre la dynamique de réplication, ainsi que la structure des plasmides et les diverses applications que l’on peut en tirer en biotechnologie.

L'objectif principal de notre projet est de développer un programme informatique permettant de prédire ces emplacements chez les bactéries. Ces prédictions sont basées sur des caractéristiques spécifiques des séquences d'ADN, telles que le point d’inversion. 

Le point d'inversion, ou "point de rebroussement", est un point clé qui marque la transition entre deux régions d'ADN présentant des propriétés différentes, souvent en termes de contenu en bases comme la densité en guanine-cytosine (GC). 
Cette transition peut être détectée à l’aide de calculs.
Ce calcul consiste en un ratio (nbC-nbG / nbC+nbG) qui évolue tout au long de la séquence d'ADN et qui permet de tracer une courbe. 
La prédiction n’est pas exacte, mais permet de se concentrer sur une partie de séquence à partir du point d’inversion, pour rechercher l’origine de réplication.

Pour illustrer notre démarche, nous avons choisi d'utiliser le génome de staphyloccoccus aureus car il est assez petit donc facile à manipuler ;  mais aussi car on trouve un certain intérêt à détecter son origine de réplication étant donné qu'il s'agit d'un pathogène ayant un impact très important notamment dans les milieux hospitaliers. On y trouve ainsi un véritable enjeu. En utilisant des données génomiques disponibles, nous pourrons identifier le point d'inversion et élaborer un algorithme spécifique pour prédire l'origine de réplication.


