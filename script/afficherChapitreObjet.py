extends Node2D

class Chatbox:
    var _sprite = null
    var _label = null
    var _dialogue_queue = []
    var _dialogue_in_progress = false

    func _init(sprite: Sprite):
        _sprite = Sprite.new()
        _sprite.texture = sprite.texture
        _sprite.position.y = get_viewport_rect().size.y - _sprite.texture.get_height()
        add_child(_sprite)

        _label = Label.new()
        _label.rect_min_size = Vector2(_sprite.texture.get_width(), _sprite.texture.get_height() / 2)
        _label.align = Label.ALIGN_CENTER
        _label.valign = Label.VALIGN_TOP
        _sprite.add_child(_label)

    func displayDialogue(dialogue: String):
        if _dialogue_in_progress:
            _dialogue_queue.append(dialogue)
            return

        _dialogue_in_progress = true
        _label.text = dialogue
        _label.rect_position = Vector2(0, _sprite.texture.get_height())
        var animation = _label.animate("rect_position", Vector2(0, -_label.rect_min_size.y), 0.1 * dialogue.length(), Tween.TRANS_LINEAR, Tween.EASE_OUT)
        animation.connect("tween_completed", self, "_on_DialogueComplete")

    func _on_DialogueComplete():
        if _dialogue_queue.size() > 0:
            var next_dialogue = _dialogue_queue.pop_front()
            displayDialogue(next_dialogue)
        else:
            _dialogue_in_progress = false




var Maddy = Chatbox.new(chatbox_sprite_character1)
var Narrateur = Chatbox.new(chatbox_sprite_character2)

# Lorsqu'un personnage parle, afficher le dialogue dans la chatbox correspondante
Maddy.displayDialogue("Bonjour ! Je suis le personnage 1.")
Narrateur.displayDialogue("Salut ! Je suis le personnage 2.")
