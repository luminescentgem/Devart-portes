extends Node2D

class Chatbox:
    var _sprite = null
    var _label = null
    var _dialogue_queue = []
    var _dialogue_in_progress = false
    var _scroll_speed = 0.1  # Vitesse de défilement par défaut

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
        var animation = _label.animate("rect_position", Vector2(0, -_label.rect_min_size.y), _scroll_speed * dialogue.length(), Tween.TRANS_LINEAR, Tween.EASE_OUT)
        animation.connect("tween_completed", self, "_on_DialogueComplete")

    func _on_DialogueComplete():
        if _dialogue_queue.size() > 0:
            var next_dialogue = _dialogue_queue.pop_front()
            displayDialogue(next_dialogue)
        else:
            _dialogue_in_progress = false

    func _process(delta):
        if Input.is_action_pressed("ui_accept"):
            _scroll_speed = 0.05  # Augmenter la vitesse de défilement lorsqu'Espac est enfoncé
        else:
            _scroll_speed = 0.1  # Revenir à la vitesse normale lorsque la touche Espace est relâchée

        if Input.is_action_pressed("ui_select"):
            if _dialogue_in_progress:
                _dialogue_queue.clear()
                _dialogue_in_progress = false
                _label.get_node_tween("rect_position").stop()
            else:
                _on_DialogueComplete()
