import heapq

lignes = []

with open("course3.txt", "r") as f:
    for ligne in f:
        nums = [int(x) for x in ligne.strip().split()]
        lignes.append(nums)

print("Lignes fin:")

# deplacement Bas
# deplacement droite
# depart en haut gauche
# arrivé en bas droite
# l'araignée met 1seconde pour paser d'un bloc à un autre de meme hauteur (hauteur = valeur de la case), 
# met 4 secondes pour monter d'un niveau et 2 secondes pour descendre d'un niveau

# j'ai une liste de liste

# 0 3 4 5 1
# 1 3 2 3 2
# 2 1 3 2 0

# On va utiliser Dijkstra pour trouver le chemin le plus rapide


def cout_deplacement(h1, h2):
    if h1 == h2:
        return 1
    elif h2 > h1:
        return 4
    else:
        return 2

def dijkstra(grille):
    rows, cols = len(grille), len(grille[0])
    depart = (0, 0)
    arrivee = (rows-1, cols-1)
    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (cout, x, y)
    directions = [(1, 0), (0, 1)]  # Bas, Droite

    while heap:
        cout, x, y = heapq.heappop(heap)
        if (x, y) == arrivee:
            return cout
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                c = cout_deplacement(grille[x][y], grille[nx][ny])
                if dist[nx][ny] > cout + c:
                    dist[nx][ny] = cout + c
                    heapq.heappush(heap, (dist[nx][ny], nx, ny))
    return -1

temps_min = dijkstra(lignes) # 17319
print("Temps minimum pour atteindre l'arrivée :", temps_min, "secondes")


def format_seconds(seconds):
    jours = seconds // 86400
    heures = (seconds % 86400) // 3600
    minutes = (seconds % 3600) // 60
    secondes = seconds % 60
    return f"{jours}/{heures:02d}/{minutes:02d}/{secondes:02d}"

print("Temps formaté :", format_seconds(temps_min)) # 0J/04H/48M/39S ( 0/04/48/39)