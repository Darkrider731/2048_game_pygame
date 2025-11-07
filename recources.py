import pygame as pg

image_0 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_0.png"
image_2 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_2.png"
image_4 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/test.png"
image_8 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_8.png"
image_16 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_16.png"
image_32 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_32.png"
image_64 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_64.png"
image_128 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_128.png"
image_256 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number 256.jpg"
image_512 = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/number_512.jpg"

you_win = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/win.png"
#you_loose = "C:\\Users\\Refael\\Desktop\\python\\2048_gui\\recource/you_loose.png"
#you_loose
icon = "C:\\Users\\Refael\\OneDrive\\Desktop\\python\\2048_gui\\recource/pic.jpg"


zero = pg.image.load(image_0)
zero = pg.transform.scale(zero, (50,50))

two = pg.image.load(image_2)
two = pg.transform.scale(two, (50,50))

four = pg.image.load(image_4)
four = pg.transform.scale(four, (50,50))

eight = pg.image.load(image_8)
eight = pg.transform.scale(eight, (50,50))

sixteen = pg.image.load(image_16)
sixteen = pg.transform.scale(sixteen, (50,50))

thirty_two = pg.image.load(image_32)
thirty_two = pg.transform.scale(thirty_two, (50,50))

sixty_four = pg.image.load(image_64)
sixty_four = pg.transform.scale(sixty_four, (50,50))

one_twenty_eight = pg.image.load(image_128)
one_twenty_eight = pg.transform.scale(one_twenty_eight, (50,50))

two_fifty_six = pg.image.load(image_256)
two_fifty_six = pg.transform.scale(two_fifty_six, (50,50))

five_twelve = pg.image.load(image_512)
five_twelve = pg.transform.scale(five_twelve, (50,50))

you_win = pg.image.load(you_win)
you_win = pg.transform.scale(you_win, (200, 100))

#you_loose = pg.image.load(you_win)
#you_loose = pg.transform.scale(you_loose, (150, 40))




icon = pg.image.load(icon)