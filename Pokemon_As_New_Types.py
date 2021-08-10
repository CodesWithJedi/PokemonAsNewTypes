import pygame
from pygame import mixer
from pygame.locals import *
import random
from os import path
import os
from button import Button

#Initialization
pygame.mixer.pre_init(44100, -16, 2, 512)
mixer.init()
pygame.init()

#Game Variables
Position = pygame.mouse.get_pos()
Width = 1200
Height = 800
Bg = (175, 227, 230)
font = pygame.font.SysFont('Bauhaus 93', 70)
Pokemon = random.randint(1, 151)
Kinds = random.randint(1, 18)
Same = 0
screen = pygame.display.set_mode((Width, Height))
pygame.display.set_caption('Pokemon as New Types! By JediCubing')
screen.fill(Bg)
#Music
pygame.mixer.music.load('Theme.mp3')
pygame.mixer.music.play(-1, 5000)
#Pokemon

#Extra
Plus = pygame.image.load('Other/Plus.png').convert_alpha()
Equals = pygame.image.load('Other/Equals.png').convert_alpha()
Question = pygame.image.load('Other/Question.png').convert_alpha()
Restart = pygame.image.load('Other/Restart.png').convert_alpha()

#Types
Grass = pygame.image.load('Type/1.png')
Fire = pygame.image.load('Type/2.png')
Water = pygame.image.load('Type/3.png')
Electric = pygame.image.load('Type/4.png')
Fairy = pygame.image.load('Type/5.png')
Fighting = pygame.image.load('Type/6.png')
Normal = pygame.image.load('Type/7.png')
Psychic = pygame.image.load('Type/8.png')
Dark = pygame.image.load('Type/9.png')
Dragon = pygame.image.load('Type/10.png')
Bugs = pygame.image.load('Type/11.png')
Flying = pygame.image.load('Type/12.png')
Ghost = pygame.image.load('Type/13.png')
Ground = pygame.image.load('Type/14.png')
Ice = pygame.image.load('Type/15.png')
Poison = pygame.image.load('Type/16.png')
Rock = pygame.image.load('Type/17.png')
Steel = pygame.image.load('Type/18.png')
#Pokemon
Bulbasaur = pygame.image.load('Pokemon/1.png')
Ivysaur = pygame.image.load('Pokemon/2.png')
Venasaur = pygame.image.load('Pokemon/3.png')
Charmander = pygame.image.load('Pokemon/4.png')
Charmeleon = pygame.image.load('Pokemon/5.png')
Charizard = pygame.image.load('Pokemon/6.png')
Squirtle = pygame.image.load('Pokemon/7.png')
Wartortle = pygame.image.load('Pokemon/8.png')
Blastoise = pygame.image.load('Pokemon/9.png')
Caterpie = pygame.image.load('Pokemon/10.png')
Metapod = pygame.image.load('Pokemon/11.png')
Butterfree = pygame.image.load('Pokemon/12.png')
Weedle = pygame.image.load('Pokemon/13.png')
Kakuna = pygame.image.load('Pokemon/14.png')
Beedrill = pygame.image.load('Pokemon/15.png')
Pidgey = pygame.image.load('Pokemon/16.png')
Pidgeotto = pygame.image.load('Pokemon/17.png')
Pidgeot = pygame.image.load('Pokemon/18.png')
Rattatta = pygame.image.load('Pokemon/19.png')
Ratticate = pygame.image.load('Pokemon/20.png')
Spearow = pygame.image.load('Pokemon/21.png')
Fearow = pygame.image.load('Pokemon/22.png')
Ekans = pygame.image.load('Pokemon/23.png')
Arbok = pygame.image.load('Pokemon/24.png')
Pikachu = pygame.image.load('Pokemon/25.png')
Raichu = pygame.image.load('Pokemon/26.png')
Sandshrew = pygame.image.load('Pokemon/27.png')
Sandslash = pygame.image.load('Pokemon/28.png')
Nidorian1 = pygame.image.load('Pokemon/29.png')
Nidorina = pygame.image.load('Pokemon/30.png')
Nidoqueen = pygame.image.load('Pokemon/31.png')
Nidorian2 = pygame.image.load('Pokemon/32.png')
Nidorino = pygame.image.load('Pokemon/33.png')
Nidoking = pygame.image.load('Pokemon/34.png')
Clefairy = pygame.image.load('Pokemon/35.png')
Clefable = pygame.image.load('Pokemon/36.png')
Vulpix = pygame.image.load('Pokemon/37.png')
Ninetails = pygame.image.load('Pokemon/38.png')
Jigglypuff = pygame.image.load('Pokemon/39.png')
Wigglytuff = pygame.image.load('Pokemon/40.png')
Zubat = pygame.image.load('Pokemon/41.png')
Golbat = pygame.image.load('Pokemon/42.png')
Oddish = pygame.image.load('Pokemon/43.png')
Gloom = pygame.image.load('Pokemon/44.png')
Vileplume = pygame.image.load('Pokemon/45.png')
Paras = pygame.image.load('Pokemon/46.png')
Parasect = pygame.image.load('Pokemon/47.png')
Venonat = pygame.image.load('Pokemon/48.png')
Venomoth = pygame.image.load('Pokemon/49.png')
Diglett = pygame.image.load('Pokemon/50.png')
Dugtrio = pygame.image.load('Pokemon/51.png')
Meowth = pygame.image.load('Pokemon/52.png')
Persian = pygame.image.load('Pokemon/53.png')
Psyduck = pygame.image.load('Pokemon/54.png')
Golduck = pygame.image.load('Pokemon/55.png')
Mankey = pygame.image.load('Pokemon/56.png')
Primeape = pygame.image.load('Pokemon/57.png')
Growlithe = pygame.image.load('Pokemon/58.png')
Arcanine = pygame.image.load('Pokemon/59.png')
Poliwag = pygame.image.load('Pokemon/60.png')
Poliwhirl = pygame.image.load('Pokemon/61.png')
Poliwrath = pygame.image.load('Pokemon/62.png')
Abra = pygame.image.load('Pokemon/63.png')
Kadabra = pygame.image.load('Pokemon/64.png')
Alakazam = pygame.image.load('Pokemon/65.png')
Machop = pygame.image.load('Pokemon/66.png')
Machoke = pygame.image.load('Pokemon/67.png')
Machamp = pygame.image.load('Pokemon/68.png')
Bellsprout = pygame.image.load('Pokemon/69.png')
Weepinbell = pygame.image.load('Pokemon/70.png')
Victreebel = pygame.image.load('Pokemon/71.png')
Tentacool = pygame.image.load('Pokemon/72.png')
Tentacruel = pygame.image.load('Pokemon/73.png')
Geodude = pygame.image.load('Pokemon/74.png')
Gravler = pygame.image.load('Pokemon/75.png')
Golem = pygame.image.load('Pokemon/76.png')
Pontya = pygame.image.load('Pokemon/77.png')
Rapidash = pygame.image.load('Pokemon/78.png')
Slowpoke = pygame.image.load('Pokemon/79.png')
Slowbro = pygame.image.load('Pokemon/80.png')
Magnemite = pygame.image.load('Pokemon/81.png')
Magnetron = pygame.image.load('Pokemon/82.png')
Farfetched = pygame.image.load('Pokemon/83.png')
Doduo = pygame.image.load('Pokemon/84.png')
Dodrio = pygame.image.load('Pokemon/85.png')
Seal = pygame.image.load('Pokemon/86.png')
Dewgong = pygame.image.load('Pokemon/87.png')
Grimer = pygame.image.load('Pokemon/88.png')
Muk = pygame.image.load('Pokemon/89.png')
Shelder = pygame.image.load('Pokemon/90.png')
Cloyster = pygame.image.load('Pokemon/91.png')
Gastly = pygame.image.load('Pokemon/92.png')
Haunter = pygame.image.load('Pokemon/93.png')
Gengar = pygame.image.load('Pokemon/94.png')
Onix = pygame.image.load('Pokemon/95.png')
Drowzee = pygame.image.load('Pokemon/96.png')
Hypno = pygame.image.load('Pokemon/97.png')
Krabby = pygame.image.load('Pokemon/98.png')
Kingler = pygame.image.load('Pokemon/99.png')
Voltorb = pygame.image.load('Pokemon/100.png')
Electrobe = pygame.image.load('Pokemon/101.png')
Exeggcute = pygame.image.load('Pokemon/102.png')
Exeggutor = pygame.image.load('Pokemon/103.png')
Cubone = pygame.image.load('Pokemon/104.png')
Marowak = pygame.image.load('Pokemon/105.png')
Hitmonlee = pygame.image.load('Pokemon/106.png')
Hitmonchan = pygame.image.load('Pokemon/107.png')
Lickitung = pygame.image.load('Pokemon/108.png')
Koffing = pygame.image.load('Pokemon/109.png')
Weezing = pygame.image.load('Pokemon/110.png')
Rhyhorn = pygame.image.load('Pokemon/111.png')
Rhydon = pygame.image.load('Pokemon/112.png')
Chansey = pygame.image.load('Pokemon/113.png')
Tangela = pygame.image.load('Pokemon/114.png')
Kangaskhan = pygame.image.load('Pokemon/115.png')
Horsea = pygame.image.load('Pokemon/116.png')
Sedra = pygame.image.load('Pokemon/117.png')
Goldeen = pygame.image.load('Pokemon/118.png')
Seaking = pygame.image.load('Pokemon/119.png')
Staryu = pygame.image.load('Pokemon/120.png')
Starmie = pygame.image.load('Pokemon/121.png')
Mr_Mime = pygame.image.load('Pokemon/122.png')
Scyther = pygame.image.load('Pokemon/123.png')
Jynx = pygame.image.load('Pokemon/124.png')
Electabuzz = pygame.image.load('Pokemon/125.png')
Magmar = pygame.image.load('Pokemon/126.png')
Pinsir = pygame.image.load('Pokemon/127.png')
Tauros = pygame.image.load('Pokemon/128.png')
Magikarp = pygame.image.load('Pokemon/129.png')
Garyados = pygame.image.load('Pokemon/130.png')
Lapras = pygame.image.load('Pokemon/131.png')
Ditto = pygame.image.load('Pokemon/132.png')
Eevee = pygame.image.load('Pokemon/133.png')
Vaporeon = pygame.image.load('Pokemon/134.png')
Jolteon = pygame.image.load('Pokemon/135.png')
Flareon = pygame.image.load('Pokemon/136.png')
Porygon = pygame.image.load('Pokemon/137.png')
Omanyte = pygame.image.load('Pokemon/138.png')
Omastar = pygame.image.load('Pokemon/139.png')
Kabuto = pygame.image.load('Pokemon/140.png')
Kabutops = pygame.image.load('Pokemon/141.png')
Areodactyl = pygame.image.load('Pokemon/142.png')
Snorlax = pygame.image.load('Pokemon/143.png')
Articuno = pygame.image.load('Pokemon/144.png')
Zapdos = pygame.image.load('Pokemon/145.png')
Moltress = pygame.image.load('Pokemon/146.png')
Dratini = pygame.image.load('Pokemon/147.png')
Dragonair = pygame.image.load('Pokemon/148.png')
Dragonite = pygame.image.load('Pokemon/149.png')
Mewtwo = pygame.image.load('Pokemon/150.png')
Mew = pygame.image.load('Pokemon/151.png')

#Lets blit some Extra stuff too First the Plus sign
screen.blit(Plus, (550, 350))
#Now the =
screen.blit(Equals, (900, 350))
#the ?
screen.blit(Question, (1050, 350))
#and lastly the restart button
screen.blit(Restart, (10, 10))

run = True
button = Button(10, 10, Restart, 2)
while run:
	
	if button.draw(screen):
		screen.fill(Bg)
		screen.blit(Plus, (550, 350))
		screen.blit(Equals, (900, 350))
		screen.blit(Question, (1050, 350))
		screen.blit(Restart, (10, 10))
		Pokemon = random.randint(1, 151)
		Kinds = random.randint(1, 18)
	
	#Mega If Statements
	if Kinds == 1:
		screen.blit(Grass, (700, 350))
	elif Kinds == 2:
		screen.blit(Fire, (650, 350))
	elif Kinds == 3:
		screen.blit(Water, (600, 350))
	elif Kinds == 4:
		screen.blit(Electric, (700, 350))
	elif Kinds == 5:
		screen.blit(Fairy, (700, 350))
	elif Kinds == 6:
		screen.blit(Fighting, (700, 350))
	elif Kinds == 7:
		screen.blit(Normal, (700, 350))
	elif Kinds == 8:
		screen.blit(Psychic, (700, 350))
	elif Kinds == 9:
		screen.blit(Dark, (700, 350))
	elif Kinds == 10:
		screen.blit(Dragon, (700, 350))
	elif Kinds == 11:
		screen.blit(Bugs, (700, 350))
	elif Kinds == 12:
		screen.blit(Flying, (700, 350))
	elif Kinds == 13:
		screen.blit(Ghost, (700, 350))
	elif Kinds == 14:
		screen.blit(Ground, (700, 350))
	elif Kinds == 15:
		screen.blit(Ice, (700, 350))
	elif Kinds == 16:
		screen.blit(Poison, (700, 350))
	elif Kinds == 17:
		screen.blit(Rock, (700, 350))
	elif Kinds == 18:
		screen.blit(Steel, (700, 350))
	#Another Mega If Statement
	if Pokemon == 1:
		screen.blit(Bulbasaur, (0, 175))
	elif Pokemon == 2:
		screen.blit(Ivysaur, (0, 175))
	elif Pokemon == 3:
		screen.blit(Venasaur, (0, 175))
	elif Pokemon == 4:
		screen.blit(Charmander, (0, 175))
	elif Pokemon == 5:
		screen.blit(Charmeleon, (0, 175))
	elif Pokemon == 6:
		screen.blit(Charizard, (0, 175))
	elif Pokemon == 7:
		screen.blit(Squirtle, (0, 175))
	elif Pokemon == 8:
		screen.blit(Wartortle, (0, 175))
	elif Pokemon == 9:
		screen.blit(Blastoise, (0, 175))
	elif Pokemon == 10:
		screen.blit(Caterpie, (0, 175))
	elif Pokemon == 11:
		screen.blit(Metapod, (0, 175))
	elif Pokemon == 12:
		screen.blit(Butterfree, (0, 175))
	elif Pokemon == 13:
		screen.blit(Weedle, (0, 175))
	elif Pokemon == 14:
		screen.blit(Kakuna, (0, 175))
	elif Pokemon == 15:
		screen.blit(Beedrill, (0, 175))
	elif Pokemon == 16:
		screen.blit(Pidgey, (0, 175))
	elif Pokemon == 17:
		screen.blit(Pidgeotto, (0, 175))
	elif Pokemon == 18:
		screen.blit(Pidgeot, (0, 175))
	elif Pokemon == 19:
		screen.blit(Rattatta, (0, 175))
	elif Pokemon == 20:
		screen.blit(Ratticate, (0, 175))
	elif Pokemon == 21:
		screen.blit(Spearow, (0, 175))
	elif Pokemon == 22:
		screen.blit(Fearow, (0, 175))
	elif Pokemon == 23:
		screen.blit(Ekans, (0, 175))
	elif Pokemon == 24:
		screen.blit(Arbok, (0, 175))
	elif Pokemon == 25:
		screen.blit(Pikachu, (0, 175))
	elif Pokemon == 26:
		screen.blit(Raichu, (20, 175))
	elif Pokemon == 27:
		screen.blit(Sandshrew, (0, 175))
	elif Pokemon == 28:
		screen.blit(Sandslash, (0, 175))
	elif Pokemon == 29:
		screen.blit(Nidorian1, (0, 175))
	elif Pokemon == 30:
		screen.blit(Nidorina, (0, 175))
	elif Pokemon == 31:
		screen.blit(Nidoqueen, (0, 175))
	elif Pokemon == 32:
		screen.blit(Nidorian2, (0, 175))
	elif Pokemon == 33:
		screen.blit(Nidorino, (0, 175))
	elif Pokemon == 34:
		screen.blit(Nidoking, (0, 175))
	elif Pokemon == 35:
		screen.blit(Clefairy, (0, 175))
	elif Pokemon == 36:
		screen.blit(Clefable, (0, 175))
	elif Pokemon == 37:
		screen.blit(Vulpix, (0, 175))
	elif Pokemon == 38:
		screen.blit(Ninetails, (0, 175))
	elif Pokemon == 39:
		screen.blit(Jigglypuff, (0, 175))
	elif Pokemon == 40:
		screen.blit(Wigglytuff, (0, 175))
	elif Pokemon == 41:
		screen.blit(Zubat, (0, 175))
	elif Pokemon == 42:
		screen.blit(Golbat, (0, 175))
	elif Pokemon == 43:
		screen.blit(Oddish, (0, 175))
	elif Pokemon == 44:
		screen.blit(Gloom, (0, 175))
	elif Pokemon == 45:
		screen.blit(Vileplume, (0, 175))
	elif Pokemon == 46:
		screen.blit(Paras, (0, 175))
	elif Pokemon == 47:
		screen.blit(Parasect, (0, 175))
	elif Pokemon == 48:
		screen.blit(Venonat, (0, 175))
	elif Pokemon == 49:
		screen.blit(Venomoth, (0, 175))
	elif Pokemon == 50:
		screen.blit(Diglett, (0, 175))
	elif Pokemon == 51:
		screen.blit(Dugtrio, (0, 175))
	elif Pokemon == 52:
		screen.blit(Meowth, (0, 175))
	elif Pokemon == 53:
		screen.blit(Persian, (0, 175))
	elif Pokemon == 54:
		screen.blit(Psyduck, (0, 175))
	elif Pokemon == 55:
		screen.blit(Golduck, (0, 175))
	elif Pokemon == 56:
		screen.blit(Mankey, (0, 175))
	elif Pokemon == 57:
		screen.blit(Primeape, (0, 175))
	elif Pokemon == 58:
		screen.blit(Growlithe, (0, 175))
	elif Pokemon == 59:
		screen.blit(Arcanine, (0, 175))
	elif Pokemon == 60:
		screen.blit(Poliwag, (0, 175))
	elif Pokemon == 61:
		screen.blit(Poliwhirl, (0, 175))
	elif Pokemon == 62:
		screen.blit(Poliwrath, (0, 175))
	elif Pokemon == 63:
		screen.blit(Abra, (0, 175))
	elif Pokemon == 64:
		screen.blit(Kadabra, (0, 175))
	elif Pokemon == 65:
		screen.blit(Alakazam, (0, 175))
	elif Pokemon == 66:
		screen.blit(Machop, (0, 175))
	elif Pokemon == 67:
		screen.blit(Machoke, (0, 175))
	elif Pokemon == 68:
		screen.blit(Machamp, (0, 175))
	elif Pokemon == 69:
		screen.blit(Bellsprout, (0, 175))
	elif Pokemon == 70:
		screen.blit(Weepinbell, (0, 175))
	elif Pokemon == 71:
		screen.blit(Victreebel, (0, 175))
	elif Pokemon == 72:
		screen.blit(Tentacool, (0, 175))
	elif Pokemon == 73:
		screen.blit(Tentacruel, (0, 175))
	elif Pokemon == 74:
		screen.blit(Geodude, (0, 175))
	elif Pokemon == 75:
		screen.blit(Gravler, (0, 175))
	elif Pokemon == 76:
		screen.blit(Golem, (0, 175))
	elif Pokemon == 77:
		screen.blit(Pontya, (0, 175))
	elif Pokemon == 78:
		screen.blit(Rapidash, (0, 175))
	elif Pokemon == 79:
		screen.blit(Slowpoke, (0, 175))
	elif Pokemon == 80:
		screen.blit(Slowbro, (0, 175))
	elif Pokemon == 81:
		screen.blit(Magnemite, (0, 175))
	elif Pokemon == 82:
		screen.blit(Magnetron, (0, 175))
	elif Pokemon == 83:
		screen.blit(Farfetched, (0, 175))
	elif Pokemon == 84:
		screen.blit(Doduo, (0, 175))
	elif Pokemon == 85:
		screen.blit(Dodrio, (0, 175))
	elif Pokemon == 86:
		screen.blit(Seal, (0, 175))
	elif Pokemon == 87:
		screen.blit(Dewgong, (0, 175))
	elif Pokemon == 88:
		screen.blit(Grimer, (0, 175))
	elif Pokemon == 89:
		screen.blit(Muk, (0, 175))
	elif Pokemon == 90:
		screen.blit(Shelder, (0, 175))
	elif Pokemon == 91:
		screen.blit(Cloyster, (0, 175))
	elif Pokemon == 92:
		screen.blit(Gastly, (0, 175))
	elif Pokemon == 93:
		screen.blit(Haunter, (0, 175))
	elif Pokemon == 94:
		screen.blit(Gengar, (0, 175))
	elif Pokemon == 95:
		screen.blit(Onix, (0, 175))
	elif Pokemon == 96:
		screen.blit(Drowzee, (0, 175))
	elif Pokemon == 97:
		screen.blit(Hypno, (0, 175))
	elif Pokemon == 98:
		screen.blit(Krabby, (0, 175))
	elif Pokemon == 99:
		screen.blit(Kingler, (0, 175))
	elif Pokemon == 100:
		screen.blit(Voltorb, (0, 175))
	elif Pokemon == 101:
		screen.blit(Electrobe, (0, 175))
	elif Pokemon == 102:
		screen.blit(Exeggcute, (0, 175))
	elif Pokemon == 103:
		screen.blit(Exeggutor, (0, 175))
	elif Pokemon == 104:
		screen.blit(Cubone, (0, 175))
	elif Pokemon == 105:
		screen.blit(Marowak, (0, 175))
	elif Pokemon == 106:
		screen.blit(Hitmonlee, (0, 175))
	elif Pokemon == 107:
		screen.blit(Hitmonchan, (0, 175))
	elif Pokemon == 108:
		screen.blit(Lickitung, (0, 175))
	elif Pokemon == 109:
		screen.blit(Koffing, (0, 175))
	elif Pokemon == 110:
		screen.blit(Weezing, (0, 175))
	elif Pokemon == 111:
		screen.blit(Rhydon, (0, 175))
	elif Pokemon == 112:
		screen.blit(Rhyhorn, (0, 175))
	elif Pokemon == 113:
		screen.blit(Chansey, (0, 175))
	elif Pokemon == 114:
		screen.blit(Tangela, (0, 175))
	elif Pokemon == 115:
		screen.blit(Kangaskhan, (0, 175))
	elif Pokemon == 116:
		screen.blit(Horsea, (0, 175))
	elif Pokemon == 117:
		screen.blit(Sedra, (0, 175))
	elif Pokemon == 118:
		screen.blit(Goldeen, (0, 175))
	elif Pokemon == 119:
		screen.blit(Seaking, (0, 175))
	elif Pokemon == 120:
		screen.blit(Staryu, (0, 175))
	elif Pokemon == 121:
		screen.blit(Starmie, (0, 175))
	elif Pokemon == 122:
		screen.blit(Mr_Mime, (0, 175))
	elif Pokemon == 123:
		screen.blit(Scyther, (0, 175))
	elif Pokemon == 124:
		screen.blit(Jynx, (0, 175))
	elif Pokemon == 125:
		screen.blit(Electabuzz, (0, 175))
	elif Pokemon == 126:
		screen.blit(Magmar, (0, 175))
	elif Pokemon == 127:
		screen.blit(Pinsir, (0, 175))
	elif Pokemon == 128:
		screen.blit(Tauros, (0, 175))
	elif Pokemon == 129:
		screen.blit(Magikarp, (0, 175))
	elif Pokemon == 130:
		screen.blit(Garyados, (0, 175))
	elif Pokemon == 131:
		screen.blit(Lapras, (0, 175))
	elif Pokemon == 132:
		screen.blit(Ditto, (0, 175))
	elif Pokemon == 134:
		screen.blit(Vaporeon, (0, 175))
	elif Pokemon == 135:
		screen.blit(Jolteon, (0, 175))
	elif Pokemon == 136:
		screen.blit(Flareon, (0, 175))
	elif Pokemon == 137:
		screen.blit(Porygon, (0, 175))
	elif Pokemon == 138:
		screen.blit(Omanyte, (0, 175))
	elif Pokemon == 139:
		screen.blit(Omastar, (0, 175))
	elif Pokemon == 140:
		screen.blit(Kabuto, (0, 175))
	elif Pokemon == 141:
		screen.blit(Kabutops, (0, 175))
	elif Pokemon == 142:
		screen.blit(Areodactyl, (0, 175))
	elif Pokemon == 143:
		screen.blit(Snorlax, (0, 175))
	elif Pokemon == 144:
		screen.blit(Articuno, (0, 175))
	elif Pokemon == 145:
		screen.blit(Zapdos, (0, 175))
	elif Pokemon == 146:
		screen.blit(Moltress, (0, 175))
	elif Pokemon == 147:
		screen.blit(Dratini, (0, 175))
	elif Pokemon == 148:
		screen.blit(Dragonair, (0, 175))
	elif Pokemon == 149:
		screen.blit(Dragonite, (0, 175))
	elif Pokemon == 150:
		screen.blit(Mewtwo, (0, 175))
	elif Pokemon == 151:
		screen.blit(Mew, (0, 175))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	
	pygame.display.update()

pygame.quit()
	