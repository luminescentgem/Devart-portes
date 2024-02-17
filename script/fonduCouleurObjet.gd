extends Node2D

class ColorFade:
    var _color_rect = null

    func _init():
        _color_rect = ColorRect.new()
        _color_rect.color = Color(0, 0, 0, 0)  # Couleur initiale transparente
        _color_rect.rect_size = get_viewport_rect().size  # Taille du nœud égale à la taille de l'écran
        add_child(_color_rect)  # Ajouter le nœud à la scène

    func fadeToColor(target_color: Color, duration: float):
        var transition = _color_rect.color.interpolate(target_color, duration, Transitions.TYPE_LINEAR)
        var timer = Timer.new()
        timer.wait_time = duration
        add_child(timer)
        timer.start()
        timer.connect("timeout", self, "_on_TimerTimeout", [transition])

    func _on_TimerTimeout(transition):
        _color_rect.color = transition.end  # Assurez-vous que la couleur finale soit correcte



var color_fade = ColorFade.new()
color_fade.fadeToColor(Color(1, 1, 1), 2.0)  #le premier parametre est la couleur, le deuxieme est la durrée du fondu
