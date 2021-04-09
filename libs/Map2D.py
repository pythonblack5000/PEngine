#author ivan.exe#8051
class Map_Manager:
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

