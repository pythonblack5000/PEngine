import pygame
pygame.init()
debug = False


def FileLoad(File="", font_size=14):
    extension = File[-3:]
    if(debug):
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


def ClearScreen(screenforbg ,r, g, b):
    return screenforbg.fill((r, g , b))

def FPSLimit(fps):
    clock = pygame.time.Clock()
    clock.tick(fps)

def SoundPlay(soundfile_FLonly, volumef=1):
    soundfile_FLonly.set_volume(volumef)
    soundfile_FLonly.play()




def UpdateScreen():
    pygame.display.flip()

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
    def __init__(self,imgfile,scalef,damagef=0):
        self.image = imgfile
        self.rect = self.image.get_rect()
        self.scale = scalef
        self.image = pygame.transform.scale(self.image, (self.scale, self.scale))
        self.damage = damagef


class Map_Manager:#author ivan.exe#8051
    def __init__(self,screen_data=[800,600],map_data=[2400,900],map_speed=3,move=True):
        self.screen_data = screen_data
        self.map_data = map_data
        self.map_speed = map_speed
        self.map_pos = [0,0]
        self.move = move

    def calc_pos(self,pos=[0,0],type_='+'):
        x, y = self.map_pos
        if type_=='+': # используй это для блоков, кубиков и так далее.
            return([ pos[0]+x, pos[1]+y ])
        elif type_=='-': # используй это например для: отображения позиции мишки на карте.
            return([ pos[0]+-x, pos[1]+-y ])
    
    def calc_x(self,px=0): x = self.map_pos[0]; return( px+x )
    def calc_y(self,py=0): y = self.map_pos[1]; return( py+y )

    def get_map(self,ind=None):
        if ind != None: return(self.map_data[ind])
        else: return(self.map_data)

    def get_screen(self,ind=None): 
        if ind != None: return(self.screen_data[ind])
        else: return(self.screen_data)
        
    def set_map(self,map_): self.map_data = map_

    def move_map(self):
        if self.move and (self.map_data[0] > self.screen_data[0] or self.map_data[1] > self.screen_data[1]):
            keys = pygame.key.get_pressed()

            if keys[pygame.K_a] and (not keys[pygame.K_d]):
                if self.map_pos[0]+self.map_speed <= 0: self.map_pos[0] += self.map_speed
                else: self.map_pos[0] = 0

            if keys[pygame.K_d] and (not keys[pygame.K_a]):
                if -(self.map_pos[0])+self.screen_data[0]+self.map_speed <= self.map_data[0]-1: self.map_pos[0] -= self.map_speed
                else: self.map_pos[0] = -(self.map_data[0]-self.screen_data[0])

            if keys[pygame.K_w] and (not keys[pygame.K_s]):
                if self.map_pos[1]+self.map_speed <= 0: self.map_pos[1] += self.map_speed
                else: self.map_pos[1] = 0

            if keys[pygame.K_s] and (not keys[pygame.K_w]):
                if -(self.map_pos[1])+self.screen_data[1]+self.map_speed <= self.map_data[1]-1: self.map_pos[1] -= self.map_speed
                else: self.map_pos[1] = -(self.map_data[1]-self.screen_data[1])