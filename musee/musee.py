# # import json

# # # Sample input data (replace with reading from 'donnees.json')
# # # input_data = {
# # #     "room": {"width": 10.0, "length": 10.0},
# # #     "artworks": [
# # #         {"id": "Africa1", "category": "Afrique", "width": 2.0, "length": 1.5, "artistic_value": 80, "historical_value": 70},
# # #         {"id": "Africa2", "category": "Afrique", "width": 1.5, "length": 1.0, "artistic_value": 90, "historical_value": 85},
# # #         {"id": "America1", "category": "Amérique", "width": 1.8, "length": 1.2, "artistic_value": 85, "historical_value": 65},
# # #         {"id": "America2", "category": "Amérique", "width": 2.0, "length": 1.0, "artistic_value": 75, "historical_value": 80},
# # #         {"id": "Asia1", "category": "Asie", "width": 1.5, "length": 1.5, "artistic_value": 95, "historical_value": 90},
# # #         {"id": "Asia2", "category": "Asie", "width": 2.0, "length": 1.8, "artistic_value": 70, "historical_value": 75},
# # #         {"id": "Europe1", "category": "Europe", "width": 1.7, "length": 1.3, "artistic_value": 88, "historical_value": 82},
# # #         {"id": "Europe2", "category": "Europe", "width": 1.9, "length": 1.1, "artistic_value": 78, "historical_value": 85},
# # #         {"id": "Oceania1", "category": "Océanie", "width": 1.6, "length": 1.4, "artistic_value": 92, "historical_value": 88},
# # #         {"id": "Oceania2", "category": "Océanie", "width": 1.8, "length": 1.2, "artistic_value": 80, "historical_value": 90}
# # #     ]
# # # }


# # with open("donnees.json", "r") as f:
# #     input_data = json.load(f)

# # # Function to compute total value
# # def compute_total_value(artwork):
# #     return 0.6 * artwork["artistic_value"] + 0.4 * artwork["historical_value"]

# # # Function to check if an artwork fits at position (x, y) without overlap
# # def can_place_artwork(artwork, x, y, placed_artworks, room_width, room_length):
# #     for placed in placed_artworks:
# #         # Check for overlap
# #         if not (x >= placed["x"] + placed["width"] or
# #                 x + artwork["width"] <= placed["x"] or
# #                 y >= placed["y"] + placed["length"] or
# #                 y + artwork["length"] <= placed["y"]):
# #             return False
# #     # Check if within room boundaries
# #     return x + artwork["width"] <= room_width and y + artwork["length"] <= room_length

# # # Main function to select and place artworks
# # def select_and_place_artworks(data):
# #     room_width = data["room"]["width"]
# #     room_length = data["room"]["length"]
# #     artworks = data["artworks"]
    
# #     # Group artworks by category
# #     categories = {"Afrique": [], "Amérique": [], "Asie": [], "Europe": [], "Océanie": []}
# #     for artwork in artworks:
# #         categories[artwork["category"]].append(artwork)
    
# #     # Compute total value for each artwork
# #     for category in categories:
# #         for artwork in categories[category]:
# #             artwork["total_value"] = compute_total_value(artwork)
# #         # Sort by total value in descending order
# #         categories[category].sort(key=lambda x: x["total_value"], reverse=True)
    
# #     # Determine number of artworks per category (assume equal number, e.g., 2 per category)
# #     num_per_category = 2  # Adjust based on room capacity or data
# #     selected_artworks = []
    
# #     # Select top artworks from each category
# #     for category in categories:
# #         selected_artworks.extend(categories[category][:num_per_category])
    
# #     # Place artworks row by row
# #     placed_artworks = []
# #     current_x, current_y = 0.0, 0.0
# #     current_row_height = 0.0
# #     output = []
    
# #     for artwork in selected_artworks:
# #         # Try to place in current row
# #         if can_place_artwork(artwork, current_x, current_y, placed_artworks, room_width, room_length):
# #             output.append({"id": artwork["id"], "x": current_x, "y": current_y})
# #             placed_artworks.append({
# #                 "x": current_x,
# #                 "y": current_y,
# #                 "width": artwork["width"],
# #                 "length": artwork["length"]
# #             })
# #             current_x += artwork["width"]
# #             current_row_height = max(current_row_height, artwork["length"])
# #         else:
# #             # Move to next row
# #             current_y += current_row_height
# #             current_x = 0.0
# #             current_row_height = 0.0
# #             # Try placing again
# #             if can_place_artwork(artwork, current_x, current_y, placed_artworks, room_width, room_length):
# #                 output.append({"id": artwork["id"], "x": current_x, "y": current_y})
# #                 placed_artworks.append({
# #                     "x": current_x,
# #                     "y": current_y,
# #                     "width": artwork["width"],
# #                     "length": artwork["length"]
# #                 })
# #                 current_x += artwork["width"]
# #                 current_row_height = max(current_row_height, artwork["length"])
# #             else:
# #                 print(f"Warning: Could not place artwork {artwork['id']}")
    
# #     return output

# # # Run the selection and placement
# # result = select_and_place_artworks(input_data)

# # # Save output to JSON file
# # with open("artwork_placement.json", "w") as f:
# #     json.dump(result, f, indent=2)

# # # Print result for verification
# # print(json.dumps(result, indent=2))



# import json
# import uuid



# with open("donnees.json", "r") as f:
#     input_data = json.load(f)

# # Function to compute total value
# def compute_total_value(artwork):
#     return 0.6 * artwork["valeur_artistique"] + 0.4 * artwork["valeur_historique"]

# # Function to check if an artwork fits at position (x, y) without overlap
# def can_place_artwork(artwork, x, y, placed_artworks, room_width, room_length):
#     for placed in placed_artworks:
#         if not (x >= placed["x"] + placed["width"] or
#                 x + artwork["largeur"] <= placed["x"] or
#                 y >= placed["y"] + placed["length"] or
#                 y + artwork["longueur"] <= placed["y"]):
#             return False
#     return x + artwork["largeur"] <= room_width and y + artwork["longueur"] <= room_length

# # Main function to select and place artworks
# def select_and_place_artworks(data):
#     room_width = data["room"]["width"]
#     room_length = data["room"]["length"]
#     artworks = data["artworks"]
    
#     # Group artworks by category
#     categories = {"Afrique": [], "Amérique": [], "Asie": [], "Europe": [], "Océanie": []}
#     for artwork in artworks:
#         if artwork["categorie"] in categories:
#             categories[artwork["categorie"]].append(artwork)
    
#     # Compute total value and sort by value
#     for category in categories:
#         for artwork in categories[category]:
#             artwork["total_value"] = compute_total_value(artwork)
#         categories[category].sort(key=lambda x: x["total_value"], reverse=True)
    
#     # Determine number of artworks per category (e.g., 1 per category for simplicity)
#     num_per_category = 1
#     # Adjust based on minimum number of artworks in any category
#     min_artworks = min(len(artworks) for artworks in categories.values() if artworks)
#     num_per_category = min(num_per_category, min_artworks)
    
#     # Select top artworks
#     selected_artworks = []
#     for category in categories:
#         selected_artworks.extend(categories[category][:num_per_category])
    
#     # Place artworks row by row
#     placed_artworks = []
#     output = []
#     current_x, current_y = 0.0, 0.0
#     current_row_height = 0.0
    
#     for artwork in selected_artworks:
#         if can_place_artwork(artwork, current_x, current_y, placed_artworks, room_width, room_length):
#             output.append({"id": artwork["id"], "x": current_x, "y": current_y})
#             placed_artworks.append({
#                 "x": current_x,
#                 "y": current_y,
#                 "width": artwork["largeur"],
#                 "length": artwork["longueur"]
#             })
#             current_x += artwork["largeur"]
#             current_row_height = max(current_row_height, artwork["longueur"])
#         else:
#             # Move to next row
#             current_y += current_row_height
#             current_x = 0.0
#             current_row_height = 0.0
#             if can_place_artwork(artwork, current_x, current_y, placed_artworks, room_width, room_length):
#                 output.append({"id": artwork["id"], "x": current_x, "y": current_y})
#                 placed_artworks.append({
#                     "x": current_x,
#                     "y": current_y,
#                     "width": artwork["largeur"],
#                     "length": artwork["longueur"]
#                 })
#                 current_x += artwork["largeur"]
#                 current_row_height = max(current_row_height, artwork["longueur"])
#             else:
#                 print(f"Warning: Could not place artwork {artwork['id']}")
    
#     return output

# # Read actual donnees.json (uncomment when file is available)
# # with open("donnees.json", "r") as f:
# #     input_data = json.load(f)

# # Run the selection and placement
# result = select_and_place_artworks(input_data)

# # Save output to JSON file
# with open("artwork_placement.json", "w") as f:
#     json.dump(result, f, indent=2)

# # Output result as artifact
# output_artifact = {
#     "artifact_id": str(uuid.uuid4()),
#     "title": "artwork_placement.json",
#     "contentType": "application/json",
#     "content": result
# }

# print(json.dumps(result, indent=2))




import json
from itertools import combinations

# Données fictives pour compléter les catégories manquantes

with open("donnees.json", "r") as f:
    donnees = json.load(f)

# Fonction pour calculer la valeur totale d'une œuvre
def calculer_valeur(oeuvre):
    return 0.6 * oeuvre["valeur_artistique"] + 0.4 * oeuvre["valeur_historique"]

# Fonction pour vérifier si une œuvre peut être placée sans chevauchement
def peut_placer(oeuvre, x, y, placement, largeur_salle, longueur_salle):
    if x + oeuvre["largeur"] > largeur_salle or y + oeuvre["longueur"] > longueur_salle:
        return False
    for placed in placement:
        px, py, p_oeuvre = placed["x"], placed["y"], placed["oeuvre"]
        if not (x >= px + p_oeuvre["largeur"] or x + oeuvre["largeur"] <= px or
                y >= py + p_oeuvre["longueur"] or y + oeuvre["longueur"] <= py):
            return False
    return True

# Fonction pour placer les œuvres dans la salle
def placer_oeuvres(oeuvres_selectionnees, largeur_salle, longueur_salle):
    placement = []
    for oeuvre in oeuvres_selectionnees:
        placed = False
        # Essayer de placer l'œuvre en parcourant la grille
        for y in range(0, int(longueur_salle * 10) + 1, 1):  # Pas de 0.1m
            y = y / 10
            for x in range(0, int(largeur_salle * 10) + 1, 1):  # Pas de 0.1m
                x = x / 10
                if peut_placer(oeuvre, x, y, placement, largeur_salle, longueur_salle):
                    placement.append({"oeuvre": oeuvre, "x": x, "y": y})
                    placed = True
                    break
            if placed:
                break
        if not placed:
            return None  # Impossible de placer toutes les œuvres
    return [{"id": p["oeuvre"]["id"], "x": p["x"], "y": p["y"]} for p in placement]

# Grouper les œuvres par catégorie
oeuvres_par_categorie = {"Afrique": [], "Amerique": [], "Asie": [], "Europe": [], "Oceanie": []}
for oeuvre in donnees["oeuvres"]:
    oeuvres_par_categorie[oeuvre["categorie"]].append(oeuvre)

# Sélectionner k œuvres par catégorie pour maximiser la valeur
k = 2  # Nombre d'œuvres par catégorie
meilleure_valeur = 0
meilleure_selection = None
meilleur_placement = None

# Générer toutes les combinaisons possibles de k œuvres par catégorie
for af in combinations(oeuvres_par_categorie["Afrique"], k):
    for am in combinations(oeuvres_par_categorie["Amerique"], k):
        for asie in combinations(oeuvres_par_categorie["Asie"], k):
            for eu in combinations(oeuvres_par_categorie["Europe"], k):
                for oc in combinations(oeuvres_par_categorie["Oceanie"], k):
                    selection = list(af) + list(am) + list(asie) + list(eu) + list(oc)
                    valeur_totale = sum(calculer_valeur(oeuvre) for oeuvre in selection)
                    # Vérifier si le placement est possible
                    placement = placer_oeuvres(selection, donnees["largeur_salle"], donnees["longueur_salle"])
                    if placement and valeur_totale > meilleure_valeur:
                        meilleure_valeur = valeur_totale
                        meilleure_selection = selection
                        meilleur_placement = placement

# Générer le fichier JSON de sortie
if meilleur_placement:
    with open("selection_oeuvres.json", "w", encoding="utf-8") as f:
        json.dump(meilleur_placement, f, indent=2)
    print("Fichier 'selection_oeuvres.json' généré avec succès.")
    print("Œuvres sélectionnées :", [oeuvre["id"] for oeuvre in meilleure_selection])
    print("Valeur totale :", meilleure_valeur)
else:
    print("Aucune solution trouvée pour placer les œuvres.")