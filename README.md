# PEngine
### PEngine - это оболочка для pygame для чайников.
**В модуле два подмодуля 2d и 3d(beta)**

# 2D module
### Импорт подмодуля
```py
import PEngine.2d as PE
#as не обязателен
#но он поможет не писать PEngine.2d.<функция>
```
### После импорта напишите стандартный цикл pygame
```py
import PEngine.2d as PE

screen = PE.CreateScreen(0,0,True) 
#первые два аргумента это x,y 
#а третий полноэкранное ли окно

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
		PE.ClearScreen(screen, 0,0,0) #заливает экран цветом 
		PE.UpdateScreen()

PE.Quit() #выходим из игры
```
# Импорт ресурсов
```py
PlayerImage = PE.FileLoad("//Player.png") #первый аргумент путь до файла
NewTTF = PE.FileLoad("//newFont.ttf", 28) #второй размер шрифта
#(только для шрифтов)
```
**Пока только расширения - wav, mp3, png, jpg, ttf**
