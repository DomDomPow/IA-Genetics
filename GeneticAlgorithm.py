# Voir document GA.pdf

# Soit une population initiale

# Tant que la règle n'est pas satisfaite
# do
#   Soit X(n) la population courante
#   Évaluer le degré d'adaptation de chaque individu
#   Sélectionner dans X(n) un ensemble de paires de solutions high quality
#   Appliquer à chacune des paires de soluions sélectionnées un opérateur de croisement
#   Remplacer une partie de X(n), formée des solutions basse qualité par des enfants de haute qualité
#   Appliquer un opérateur de mutation aux solutions ainsi obtenues
#   Les solutions éventuellement mutées constituent la population X(n+1)
# end


# Recombinaison OX
#   On replace les éléments non répétés en partant de la gauche de la zone à
#   échanger et on repart à droite quand on arrive à la fin de gauche (comme
#   dans un vieux jeu)

# すき な こと だけ おしえて たい
# Un lien très intéressant : http://www.theprojectspot.com/tutorial-post/applying-a-genetic-algorithm-to-the-travelling-salesman-problem/5 
