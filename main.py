music.play_melody("C D E F G A B C5", 120)
def on_button_pressed_a():
    basic.show_string("button a was pushed")
input.on_button_pressed(Button.A, on_button_pressed_a)