import mido
from pynput.keyboard import Controller, Key

# A map of MIDI notes to keyboard keys
midi_to_keyboard = {
    60: 'a', # C4
    61: 's', # C#4
    62: 'd', # D4
    79: Key.up, # G5
}

def on_note_on(message):
    if message.type == 'note_on' and message.note in midi_to_keyboard:
        with Controller() as controller:
            key = midi_to_keyboard[message.note]
            controller.press(key)
            controller.release(key)

# Listen to all incoming MIDI messages
with mido.open_input() as inport:
    for message in inport:
        on_note_on(message)
