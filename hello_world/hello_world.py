print('Zdravei Svqt')

import os
import re
import random
import pygame as pg
from pygame.locals import *
def sorted_nicely(l):
	convert = lambda text: int(text) if text.isdigit() else text
	alphanum_key = lambda key: [convert(c) for c in re.split("([0-9]+)", key)]
	return sorted(l, key=alphanum_key)
pg.init()
pg.mixer.init()
clock = pg.time.Clock()
class Text(pg.sprite.Sprite):
	def __init__(self, text, font, color):
		super(Text, self).__init__()
		self.type = "Text"
		self.string = text
		self.font = font
		self.color = color
		self.surf = font.render(text, True, color)
		self.rect = self.surf.get_rect()
	def draw(self, x, y):
		global screen, sprite_group
		self.move(x, y)
		screen.blit(self.surf, self.rect)
		sprite_group.add(self)
	def destroy(self):
		self.kill()
	def move(self, x, y):
		self.rect.centerx = x
		self.rect.centery = y
class Button(pg.sprite.Sprite):
	def __init__(self, text, color, bg_color, hover_color, font, width, height):
		super(Button, self).__init__()
		self.type = "Button"
		self.bg_color = bg_color
		self.hover_color = hover_color
		self.font = font
		self.width = width
		self.height = height
		self.text = Text(text, font, color)
		self.surf = pg.Surface((width, height))
		self.surf.fill(bg_color)
		self.rect = self.surf.get_rect()
		self.is_hover = False
	def draw(self, x, y):
		global screen, sprite_group
		self.move(x, y)
		screen.blit(self.surf, self.rect)
		sprite_group.add(self)
		self.text.draw(x, y)
	def destroy(self):
		self.kill()
		self.text.kill()
	def move(self, x, y):
		self.rect.centerx = x
		self.rect.centery = y
	def hover(self):
		self.surf.fill(self.hover_color)
		self.is_hover = True
	def no_hover(self):
		self.surf.fill(self.bg_color)
		self.is_hover = False
class Hero(pg.sprite.Sprite):
	def __init__(self, width, height, sprite, color="#ffffff"):
		super(Hero, self).__init__()
		self.color = color
		if sprite == "pravougulniche":
			self.surf = pg.Surface((width, height))
			self.surf.fill(color)
			self.type = "Hero_Pravougulniche"
		elif sprite == "krugche":
			self.surf = pg.Surface((width, height), pg.SRCALPHA)
			pg.draw.circle(self.surf, color, (width // 2, height // 2), width // 2)
			self.type = "Hero_Krugche"
		else:
			self.surf = pg.image.load(sprite).convert()
			self.surf = pg.transform.scale(self.surf, (width, height))
			self.anmations = {}
			self.index = 0
			self.current_time = 0
			self.animation_time = 0.1
			self.type = "Hero_Image"
		self.rect = self.surf.get_rect()
	def draw(self, x, y):
		global screen, sprite_group
		self.move(x, y)
		screen.blit(self.surf, self.rect)
		sprite_group.add(self)
	def destroy(self):
		self.kill()
	def move_with(self, x, y):
		self.rect.move_ip(x, y)
	def move(self, x, y):
		self.rect.centerx = x
		self.rect.centery = y
	def change_color(self, new_color):
		if self.type == "Hero_Image":
			return
		self.color = new_color
		self.surf.fill(new_color)
	def add_animation(self, name, path):
		if not self.type == "Hero_Image":
			try:
				raise TypeError("Kak she go animirash kat nqma snimki be...")
			except Exception as exep:
				print(exep)
		self.anmations[name] = []
		files = sorted_nicely(os.listdir(path))
		for file_name in files:
			image = pg.image.load(path + os.sep + file_name).convert()
			image = pg.transform.scale(image, (self.rect.width, self.rect.height))
			self.anmations[name].append(image)
	def play_animation(self, name, dt):
		if not self.type == "Hero_Image":
			try:
				raise TypeError("Kak she go animirash kat nqma snimki be...")
			except Exception as exep:
				print(exep)
		self.current_time += dt
		if self.current_time > self.animation_time:
			self.current_time = 0
			self.index = (self.index + 1) % len(self.anmations[name])
			self.surf = self.anmations[name][self.index]
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SHIRINA_EKRAN = SCREEN_WIDTH
VISOCHINA_EKRAN = SCREEN_HEIGHT
FPS = 30
CENTER = (640, 360.0)
screen = pg.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
sprite_group = pg.sprite.Group()
button_list = []
hero_data = {}
event_number = 1
izteklo_vreme = 0
clock_paused = True
running = True
ICON = pg.image.load("assets/ship/ship_1.png")
pg.display.set_icon(ICON)
pg.display.set_caption("Space Invaders 2.0")
FPS = 30
BACKGROUND_IMAGE = pg.image.load("assets/background.png").convert()
BACKGROUND_IMAGE = pg.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
screen.blit(BACKGROUND_IMAGE, (0, 0))

pg.mixer.music.load("assets/music/" + str(random.randint(1, 12)) + ".mp3")
pg.mixer.music.play(loops=-1)
pg.mixer.music.set_volume(0.8)

golemina_igrach = 64
skorost_na_igrach = 20
hero_data["igrach"] = dict(width=golemina_igrach, height=golemina_igrach, sprite="assets/ship/ship_1.png", color=(255, 255, 255))
if "igrach" in hero_data.keys():
	igrach = Hero(**hero_data["igrach"])
igrach.draw(CENTER[0], SCREEN_HEIGHT - 100)
igrach.add_animation("igrach_idle", "assets/ship")

lazeri = pg.sprite.Group()
hero_data["lazer"] = dict(width=16, height=32, sprite="assets/laser.png", color=(255, 255, 255))
skorost_lazer = -30
lazer_zvuk = pg.mixer.Sound("assets/laser.wav")
lazer_zvuk.set_volume(1.2)
sled_posledno_strelqne = 0

vragove = pg.sprite.Group()
hero_data["ufo"] = dict(width=64, height=64, sprite="assets/ufo/ufo_1.png", color=(255, 255, 255))
skorost_vrag = 3
RODI_VRAG = pg.USEREVENT + event_number
event_number += 1
pg.time.set_timer(RODI_VRAG, 1000)

explozii = pg.sprite.Group()
hero_data["exploziq"] = dict(width=90, height=90, sprite="assets/explosion/explosion_1.png", color=(255, 255, 255))

hero_data["pravougulnik"] = dict(width=40, height=40, sprite="krugche", color=(255, 255, 255))
if "pravougulnik" in hero_data.keys():
	pravougulnik = Hero(**hero_data["pravougulnik"])
pravougulnik.draw(0, 0)

golqm_font = pg.font.Font("assets/joystix.ttf", 120)
maluk_font = pg.font.Font("assets/joystix.ttf", 24)

igrai_text = Text('Play', golqm_font, (255, 255, 255))
pauza_text = Text('Paused', golqm_font, (255, 255, 255))
krai_text = Text('Game Over', golqm_font, (255, 255, 255))
tochki_text = Text('Score:0', maluk_font, (255, 255, 255))

if "tochki_text" in hero_data.keys():
	tochki_text = Hero(**hero_data["tochki_text"])
tochki_text.draw(SCREEN_WIDTH - 80, 20)

igrai_buton = Button('Play', (255, 255, 255), (71, 28, 12), (161, 87, 59), maluk_font, 100, 50)
button_list.append(igrai_buton)
izlez_buton = Button('Quit', (255, 255, 255), (71, 28, 12), (161, 87, 59), maluk_font, 100, 50)
button_list.append(izlez_buton)

igrai_text_plesnat = False
pauza_text_plesnat = False
krai_text_plesnat = False

sustoqnie = 'Nachalo'
tochki = 0

def mrudni_igrach(nakude):
	global igrach, skorost_na_igrach, golemina_igrach

	poziciq_igrach = (igrach.rect.centerx, igrach.rect.centery)

	if poziciq_igrach[0] <= 0:
		igrach.move_with(skorost_na_igrach, 0)
	elif poziciq_igrach[0] >= SCREEN_WIDTH:
		igrach.move_with(skorost_na_igrach * -1, 0)

	if nakude == 'nalqvo':
		igrach.move_with(skorost_na_igrach * -1, 0)
	elif nakude == 'nadqsno':
		igrach.move_with(skorost_na_igrach, 0)

def strelqi():
	global lazer, igrach, lazeri

	poziciq_igrach = (igrach.rect.centerx, igrach.rect.centery)

	lazer = Hero(**hero_data["lazer"])
	lazeri.add(lazer)
	lazer.draw(poziciq_igrach[0], poziciq_igrach[1])
	lazer_zvuk.play()

def update(dt, mouse_pos, events, keys):
	global izteklo_vreme, clock_paused
	pass
	global sled_posledno_strelqne, skorost_lazer, skorost_vrag, sustoqnie, igrai_text_plesnat, pauza_text_plesnat, krai_text_plesnat, igrai_text, pauza_text, igrai_buton, pauza_buton, izlez_buton, igrach, krai_text, pravougulnik, lazer, tochki, tochki_text

	if sustoqnie == 'Igra':
		print(izteklo_vreme)
		igrach.play_animation("igrach_idle", dt)
		for entity in explozii:
			entity.play_animation("exploziq_animaciq", dt)

		for entity in vragove:
			entity.play_animation("ufo_idle", dt)
		sled_posledno_strelqne += dt

		poz_mishka = mouse_pos
		pravougulnik.move(poz_mishka[0], poz_mishka[1])

		skorost_vrag = 3 + izteklo_vreme / 20

		if MOUSEMOTION in events:
			skorost_vrag += 0.1

		if keys[K_LEFT]:
			mrudni_igrach('nalqvo')
		elif keys[K_RIGHT]:
			mrudni_igrach('nadqsno')
		elif keys[K_ESCAPE] or MOUSEBUTTONDOWN in events:
			sustoqnie = 'Pauza'

		if sled_posledno_strelqne > 0.3 and keys[K_SPACE]:
			sled_posledno_strelqne = 0
			strelqi()

		for lazerche in lazeri:
			poziciq_lazerche = (lazerche.rect.centerx, lazerche.rect.centery)
			if poziciq_lazerche[1] - 20 < 0:
				lazerche.destroy()
			else:
				lazerche.move_with(0, skorost_lazer)

		if RODI_VRAG in events:
			sluchaino_x = random.randint(30, SCREEN_WIDTH - 30)
			sluchaino_y = random.randint(-300, -50)
			ufo = Hero(**hero_data["ufo"])
			vragove.add(ufo)
			ufo.draw(sluchaino_x, sluchaino_y)
			ufo.add_animation("ufo_idle", "assets/ufo")

		vragut_umre = False
		for vrag in vragove:
			poziciq_vrag = (vrag.rect.centerx, vrag.rect.centery)
			for lazerche in lazeri:
				if pg.sprite.collide_rect(lazerche, vrag):
					exploziq = Hero(**hero_data["exploziq"])
					explozii.add(exploziq)
					exploziq.draw(poziciq_vrag[0], poziciq_vrag[1])
					exploziq.add_animation("exploziq_animaciq", "assets/explosion")
					vrag.destroy()
					lazerche.destroy()
					vragut_umre = True
					tochki += 10
					tochki_text.destroy()
					tochki_text = Text('Score:' + str(tochki), maluk_font, (255, 255, 255))
					if "tochki_text" in hero_data.keys():
						tochki_text = Hero(**hero_data["tochki_text"])
					tochki_text.draw(SCREEN_WIDTH - (len(str(tochki)) * 8 + 80), 20)
					break
			if vragut_umre:
				vragut_umre = False
				break
			if poziciq_vrag[1] > SCREEN_HEIGHT - 120:
				sustoqnie = 'Krai'
			vrag.move_with(0, skorost_vrag)

		for exploziq in explozii:
			if exploziq.index == 11:
				exploziq.destroy()
	elif sustoqnie == 'Nachalo':
		if not igrai_text_plesnat:
			igrai_text_plesnat = True
			if "igrai_text" in hero_data.keys():
				igrai_text = Hero(**hero_data["igrai_text"])
			igrai_text.draw(CENTER[0], 200)
			if "igrai_buton" in hero_data.keys():
				igrai_buton = Hero(**hero_data["igrai_buton"])
			igrai_buton.draw(CENTER[0] - 100, 500)
			if "izlez_buton" in hero_data.keys():
				izlez_buton = Hero(**hero_data["izlez_buton"])
			izlez_buton.draw(CENTER[0] + 100, 500)
		if (igrai_buton.rect.x + igrai_buton.rect.width > mouse_pos[0] > igrai_buton.rect.x and igrai_buton.rect.y + igrai_buton.rect.height > mouse_pos[1] > igrai_buton.rect.y and MOUSEBUTTONDOWN in events) or keys[K_RETURN]:
			clock_paused = False
			pg.mouse.set_visible(False)
			igrai_text.destroy()
			igrai_buton.destroy()
			izlez_buton.destroy()
			sustoqnie = 'Igra'
			igrai_text_plesnat = False
		elif (izlez_buton.rect.x + izlez_buton.rect.width > mouse_pos[0] > izlez_buton.rect.x and izlez_buton.rect.y + izlez_buton.rect.height > mouse_pos[1] > izlez_buton.rect.y and MOUSEBUTTONDOWN in events) or keys[K_ESCAPE]:
			return "GAME OVER"
	elif sustoqnie == 'Pauza':
		if not pauza_text_plesnat:
			clock_paused = True
			pg.mouse.set_visible(True)
			igrach.surf = pg.transform.rotate(igrach.surf, 90)
			igrach.surf = pg.transform.scale(igrach.surf, (100, 100))
			pg.mixer.music.pause()
			pauza_text_plesnat = True
			if "pauza_text" in hero_data.keys():
				pauza_text = Hero(**hero_data["pauza_text"])
			pauza_text.draw(CENTER[0], 200)
			if "igrai_buton" in hero_data.keys():
				igrai_buton = Hero(**hero_data["igrai_buton"])
			igrai_buton.draw(CENTER[0] - 100, 500)
			if "izlez_buton" in hero_data.keys():
				izlez_buton = Hero(**hero_data["izlez_buton"])
			izlez_buton.draw(CENTER[0] + 100, 500)
		if (igrai_buton.rect.x + igrai_buton.rect.width > mouse_pos[0] > igrai_buton.rect.x and igrai_buton.rect.y + igrai_buton.rect.height > mouse_pos[1] > igrai_buton.rect.y and MOUSEBUTTONDOWN in events) or keys[K_RETURN]:
			clock_paused = False
			pg.mouse.set_visible(False)
			pg.mixer.music.unpause()
			pauza_text.destroy()
			igrai_buton.destroy()
			izlez_buton.destroy()
			sustoqnie = 'Igra'
			pauza_text_plesnat = False
		elif (izlez_buton.rect.x + izlez_buton.rect.width > mouse_pos[0] > izlez_buton.rect.x and izlez_buton.rect.y + izlez_buton.rect.height > mouse_pos[1] > izlez_buton.rect.y and MOUSEBUTTONDOWN in events):
			return "GAME OVER"
	elif sustoqnie == 'Krai':
		if not krai_text_plesnat:
			pg.mouse.set_visible(True)
			pg.mixer.music.fadeout(500)
			krai_text_plesnat = True
			if "krai_text" in hero_data.keys():
				krai_text = Hero(**hero_data["krai_text"])
			krai_text.draw(CENTER[0], 200)
			if "igrai_buton" in hero_data.keys():
				igrai_buton = Hero(**hero_data["igrai_buton"])
			igrai_buton.draw(CENTER[0] - 100, 500)
			if "izlez_buton" in hero_data.keys():
				izlez_buton = Hero(**hero_data["izlez_buton"])
			izlez_buton.draw(CENTER[0] + 100, 500)
		if (igrai_buton.rect.x + igrai_buton.rect.width > mouse_pos[0] > igrai_buton.rect.x and igrai_buton.rect.y + igrai_buton.rect.height > mouse_pos[1] > igrai_buton.rect.y and MOUSEBUTTONDOWN in events) or keys[K_RETURN]:
			pg.mixer.music.load("assets/music/" + str(random.randint(1, 12)) + ".mp3")
			pg.mixer.music.play(loops=-1)
			pg.mouse.set_visible(False)
			krai_text_plesnat = False
			krai_text.destroy()
			igrai_buton.destroy()
			izlez_buton.destroy()
			igrach.move(CENTER[0], SCREEN_HEIGHT - 100)
			skorost_vragove = 3
			for entity in vragove:
				entity.kill()
			for entity in lazeri:
				entity.kill()
			for entity in explozii:
				entity.kill()
			tochki = 0
			tochki_text.destroy()
			tochki_text = Text('Score:0', maluk_font, (255, 255, 255))
			if "tochki_text" in hero_data.keys():
				tochki_text = Hero(**hero_data["tochki_text"])
			tochki_text.draw(SCREEN_WIDTH - 80, 20)
			izteklo_vreme = 0
			sustoqnie = 'Igra'
		elif (izlez_buton.rect.x + izlez_buton.rect.width > mouse_pos[0] > izlez_buton.rect.x and izlez_buton.rect.y + izlez_buton.rect.height > mouse_pos[1] > izlez_buton.rect.y and MOUSEBUTTONDOWN in events) or keys[K_ESCAPE]:
			return "GAME OVER"
			

while running:
	dt = clock.tick(FPS) / 1000
	if not clock_paused:
		izteklo_vreme += dt
	mouse_pos = pg.mouse.get_pos()
	events = []
	keys = pg.key.get_pressed()
	screen.blit(BACKGROUND_IMAGE, (0, 0))
	for event in pg.event.get():
		events.append(event.type)
		if event.type == QUIT:
			running = False
	for btn in button_list:
		_ = (btn.rect.x, btn.rect.y, btn.rect.width, btn.rect.height)
		if _[0] + _[2] > mouse_pos[0] > _[0] and _[1] + _[3] > mouse_pos[1] > _[1] and not btn.is_hover:
			btn.hover()
		elif not (_[0] + _[2] > mouse_pos[0] > _[0] and _[1] + _[3] > mouse_pos[1] > _[3]):
			btn.no_hover()
	if update(dt, mouse_pos, events, keys) == "GAME OVER":
		running = False
	for entity in sprite_group:
		screen.blit(entity.surf, entity.rect)
	pg.display.flip()
pg.mixer.stop()
pg.mixer.music.stop()
pg.mixer.quit()
pg.quit()
os._exit(1)
