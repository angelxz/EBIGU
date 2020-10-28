'''
The dictionary of EBIGU actions with their equivalent function name
EBIGU action -> function name
'''

import re
import functions as f


def get_funcs_list():
    funcs_list = [
        {
            'func': f.init_game,
            'pattern': re.compile(r'prozorcheto da mi bude \((?P<width>[0-9]+), (?P<height>[0-9]+)\)')
        },
        {
            'func': f.set_icon,
            'pattern': re.compile(r'ikonkata da mi bude \'|"(?P<path>.+)\'|"')
        },
        # 'igrata mi se kazva' => 'set_window_caption'
        # 'plesni': {'func': 'draw', 'pattern': re.compile(r'')},
        # 'mahni': {'func': 'remove', 'pattern': re.compile(r'')},
        # 'poziciq': {'func': 'get_pos', 'pattern': re.compile(r'')},
        # 'mrudni': {'func': 'move', 'pattern': re.compile(r'')},
        # 'geroi': {'func': 'new_hero', 'pattern': re.compile(r'')},
        # 'font': {'func': 'new_font', 'pattern': re.compile(r'')},
        # 'text': {'func': 'new_text', 'pattern': re.compile(r'')},
        # 'zvuk': {'func': 'new_sound', 'pattern': re.compile(r'')},
        # 'izpei': {'func': 'play_sound', 'pattern': re.compile(r'')},
        # 'pei': {'func': 'loop_sound', 'pattern': re.compile(r'')},
        # 'zavurti': {'func': 'rotate', 'pattern': re.compile(r'')},
        # 'ugolemi': {'func': 'make_bigger', 'pattern': re.compile(r'')},
        # 'smali': {'func': 'make_smaller', 'pattern': re.compile(r'')},
        # 'napravi': {'func': 'change_size', 'pattern': re.compile(r'')},
        # 'golemina': {'func': 'get_size', 'pattern': re.compile(r'')},
        # 'zavurtqnost': {'func': 'get_angle', 'pattern': re.compile(r'')},
        # 'blusne': {'func': 'has_collided', 'pattern': re.compile(r'')},
        # 'kliknat': {'func': 'is_clicked', 'pattern': re.compile(r'')},
        # 'natisnat': {'func': 'is_pressed', 'pattern': re.compile(r'')},
        # 'osnoven_cikul': {'func': 'update', 'pattern': re.compile(r'')},
        # 'sluchaino': {'func': 'random', 'pattern': re.compile(r'')},
        # 'krai na igrata': {'func': 'game_over', 'pattern': re.compile(r'')},
    ]

    return funcs_list
