# PEngine Documentation

PEngine - это оболочка для pygame для чайников.
В модуле два подмодуля 2d и 3d(beta)

## 2D подмодуль
### Импорт подмодуля
```py
import PEngine.2D as PE
#as PE - не обязателен
#но он поможет не писать PEngine.2D.<функция>(аргументы)
```
### После импорта напишите стандартный цикл pygame
```py
import PEngine.2D as PE

screen = PE.CreateScreen(0,0,True) 
#первые два аргумента это x,y 
#а третий полноэкранное ли окно

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		PE.ClearScreen(screen, 0,0,0) #заливает экран чёрным цветом 
		PE.UpdateScreen()

PE.Quit() #выходим из игры
```
### Импорт ресурсов
```py
import PEngine.2D as PE

PlayerImage = PE.FileLoad("//Player.png") #первый аргумент путь до файла
NewTTF = PE.FileLoad("//newFont.ttf", 28) #второй размер шрифта
#(только для шрифтов)
```
**Пока только расширения - wav, mp3, png, jpg, ttf**

### Классы Player, GameObject и MapManager
#### Player Class
```py
import PEngine.2D as PE

screen = PE.CreateScreen(0,0,True) 
#первые два аргумента это x,y 
#а третий полноэкранное ли окно

PlayerImage = PE.FileLoad("//Player.png") #наша картинка игрока

plr = Player(10, PlayerImage, 1) #создаём объект класса игрока
#первый аргумент - скорость перемещения (да оно встроенное)
#второй - картинка(!ЗАГРУЖЕННАЯ С ПОМОЩЬЮ  FileLoad!)
#третий - размер (1 это оригинальный размер)

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		plr.Update() #обновляем игрока + активируем перемещение (оно на WASD)
		#
		PE.ClearScreen(screen, 0,0,0) #заливает экран чёрным цветом 
		PE.UpdateScreen()

PE.Quit() #выходим из игры
```
#### GameObject Class
```py
import PEngine.2D as PE

screen = PE.CreateScreen(0,0,True) 
#первые два аргумента это x,y 
#а третий полноэкранное ли окно

GMEOBJ_Image = PE.FileLoad("//obj.png") #наша картинка объекта

GMEOBJ = GameObject(PlayerImage, 1, 10) #создаём объект класса объекта
#первый аргумент - картинка объекта(!ЗАГРУЖЕННАЯ С ПОМОЩЬЮ  FileLoad!)
#второй - размер
#а третий - урон(пока бесполезен) 

running = True
while running:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		PE.ClearScreen(screen, 0,0,0) #заливает экран чёрным цветом 
		PE.UpdateScreen()

PE.Quit() #выходим из игры
```
#### MapManager Class
```py
#документация будет позже
```
