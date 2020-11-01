# EBIGU

### EBIGU [ibígu] aka Extraordinary Basically Ingenious Gamemaking Utility is a simple "programming language" which I wrote in python for exactly 3 days xD It is mainly made for creating 2D games (using pygame as a base). Oh yes, and it is in Bulgarian :D (not in cyrillic though)

### You can also write pure python in .ebigu files and mix it with EBIGU, no probs


## Installation
You can either just clone the source code or download a compiled version from [the latest release](https://github.com/angelxz/EBIGU/releases/latest)

## Usage
Just open your .ebigu file with the EBIGU.py or EBIGU.exe
```bash
py EBIGU.py hello_world.ebigu
EBIGU.exe hello_world.ebigu
```

If you specify a thirt parameter (a python file) the source code will be translated and written in that file. (rather than executed)
```bash
py EBIGU.py hello_world.ebigu my_cool_file.py
```

## Contributing
I am 100% open for any ideas and contibutions :D

## Hello World
```eibgu
izpishi('Zdravei Svqt')
```
If ya wan't a more thorough hello world check out the [hello_world folder](hello_world/) in the repo. It is a simple af game which I wrote in the process of testing the language, perfect to get ya started. Btw, the assets are just some stuff I downloaded from the Internet so be careful with copyright and stuff if you intend to use them.

# The Docs
The official documentation of EBIGU :D
## The Basics
Assigning a variable:
```eibgu
kon = 'Mustang'
listche = [1, 2, 3]
```
If else statement:
```eibgu
ako kon e 'Mustang' ili 3 ne v listche:          # if kon == 'Mustang' or 3 not in listche
	ne pravi nishto                              # pass
ako li puk kon ne e 'Pesho' i kon ne e 'Gosho':  # elif kon != 'Pesho' and kon != 'Gosho'
	izpishi('Kude li sa Pesho i Gosho')          # print
inache:                                          # else
	ne_znam = vqrno                              # vqrno -> False, nevqrno -> True

# BTW the tabs are important... Just sayin'
# And they have to tabs tabs, not spaces
```
Loops:
```eibgu
za l v obseg(30):              # for l in range(30)
	izpishi(l)

broqch = 0
dokato vqrno:                  # while True
	ako broqch e 31:
		preskochi              # continue
    ako li puk broqch e 100:
		schupi                 # break
    inache:
		izpishi(broqch)
```
Functions:
```eibgu
kato izvikam kvo_staa(na_kef_sum):       # def kvo_staa(na_kef_sum):
	globalni nqkva_globalna_promenliva   # global nqkva_globalna_promenliva
	ako na_kef_sum e vqrno:
		izpishi('Na kef sum')
    inache:
		vurni                             # return
```
Comments:
```eibgu
# Az sum komentar
```
Random:
```eibgu
sluchaino(0, 9)  # random.randint(0, 9)
```

## The cool stuff
Here you can find all the gamemaking EBIGU actions

### Initializing the game

Initialize new game and set the window size (compulsory):
```eibgu
prozorcheto da mi bude (width, height)
```
Set window icon:
```eibgu
ikonkata da mi bude ./path/to/icon.png
```
Set window caption (title):
```eibgu
igrata mi se kazva 'Nai qkata igra na zemqta'
```
Set desired fps:
```eibgu
# Default is 30 (you don't really need to set this)
nadqvam se igrata mi da vurvi s 60 fps
```
Set background (colors can be either in hex or rgb values):
```eibgu
fonut da mi bude ./path/to/background.jpg
fonut da mu bude #ffffff
```

### Ifs and checkers
! Every one of these has to be in the "osnoven cikul" aka the main game loop

Check if mouse has been clicked:
```eibgu
ako mishkata e cuknata:
	...
```
Check if the mouse is currently in motion:
```eibgu
ako mishkata murda:
	...
```
Check if the button specified has been clicked:
```eibgu
ako nqkuv_qk_buton e kliknat:
	...
```
Check if a certain key is pressed:
(you can find the full list of key names [here](https://www.pygame.org/docs/ref/key.html))
```eibgu
ako K_UP e natisnat:
	...
```
Collision detection between two sprites (aka heroes):
```eibgu
ako sprite1 se blusne s sprite2:
	...
```
Collision detection between a sprite and a group of sprites:
```eibgu
ako sprite se blusne s neshto ot group:
	...
```
Check if a sprite (aka hero) is outside the window boundaries:
```eibgu
ako sprite izleze ot poleto:
	...
```
Check if an event is happening:
```eibgu
ako subitie NQKAKVO_SUBITIE:
	...
```
Create a new hero object (sprite):
```eibgu
igrach = nov geroi s golemina (width, height) i sprite ./path/to/player.png
krugche= nov geroi s golemina (width, height) i sprite krugche i cvqt #d8f83f
# default color is #ffffff so it is not a compulsory parameter
pravougulniche = nov geroi s golemina (width, height) i sprite pravougulniche
```
Create a new font object (needed for buttons and texts):
```eibgu
fontche = nov font ./path/to/fontche.ttf s golemina 40
```
Create a new text object:
```eibgu
krai_text = nov text 'Krai na igrata' s font fontche i cvqt #ffffff
```
Create a new button object:
```eibgu
igrai_buton = nov buton 'Igrai' s cvqt #ffffff i fonov cvqt #000000 i cvqt #0f0f0f pod kursora i font fontche i golemina (width, height)
```
Create a new event:
```eibgu
# Always has to be in uppercase
NOVO_SUBITIE = novo subitie
```

### Audio
Load a new sound:
```eibgu
lazer_zvuk = nov zvuk ./path/to/lazer.wav
```
Play sound:
```eibgu
izpei lazer_zvuk
```
Set sound volume:
```eibgu
izpeivai lazer_zvuk s 0.5 zvuk
```
Play music (looped):
```eibgu
pei ./path/to/muzichka.mp3
```
Set the music volume:
```eibgu
pei s 1.3 zvuk
```
Pause the music:
```eibgu
pauzirai peeneto
```
Unpause the music:
```eibgu
otpauzirai peeneto
```
Stop the music:
```eibgu
q zemi se sopri s tva tvoe peene
```

### Manipulating the sprites (hero objects)
Draw a sprite:
```eibgu
plesni igrach na (x, y)
```
Remove a sprite:
```eibgu
mahni igrach
```
Move a sprite to a certain location:
```eibgu
mrudni igrach na (x, y)
```
Move a sprite by some pixels:
```eibgu
mrudni igrach s (x, y)
```
Change size of a sprite:
```eibgu
napravi igrach (width, height)
```
Rotate sprite:
```eibgu
zavurti igrach s 90 gradusa
```

### Some useful get actions
Get current mouse position (works only in "osnoven cikul"):
```eibgu
poz_mishka = poziciq na mishkata
```
Get the position of a sprite:
```eibgu
poz_igrach = poziciq na igrach
```
Get the size of a sprite:
```eibgu
golemina_igrach = golemina na igrach
```

### Animations
Add an animation to a sprite (the sprite has to be first "plesnat" (drawn)):
```eibgu
# The folder has to consist of the animation's images only
# and they should be numbered in the right order
igrach_animaciq = nova animaciq na igrach ot ./path/to/folder
```
Play animation:
```eibgu
animirai igrach_animaciq na igrach
```
Play animation on a whole group:
```eibgu
animirai vrag_animaciq na grupa vragove
```

### Sprite groups
- used to store multiple sprites in the same place for ease

Create a new sprite group:
```eibgu
vragove = nova grupa
```
Add to group (and draw):
```eibgu
dobavi vrag v vragove i go plesni na (x, y)
```
Remove from group:
```eibgu
mahni vrag ot vragove
```
Empty a group:
```eibgu
izprazni grupa vragove
```

### Other useful actions
Post an event after a given amount of milleseconds:
```ebigu
sled 1000 ms NOVO_SUBITIE
```
Post an event every n amount of milleseconds:
```ebigu
prez 2000 ms RODI_VRAG
```
Start counting the elapsed time (the izminalo_vreme var):
```ebigu
# All the clock actions work only in the "osnoven cikul" aka the main game loop
# Also by default the clock is not counting
pusni chasovnika
```
Pause the counting of elapsed time:
```ebigu
pauzirai chasovnika
```
Reset the counting of elapsed time:
```ebigu
nulirai chasovnika
```
Show the cursor:
```ebigu
pokazhi kursora
```
Hide the cursor:
```ebigu
skrii kursora
```

### The main game loop function
```ebigu
osnoven cikul:
	...
```

### Quit game
Can only be used in the main game loop
```ebigu
krai na igrata
```

### End of EBIGU file (when making a game):
! Compulsory
```ebigu
# This is the final line of my beautiful game!
dobra igra
```

### Special variables
Screen width and height:
```ebigu
SHIRINA_EKRAN    # -> gives you the width of the screen
VISOCHINA_EKRAN  # -> gives you the height of the screen
```
Center of the screen:
```ebigu
CENTER  # -> [centerx, centery]
```
The set fps:
```ebigu
FPS  # -> a number (what you have set or the default 30)
```
Time elapsed since you started the clock:
```ebigu
# Can only be accessed from the "osnoven cikul"
izteklo_vreme  # -> gives you the number of seconds elapsed since the clock was started
```
Time elapsed between each loop in the "osnoven cikul" aka the main game loop:
```ebigu
# Can only be accessed from the "osnoven cikul"
dt  # -> gives you the number of seconds elapsed between each loop
```

Feel free to add more features and happy codin'!
