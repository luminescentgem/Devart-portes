extends Node2D

var couleur_cible = Color(1, 0, 0)  # Couleur cible du fondu
var duree_fondu = 2.0  # Durée du fondu en secondes

# Fonction pour réaliser un fondu de couleur
func fonduAuCouleur(couleur: Color, duree: float):
    var sprite_noir = ColorRect.new()  # Créer un nœud ColorRect
    sprite_noir.color = Color(0, 0, 0, 0)  # Couleur initiale transparente
    sprite_noir.rect_size = get_viewport_rect().size  # Taille du nœud égale à la taille de l'écran
    add_child(sprite_noir)  # Ajouter le nœud à la scène

    # Transition de la couleur transparente à la couleur spécifiée
    var transition = sprite_noir.color.interpolate(couleur, duree, Transitions.TYPE_LINEAR)

    # Effectuer le fondu
    var timer = Timer.new()
    timer.wait_time = duree
    add_child(timer)
    timer.start()

    # Fonction pour mettre à jour la couleur du fondu à chaque frame
    func _process(delta):
        sprite_noir.color = transition.advance(delta)

# Appel de la fonction lorsque la touche Espace est enfoncée
func _input(event):
    if event.is_action_pressed("ui_accept"):  # "ui_accept" est l'action associée à la touche Espace par défaut
        fonduAuCouleur(couleur_cible, duree_fondu)
