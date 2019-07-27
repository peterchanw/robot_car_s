import pygame as py

py.init()
# we only need a screen to get access tp the events!
screen = py.display.set_mode((320,240))
py.display.set_caption('The amazing key presser!')

endProgram = False

while not endProgram:
    # pygame event loop
    for e in py.event.get():
        if e.type == py.KEYDOWN:
            if (e.key == py.K_a):
                print ("A was pressed")
            elif (e.key == py.K_b):
                print ("B was pressed")
            elif (e.key == py.K_ESCAPE):
                endProgram = True
            else:
                print ("error - wrong key")

py.display.quit()
py.quit()
