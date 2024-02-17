extends Node2D

class InteractiveObject:
    var _sprite = null
    var _interaction_text = ""
    var _chatbox = null
    var _interaction_in_progress = false

    func _init(sprite: Sprite, interaction_text: String):
        _sprite = Sprite.new()
        _sprite.texture = sprite.texture
        add_child(_sprite)

        _interaction_text = interaction_text

    func interact():
        if not _interaction_in_progress:
            _interaction_in_progress = true
            if _chatbox == null:
                _chatbox = Chatbox.new()  # Créer une nouvelle instance de la classe Chatbox
                _chatbox.displayDialogue(_interaction_text)  # Afficher le texte d'interaction dans la chatbox
            else:
                _chatbox.displayDialogue(_interaction_text)  # Afficher le texte d'interaction dans la chatbox existante
