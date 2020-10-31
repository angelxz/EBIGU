'''
The list of EBIGU actions
func is the equivalent function to the EBIGU action
pattern is the pattern of the EBIGU action
'''

import re
import functions as f


def get_func_list():
    func_list = [
        # ---------- Initializing functions -----------
        {
            # Initializes the window size, pygame and everything else needed
            # Has to be the first EBIGU action
            'func': f.init_game,
            'pattern': re.compile(r'prozorcheto da mi bude \((?P<width>\w+?), (?P<height>\w+?)\)\n')
        },
        {
            # Sets the icon of the window
            'func': f.set_icon,
            'pattern': re.compile(r'\n(?P<tabs>\t*)ikonkata da mi bude (?P<path>.+?)\n'),
            'run_twice': True
        },
        {
            # Sets the window caption (title)
            'func': f.set_window_caption,
            'pattern': re.compile(r'igrata mi se kazva \'(?P<caption>.+?)\'\n')
        },
        {
            # Sets the frames per second with which the game should run
            'func': f.set_fps,
            'pattern': re.compile(r'nadqvam se igrata mi da vurvi s (?P<fps>\w+?) fps\n')
        },
        {
            # Sets the background to a certain image or color if color is given
            'func': f.set_background,
            'pattern': re.compile(r'\n(?P<tabs>\t*)fonut da mi bude (?P<background>.+?)\n'),
            'run_twice': True
        },
        # ---------- If functions -----------
        {
            # Checks if the mouse is being clicked
            'func': f.is_mousedown,
            'pattern': re.compile(r'mishkata e cuknata(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if the mouse in motions
            'func': f.is_mousemotion,
            'pattern': re.compile(r'mishkata murda(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if a button is clicked
            'func': f.is_button_clicked,
            'pattern': re.compile(r'buton (?P<button>\w+?) e kliknat(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if a key is being pressed
            'func': f.is_key_pressed,
            'pattern': re.compile(r'(?P<key>\w+?) e natisnat(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if a collision has occured between a sprite and a group
            'func': f.has_any_collided,
            'pattern': re.compile(r'(?P<sprite>\w+?) se blusne s neshto ot (?P<group>\w+?)(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if a collision has occured between 2 sprites
            'func': f.has_collided,
            'pattern': re.compile(r'(?P<sprite1>\w+?) se blusne s (?P<sprite2>\w+?)(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if a hero object (sprite) is outside the screen boundaries
            'func': f.is_outside,
            'pattern': re.compile(r'(?P<sprite>\w+?) izleze ot poleto(?=( i)|(:\n)| ili)')
        },
        {
            # Checks if an event is happening
            'func': f.is_event,
            'pattern': re.compile(r'subitie (?P<event>[A-Z0-9_]+?)(?=( i)|(:\n)| ili)')
        },
        # ---------- New Object functions -----------
        {
            # Creates a new hero object
            'func': f.new_hero,
            'pattern': re.compile(r'(?P<name>\w+?) = nov geroi s golemina \((?P<width>.+?), (?P<height>.+?)\) i sprite (?P<sprite>.+?)(?: s cvqt (?P<color>.+?))?\n')
        },
        {
            # Creates a new font object
            'func': f.new_font,
            'pattern': re.compile(r'(?P<name>\w+?) = nov font (?P<path>.+?) s golemina (?P<size>.+?)\n')
        },
        {
            # Creates a new text object
            'func': f.new_text,
            'pattern': re.compile(r'(?P<name>\w+?) = nov text (?P<text>.+?) s font (?P<font>\w+?) i cvqt (?P<color>.+?)\n')
        },
        {
            # Creates a new button object
            'func': f.new_button,
            'pattern': re.compile(r'(?P<name>\w+?) = nov buton (?P<text>.+?) s cvqt (?P<color>.+?) i fonov cvqt (?P<bg_color>.+?) i cvqt (?P<hover_color>.+?) pod kursora i font (?P<font>\w+?) i golemina \((?P<width>.+?), (?P<height>.+?)\)\n')
        },
        {
            # Creates a new user event
            'func': f.new_event,
            'pattern': re.compile(r'(?P<name>[A-Z0-9_]+?) = novo subitie\n')
        },
        # ---------- Music and Sound -----------
        {
            # Loads a new sound from the given audio file
            'func': f.new_sound,
            'pattern': re.compile(r'(?P<name>\w+?) = nov zvuk (?P<path>.+?)\n')
        },
        {
            # Plays a sound which is already loaded
            'func': f.play_sound,
            'pattern': re.compile(r'izpei (?P<sound>\w+?)\n')
        },
        {
            # Sets the volume of the given sound
            'func': f.set_sound_volume,
            'pattern': re.compile(r'izpeivai (?P<sound>\w+?) s (?P<volume>[a-zA-Z0-9_.]+?) zvuk\n')
        },
        {
            # Sets the music volume (has to be before play_music)
            'func': f.set_music_volume,
            'pattern': re.compile(r'pei s (?P<volume>[a-zA-Z0-9_.]+?) zvuk\n')
        },
        {
            # Loads and starts playing the audio file given (looping it)
            'func': f.play_music,
            'pattern': re.compile(r'\n(?P<tabs>\t*)pei (?P<path>.+?)\n'),
            'run_twice': True
        },
        {
            # Plays the music again (after being paused)
            'func': f.unpause_music,
            'pattern': re.compile(r'otpauzirai peeneto\n')
        },
        {
            # Pauses the music (has to bi after unpause_music)
            'func': f.pause_music,
            'pattern': re.compile(r'pauzirai peeneto\n')
        },
        {
            # Stops the music (using fadeout for 0.5 seconds)
            'func': f.stop_music,
            'pattern': re.compile(r'q zemi se sopri s tva tvoe peene\n')
        },

        # ---------- Manipulate Objects -----------
        {
            # Shows the sprite given on the screen at the given coordinates
            'func': f.draw,
            'pattern': re.compile(r'\n(?P<tabs>\t*)plesni (?P<sprite>\w+?) na \((?P<x>.+?), (?P<y>.+?)\)\n'),
            'run_twice': True
        },
        {
            # Kills the sprite given (it is not being drawn anymore)
            'func': f.destroy,
            'pattern': re.compile(r'(?<=\n|\t)mahni (?P<sprite>\w+?)\n'),
        },
        {
            # Moves a sprite to the coordinates given
            'func': f.move,
            'pattern': re.compile(r'mrudni (?P<sprite>\w+?) na \((?P<x>.+?), (?P<y>.+?)\)\n')
        },
        {
            # Moves a sprite by the amount pixels given
            'func': f.move_by,
            'pattern': re.compile(r'mrudni (?P<sprite>\w+?) s \((?P<x>.+?), (?P<y>.+?)\)\n')
        },
        {
            # Changes the size of the given sprite
            'func': f.change_size,
            'pattern': re.compile(r'napravi (?P<sprite>\w+?) \((?P<width>.+?), (?P<height>.+?)\)\n')
        },
        {
            # Rotates the given sprite by the given angle
            'func': f.rotate,
            'pattern': re.compile(r'zavurti (?P<sprite>\w+?) s (?P<angle>\w+?) gradusa\n')
        },

        # ---------- Get functions -----------
        {
            # Gets you the current position of the cursor (has to be before get_pos)
            'func': f.get_mouse_pos,
            'pattern': re.compile(r'poziciq na mishkata\n'),
        },
        {
            # Gets you the position of a hero object (sprite) using centerx and centery
            'func': f.get_pos,
            'pattern': re.compile(r'poziciq na (?P<sprite>\w+?)\n')
        },
        {
            # Gets you the size of a hero object (sprite)
            'func': f.get_size,
            'pattern': re.compile(r'golemina na (?P<sprite>\w+?)\n')
        },

        # ---------- Animations -----------
        {
            # Adds an animation to the given sprite
            'func': f.new_animation,
            'pattern': re.compile(r'(?P<name>\w+?) = nova animaciq na (?P<sprite>\w+?) ot (?P<path>.+?)\n')
        },
        {
            # Plays the given animation on the sprite given
            'func': f.play_animation,
            'pattern': re.compile(r'animirai (?P<animation>\w+?) na (?P<sprite>\w+?)\n')
        },
        {
            # Plays the given animation on every member of the group given
            'func': f.play_group_animation,
            'pattern': re.compile(r'\n(?P<tabs>\t*)animirai (?P<animation>\w+?) na grupa (?P<group>\w+?)\n'),
            'run_twice': True
        },

        # ---------- Sprite Groups -----------
        {
            # Creates a new sprite group
            'func': f.new_hero_group,
            'pattern': re.compile(r'(?P<name>\w+?) = nova grupa\n'),
        },
        {
            # Adds a sprite to a group and draws it on the screen
            'func': f.add_to_group,
            'pattern': re.compile(r'\n(?P<tabs>\t*)dobavi (?P<sprite>\w+?) v (?P<group>\w+?) i go plesni na \((?P<x>.+?), (?P<y>.+?)\)\n'),
            'run_twice': True
        },
        {
            # Removes a sprite from a group
            'func': f.remove_from_group,
            'pattern': re.compile(r'(?<=\n|\t)mahni (?P<sprite>\w+?) ot (?P<group>\w+?)\n')
        },
        {
            # Kills all sprites from the group given
            'func': f.empty_group,
            'pattern': re.compile(r'\n(?P<tabs>\t*)izprazni grupa (?P<group>\w+?)\n'),
            'run_twice': True
        },

        # ---------- Other -----------
        {
            # Post an event after a given amount of milleseconds
            'func': f.exec_after,
            'pattern': re.compile(r'sled (?P<time>.+?) ms (?P<event>[A-Z0-9_]+?)\n')
        },
        {
            # Post an event every n amount of milleseconds
            'func': f.set_timer,
            'pattern': re.compile(r'prez (?P<time>.+?) ms (?P<event>[A-Z0-9_]+?)\n')
        },
        {
            # Starts to count the time elapsed since the start of the game (the izteklo_vreme variable)
            'func': f.start_clock,
            'pattern': re.compile(r'pusni chasovnika\n')
        },
        {
            # Pauses the izteklo_vreme variable
            'func': f.pause_clock,
            'pattern': re.compile(r'pauzirai chasovnika\n')
        },
        {
            # Resets the izteklo_vreme variable (time elapsed since the start of the game)
            'func': f.reset_clock,
            'pattern': re.compile(r'nulirai chasovnika\n')
        },
        {
            # Shows the cursor
            'func': f.show_cursor,
            'pattern': re.compile(r'pokazhi kursora\n')
        },
        {
            # Hides the cursor when it is over the pygame window
            'func': f.hide_cursor,
            'pattern': re.compile(r'skrii kursora\n')
        },

        # ---------- Main Function -----------
        {
            # This function is being called on every frame
            'func': f.update,
            'pattern': re.compile(r'osnoven cikul:\n')
        },

        # ---------- Quit game action -----------
        {
            # Used to exit the pygame window
            'func': f.game_over,
            'pattern': re.compile(r'krai na igrata\n')
        },

        # ---------- End of file action -----------
        {
            # Has to always be at the end of an EBIGU file
            # which has initialized pygame
            'func': f.gg,
            'pattern': re.compile(r'dobra igra')
        },
    ]

    return func_list
