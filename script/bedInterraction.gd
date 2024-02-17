extends Node2D

class Bed extends Node2D:
    func interact():
        var color_fade = ColorFade.new()
        color_fade.fadeToColor(Color(0, 0, 0, 1), 5.0)  # Faire un fondu noir pendant 5 secondes

        yield(get_tree().create_timer(5.0), "timeout")  # Attendre 5 secondes

        var chatbox = Chatbox.new()
        chatbox.displayDialogue("A bien dormir !")
