import pygame
pygame.init()
debug = False
def CreateScreen(xscreen,yscreen):
    return pygame.display.set_mode([xscreen, yscreen])

def FileLoad(File="", font_size=14):
    extension = File[-3:]
    if(debug == True):
    	print("Extension: " + extension)
    if extension == "wav":
        pygame.mixer.init()
        return pygame.mixer.Sound(File)
    if extension == "mp3":
        pygame.mixer.init()
        return pygame.mixer.Sound(File)
    if extension == "png":
        return pygame.image.load(File)
    if extension == "jpg":
        return pygame.image.load(File)
    if extension == "ttf":
        return pygame.font.Font(File, font_size)

def CheckCollision(first_object, second_object, to_bool=True):
	first_rect = first_object.get_rect()
	second_rect = second_object.get_rect()
	if(to_bool == False):
		return first_rect.colliderect(second_rect)
	else:
		if(first_rect.colliderect(second_rect) == 1):
			return True
		else:
			return False


def CreateScreen(xscreen,yscreen, fullscreenf = False):
    if(fullscreenf == False):
        return pygame.display.set_mode([xscreen, yscreen])
    else:
        return pygame.display.set_mode([xscreen, yscreen],pygame.FULLSCREEN)

def Render(screenforrender, img, posx, posy):
    return screenforrender.blit(img, (posx, posy))


def Background(screenforbg ,r, g, b):
    return screenforbg.fill((r, g , b))

def FPSLimit(fps):
    clock = pygame.time.Clock()
    clock.tick(fps)

def SoundPlay(soundfile_FLonly, volumef=1):
    soundfile_FLonly.set_volume(volumef)
    soundfile_FLonly.play()




def UpdateScreen():
    pygame.display.update()

def Quit():
    pygame.quit()

class Player:
    def __init__(self,speedf,imgfile, scalef):
        self.image = imgfile
        self.rect = self.image.get_rect()
        self.speed = speedf
        self.scale = scalef
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))

    def Update(self):
        keys = pygame.key.get_pressed()

        self.rect.x += (keys[pygame.K_d] - keys[pygame.K_a]) * self.speed
        self.rect.y += (keys[pygame.K_s] - keys[pygame.K_w]) * self.speed

class GameObject:
    def __init__(self,imgfile,scalef,damage=0):
        self.image = imgfile
        self.rect = self.image.get_rect()
        self.scale = scalef
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))

