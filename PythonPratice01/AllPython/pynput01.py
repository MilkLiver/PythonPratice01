from pynput.keyboard import Listener
from pynput import mouse
#from pynput.mouse import Button,Controller

def press(key):
    #print(key)
    pass
    
def click(x, y, button, pressed):
    print(x,y,button,pressed)
    pass

def move(x,y):
    #print("position:",x,y)
    pass

def scroll(x, y, dx, dy):
    #print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up',(x, y)))
    print(x,y,dx,dy)

#with Listener(on_press = press) as listener:
#        listener.join()

with mouse.Listener(on_move=move,on_click=click,
                    on_scroll=scroll) as listener:
    listener.join()

