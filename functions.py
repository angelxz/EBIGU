

def init_game(width, height):
    py_code = (
        'import pygame as pg\n'
        'pg.init()\n'
        f'screen = pg.display.set_mode([{width}, {height}])\n'
        'running = True\n'
        'while running:\n'
        '   for event in pg.event.get():\n'
        '       if event.type == pg.QUIT:\n'
        '           running = False\n'
        '   screen.fill((255, 255, 255))\n'
        '   pg.draw.circle(screen, (0, 0, 255), (250, 250), 75)\n'
        '   pg.display.flip()\n'
        'pg.quit()\n'
    )

    return py_code


def set_icon(path):
    py_code = (
        f'iconchica = pg.image.load("{path}")\n'
        'pg.display.set_icon(iconchica)\n'
    )

    return py_code
