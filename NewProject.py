import sys

code = """import PEngine.TwoD as PE
import pygame

screen = PE.CreateScreen(0,0,True) 

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		PE.ClearScreen(screen, 0,0,0)
		PE.UpdateScreen()

PE.Quit()
"""
if(len(sys.argv) < 2):
	print("ERROR: Type a path for file!")	
	quit()
else:
	f = open(sys.argv[1], "w")
	f.write(code)
	f.close()