'''
All the python equivalent functions to the EBIGU actions
'''

import helpers as h

add_to_main_loop = ''


# ---------- Initializing functions -----------
def init_game(width, height):
    py_code = (
        'import os\n'
        'import re\n'
        'import random\n'
        'import pygame as pg\n'
        'from pygame.locals import *\n'
        'def sorted_nicely(l):\n'
        '\tconvert = lambda text: int(text) if text.isdigit() else text\n'
        '\talphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]\n'
        '\treturn sorted(l, key=alphanum_key)\n'
        'pg.init()\n'
        'pg.mixer.init()\n'
        'clock = pg.time.Clock()\n'
        'class Text(pg.sprite.Sprite):\n'
        '\tdef __init__(self, text, font, color):\n'
        '\t\tsuper(Text, self).__init__()\n'
        '\t\tself.type = "Text"\n'
        '\t\tself.string = text\n'
        '\t\tself.font = font\n'
        '\t\tself.color = color\n'
        '\t\tself.surf = font.render(text, True, color)\n'
        '\t\tself.rect = self.surf.get_rect()\n'
        '\tdef draw(self, x, y):\n'
        '\t\tglobal screen, sprite_group\n'
        '\t\tself.move(x, y)\n'
        '\t\tscreen.blit(self.surf, self.rect)\n'
        '\t\tsprite_group.add(self)\n'
        '\tdef destroy(self):\n'
        '\t\tself.kill()\n'
        '\tdef move(self, x, y):\n'
        '\t\tself.rect.centerx = x\n'
        '\t\tself.rect.centery = y\n'
        'class Button(pg.sprite.Sprite):\n'
        '\tdef __init__(self, text, color, bg_color, hover_color, font, width, height):\n'
        '\t\tsuper(Button, self).__init__()\n'
        '\t\tself.type = "Button"\n'
        '\t\tself.bg_color = bg_color\n'
        '\t\tself.hover_color = hover_color\n'
        '\t\tself.font = font\n'
        '\t\tself.width = width\n'
        '\t\tself.height = height\n'
        '\t\tself.text = Text(text, font, color)\n'
        '\t\tself.surf = pg.Surface((width, height))\n'
        '\t\tself.surf.fill(bg_color)\n'
        '\t\tself.rect = self.surf.get_rect()\n'
        '\t\tself.is_hover = False\n'
        '\tdef draw(self, x, y):\n'
        '\t\tglobal screen, sprite_group\n'
        '\t\tself.move(x, y)\n'
        '\t\tscreen.blit(self.surf, self.rect)\n'
        '\t\tsprite_group.add(self)\n'
        '\t\tself.text.draw(x, y)\n'
        '\tdef destroy(self):\n'
        '\t\tself.kill()\n'
        '\t\tself.text.kill()\n'
        '\tdef move(self, x, y):\n'
        '\t\tself.rect.centerx = x\n'
        '\t\tself.rect.centery = y\n'
        '\tdef hover(self):\n'
        '\t\tself.surf.fill(self.hover_color)\n'
        '\t\tself.is_hover = True\n'
        '\tdef no_hover(self):\n'
        '\t\tself.surf.fill(self.bg_color)\n'
        '\t\tself.is_hover = False\n'
        'class Hero(pg.sprite.Sprite):\n'
        '\tdef __init__(self, width, height, sprite, color="#ffffff"):\n'
        '\t\tsuper(Hero, self).__init__()\n'
        '\t\tself.color = color\n'
        '\t\tif sprite == "pravougulniche":\n'
        '\t\t\tself.surf = pg.Surface((width, height))\n'
        '\t\t\tself.surf.fill(color)\n'
        '\t\t\tself.type = "Hero_Pravougulniche"\n'
        '\t\telif sprite == "krugche":\n'
        '\t\t\tself.surf = pg.Surface((width, height), pg.SRCALPHA)\n'
        '\t\t\tpg.draw.circle(self.surf, color, (width // 2, height // 2), width // 2)\n'
        '\t\t\tself.type = "Hero_Krugche"\n'
        '\t\telse:\n'
        '\t\t\tself.surf = pg.image.load(sprite).convert()\n'
        '\t\t\tself.surf = pg.transform.scale(self.surf, (width, height))\n'
        '\t\t\tself.anmations = {}\n'
        '\t\t\tself.index = 0\n'
        '\t\t\tself.current_time = 0\n'
        '\t\t\tself.animation_time = 0.1\n'
        '\t\t\tself.type = "Hero_Image"\n'
        '\t\tself.rect = self.surf.get_rect()\n'
        '\tdef draw(self, x, y):\n'
        '\t\tglobal screen, sprite_group\n'
        '\t\tself.move(x, y)\n'
        '\t\tscreen.blit(self.surf, self.rect)\n'
        '\t\tsprite_group.add(self)\n'
        '\tdef destroy(self):\n'
        '\t\tself.kill()\n'
        '\tdef move_with(self, x, y):\n'
        '\t\tself.rect.move_ip(x, y)\n'
        '\tdef move(self, x, y):\n'
        '\t\tself.rect.centerx = x\n'
        '\t\tself.rect.centery = y\n'
        '\tdef change_color(self, new_color):\n'
        '\t\tif self.type == "Hero_Image":\n'
        '\t\t\treturn\n'
        '\t\tself.color = new_color\n'
        '\t\tself.surf.fill(new_color)\n'
        '\tdef add_animation(self, name, path):\n'
        '\t\tif not self.type == "Hero_Image":\n'
        '\t\t\ttry:\n'
        '\t\t\t\traise TypeError("Kak she go animirash kat nqma snimki be...")\n'
        '\t\t\texcept Exception as exep:\n'
        '\t\t\t\tprint(exep)\n'
        '\t\tself.anmations[name] = []\n'
        '\t\tfiles = sorted_nicely(os.listdir(path))\n'
        '\t\tfor file_name in files:\n'
        '\t\t\timage = pg.image.load(path + os.sep + file_name).convert()\n'
        '\t\t\timage = pg.transform.scale(image, (self.rect.width, self.rect.height))\n'
        '\t\t\tself.anmations[name].append(image)\n'
        '\tdef play_animation(self, name, dt):\n'
        '\t\tif not self.type == "Hero_Image":\n'
        '\t\t\ttry:\n'
        '\t\t\t\traise TypeError("Kak she go animirash kat nqma snimki be...")\n'
        '\t\t\texcept Exception as exep:\n'
        '\t\t\t\tprint(exep)\n'
        '\t\tself.current_time += dt\n'
        '\t\tif self.current_time > self.animation_time:\n'
        '\t\t\tself.current_time = 0\n'
        '\t\t\tself.index = (self.index + 1) % len(self.anmations[name])\n'
        '\t\t\tself.surf = self.anmations[name][self.index]\n'
        f'SCREEN_WIDTH = {width}\n'
        f'SCREEN_HEIGHT = {height}\n'
        'SHIRINA_EKRAN = SCREEN_WIDTH\n'
        'VISOCHINA_EKRAN = SCREEN_HEIGHT\n'
        'FPS = 30\n'
        f'CENTER = ({int(width) // 2}, {int(height) / 2})\n'
        'screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])\n'
        'sprite_group = pg.sprite.Group()\n'
        'button_list = []\n'
        'hero_data = {}\n'
        'event_number = 1\n'
        'izteklo_vreme = 0\n'
        'clock_paused = True\n'
        'running = True\n'
    )

    return py_code


def set_icon(tabs, path):
    py_code = (
        f'\n{tabs}ICON = pg.image.load("{path}")\n'
        f'{tabs}pg.display.set_icon(ICON)\n'
    )

    return py_code


def set_window_caption(caption):
    py_code = (
        f'pg.display.set_caption("{caption}")\n'
    )

    return py_code


def set_fps(fps):
    py_code = (
        f'FPS = {fps}\n'
    )

    return py_code


def set_background(tabs, background):
    global add_to_main_loop

    if h.hex2rgb(background):
        color = h.hex2rgb(background)
        py_code = (
            f'\nscreen.fill({color})\n'
        )
        add_to_main_loop += 'screen.fill({color})\n'
    else:
        py_code = (
            f'\n{tabs}BACKGROUND_IMAGE = pg.image.load("{background}").convert()\n'
            f'{tabs}BACKGROUND_IMAGE = pg.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))\n'
            f'{tabs}screen.blit(BACKGROUND_IMAGE, (0, 0))\n'
        )
        add_to_main_loop += 'screen.blit(BACKGROUND_IMAGE, (0, 0))\n'

    return py_code


# ---------- If functions -----------
def is_mousedown():
    py_code = (
        f'MOUSEBUTTONDOWN in events'
    )

    return py_code


def is_mousemotion():
    py_code = (
        f'MOUSEMOTION in events'
    )

    return py_code


def is_button_clicked(button):
    py_code = (
        f'({button}.rect.x + {button}.rect.width > mouse_pos[0] > {button}.rect.x and {button}.rect.y + {button}.rect.height > mouse_pos[1] > {button}.rect.y and MOUSEBUTTONDOWN in events)'
    )

    return py_code


def is_key_pressed(key):

    py_code = (
        f'keys[{key}]'
    )

    return py_code


def has_any_collided(sprite, group):
    py_code = (
        f'pg.sprite.spritecollideany({sprite}, {group})'
    )

    return py_code


def has_collided(sprite1, sprite2):
    py_code = (
        f'pg.sprite.collide_rect({sprite1}, {sprite2})'
    )

    return py_code


def is_outside(sprite):
    py_code = (
        f'(SCREEN_WIDTH < {sprite}.rect.x + {sprite}.rect.width or {sprite}.rect.x < 0 \
        or SCREEN_HEIGHT < {sprite}.rect.y + {sprite}.rect.height or {sprite}.rect.y < 0)'
    )

    return py_code


def is_event(event):
    py_code = (
        f'{event} in events'
    )

    return py_code


# ---------- New Object functions -----------
def new_hero(name, width, height, sprite, color='#ffffff'):
    if not color:
        color = '#ffffff'
    color = h.hex2rgb(color)

    py_code = (
        f'hero_data["{name}"] = dict(width={width}, height={height}, sprite="{sprite}", color={color})\n'
    )

    return py_code


def new_font(name, path, size):
    py_code = (
        f'{name} = pg.font.Font("{path}", {size})\n'
    )

    return py_code


def new_text(name, text, font, color):
    color = h.hex2rgb(color)
    py_code = (
        f'{name} = Text({text}, {font}, {color})\n'
    )

    return py_code


def new_button(name, text, color, bg_color, hover_color, font, width, height):
    color = h.hex2rgb(color)
    bg_color = h.hex2rgb(bg_color)
    hover_color = h.hex2rgb(hover_color)

    py_code = (
        f'{name} = Button({text}, {color}, {bg_color}, {hover_color}, {font}, {width}, {height})\n'
        f'button_list.append({name})\n'
    )

    return py_code


def new_event(name):
    py_code = (
        f'{name} = pg.USEREVENT + event_number\n'
        f'event_number += 1\n'
    )

    return py_code


# ---------- Music and Sound -----------
def new_sound(name, path):
    py_code = (
        f'{name} = pg.mixer.Sound("{path}")\n'
    )

    return py_code


def play_sound(sound):
    py_code = (
        f'{sound}.play()\n'
    )

    return py_code


def set_sound_volume(sound, volume):
    py_code = (
        f'{sound}.set_volume({volume})\n'
    )

    return py_code


def set_music_volume(volume):
    py_code = (
        f'pg.mixer.music.set_volume({volume})\n'
    )

    return py_code


def play_music(tabs, path):
    py_code = (
        f'\n{tabs}pg.mixer.music.load("{path}")\n'
        f'{tabs}pg.mixer.music.play(loops=-1)\n'
    )

    return py_code


def unpause_music():
    py_code = (
        'pg.mixer.music.unpause()\n'
    )

    return py_code


def pause_music():
    py_code = (
        'pg.mixer.music.pause()\n'
    )

    return py_code


def stop_music():
    py_code = (
        'pg.mixer.music.fadeout(500)\n'
    )

    return py_code


# ---------- Manipulate Objects -----------
def draw(tabs, sprite, x, y):
    py_code = (
        f'\n{tabs}if "{sprite}" in hero_data.keys():\n'
        f'{tabs}\t{sprite} = Hero(**hero_data["{sprite}"])\n'
        f'{tabs}{sprite}.draw({x}, {y})\n'
    )

    return py_code


def destroy(sprite):
    py_code = (
        f'{sprite}.destroy()\n'
    )

    return py_code


def move(sprite, x, y):
    py_code = (
        f'{sprite}.move({x}, {y})\n'
    )

    return py_code


def move_with(sprite, x, y):
    py_code = (
        f'{sprite}.move_with({x}, {y})\n'
    )

    return py_code


def change_size(sprite, width, height):
    py_code = (
        f'{sprite}.surf = pg.transform.scale({sprite}.surf, ({width}, {height}))\n'
    )

    return py_code


def rotate(sprite, angle):
    py_code = (
        f'{sprite}.surf = pg.transform.rotate({sprite}.surf, {angle})\n'
    )

    return py_code


# ---------- Get functions -----------
def get_mouse_pos():
    py_code = (
        'mouse_pos\n'
    )

    return py_code


def get_pos(sprite):
    py_code = (
        f'({sprite}.rect.centerx, {sprite}.rect.centery)\n'
    )

    return py_code


def get_size(sprite):
    py_code = (
        f'({sprite}.rect.width, {sprite}.rect.height)\n'
    )

    return py_code


# ---------- Animations -----------
def new_animation(name, sprite, path):
    py_code = (
        f'{sprite}.add_animation("{name}", "{path}")\n'
    )

    return py_code


def play_animation(animation, sprite):
    py_code = (
        f'{sprite}.play_animation("{animation}", dt)\n'
    )

    return py_code


def play_group_animation(tabs, animation, group):
    py_code = (
        f'\n{tabs}for entity in {group}:\n'
        f'{tabs}\tentity.play_animation("{animation}", dt)\n'
    )

    return py_code


# ---------- Sprite Groups -----------
def new_hero_group(name):
    py_code = (
        f'{name} = pg.sprite.Group()\n'
    )

    return py_code


def add_to_group(tabs, sprite, group, x, y):
    py_code = (
        f'\n{tabs}{sprite} = Hero(**hero_data["{sprite}"])\n'
        f'{tabs}{group}.add({sprite})\n'
        f'{tabs}{sprite}.draw({x}, {y})\n'
    )

    return py_code


def remove_from_group(sprite, group):
    py_code = (
        f'{group}.remove({sprite})\n'
    )

    return py_code


def empty_group(tabs, group):
    py_code = (
        f'\n{tabs}for entity in {group}:\n'
        f'{tabs}\tentity.kill()\n'
    )

    return py_code


# ---------- Other -----------
def exec_after(time, event):
    py_code = (
        f'pg.time.set_timer({event}, {time}, True)\n'
    )

    return py_code


def set_timer(time, event):
    py_code = (
        f'pg.time.set_timer({event}, {time})\n'
    )

    return py_code


def start_clock():
    py_code = (
        f'clock_paused = False\n'
    )

    return py_code


def pause_clock():
    py_code = (
        f'clock_paused = True\n'
    )

    return py_code


def reset_clock():
    py_code = (
        f'izteklo_vreme = 0\n'
    )

    return py_code


def show_cursor():
    py_code = (
        'pg.mouse.set_visible(True)\n'
    )

    return py_code


def hide_cursor():
    py_code = (
        'pg.mouse.set_visible(False)\n'
    )

    return py_code


# ---------- Main Function -----------
def update():
    py_code = (
        'def update(dt, mouse_pos, events, keys):\n'
        '\tglobal izteklo_vreme, clock_paused\n'
        '\tpass\n'
    )

    return py_code


# ---------- Quit game action -----------
def game_over():
    py_code = (
        'return "GAME OVER"\n'
    )

    return py_code


# ---------- End of file action -----------
def gg():
    global add_to_main_loop

    add_to_main_loop = add_to_main_loop.replace('\n', '\n\t')
    add_to_main_loop = add_to_main_loop[:add_to_main_loop.rfind('\t')]
    add_to_main_loop = '\t' + add_to_main_loop if add_to_main_loop else ''

    py_code = (
        'while running:\n'
        '\tdt = clock.tick(FPS) / 1000\n'
        '\tif not clock_paused:\n'
        '\t\tizteklo_vreme += dt\n'
        '\tmouse_pos = pg.mouse.get_pos()\n'
        '\tevents = []\n'
        '\tkeys = pg.key.get_pressed()\n'
        f'{add_to_main_loop}'
        '\tfor event in pg.event.get():\n'
        '\t\tevents.append(event.type)\n'
        '\t\tif event.type == QUIT:\n'
        '\t\t\trunning = False\n'
        '\tfor btn in button_list:\n'
        '\t\t_ = (btn.rect.x, btn.rect.y, btn.rect.width, btn.rect.height)\n'
        '\t\tif _[0] + _[2] > mouse_pos[0] > _[0] and _[1] + _[3] > mouse_pos[1] > _[1] and not btn.is_hover:\n'
        '\t\t\tbtn.hover()\n'
        '\t\telif not (_[0] + _[2] > mouse_pos[0] > _[0] and _[1] + _[3] > mouse_pos[1] > _[3]):\n'
        '\t\t\tbtn.no_hover()\n'
        '\tif update(dt, mouse_pos, events, keys) == "GAME OVER":\n'
        '\t\trunning = False\n'
        '\tfor entity in sprite_group:\n'
        '\t\tscreen.blit(entity.surf, entity.rect)\n'
        '\tpg.display.flip()\n'
        'pg.mixer.stop()\n'
        'pg.mixer.music.stop()\n'
        'pg.mixer.quit()\n'
        'pg.quit()\n'
        'os._exit(1)'
    )

    return py_code
