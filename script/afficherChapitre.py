extends Node2D


func afficherEtDisparaitreAvecFondu(sprite: Sprite):
    
    # Positionner le sprite au milieu du haut de l'écran
    sprite.position.x = get_viewport_rect().size.x / 2 - sprite.texture.get_width() / 2
    sprite.position.y = 0

    # Ajouter le sprite à la scène
    add_child(sprite)

  
    var timer = Timer.new()
    var duree_fondu = 1.0
    timer.wait_time = 7.0 - duree_fondu  
    add_child(timer)
    timer.start()

    # Fonction pour réaliser le fondu
    func _on_Timer_timeout():
        var fade = sprite.modulate.a  # Opacité actuelle du sprite
        var fade_out = fade.interpolate(0, duree_fondu)  # Opacité à atteindre (0 pour fondu complet)
        var transition = Tween.new()
        sprite.add_child(transition)
        transition.interpolate_property(sprite, "modulate:a", fade, fade_out, duree_fondu, Tween.TRANS_LINEAR, Tween.EASE_IN_OUT)
        transition.start()
        transition.connect("tween_completed", self, "_on_FadeOutComplete")

    # Fonction appelée lorsque le fondu est terminé
    func _on_FadeOutComplete():
        sprite.queue_free()  # Supprimer le sprite de la scène après le fondu


var sprite_node = Sprite.new()
sprite_node.texture = load("res://sprite.png")


afficherEtDisparaitreAvecFondu(sprite_node)
