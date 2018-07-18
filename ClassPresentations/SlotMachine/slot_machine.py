import Tkinter as tk
import random
import os.path
from time import sleep
from PIL import ImageTk, Image

directory = os.path.dirname(os.path.abspath(__file__))
def full( fname ):
    return os.path.join( directory, fname )

# Main window
window = tk.Tk()
window.wm_title("Slot machine")

window.geometry("415x460")

# Load all icons as a single image
slot_icons = Image.open(full("slot-machine-icon-vector.jpg"))
background_image = ImageTk.PhotoImage( Image.open(full("red-slot-machine.jpg")))

# calculate start positions of each icon in slot_icons image
# These values are specific to the icons image used.
# Each tuple in icon_positions represents the top left coordinate of the icon
icon_positions = []
for y in range(0, 2):
    for x in range(0, 5):
        icon_positions.append( ( 12 + ( x * 137 ), 77 + ( y * 189 ) ) )

# break single image into individual icons
ICON_WIDTH, ICON_HEIGHT = (130, 135)
SLOT_WIDTH, SLOT_HEIGHT = (48, 65)
X, Y = (0, 1)

icons = []
for point in icon_positions:
    image = Image.new( 'RGB', ( SLOT_WIDTH, SLOT_HEIGHT ) )
    temp = slot_icons.crop(
        ( point[X], point[Y], point[X] + ICON_WIDTH, point[Y] + ICON_HEIGHT )
    )
    image.paste( temp.resize(
        (image.width, image.height), Image.ANTIALIAS
    ))
    icons.append( ( image, ImageTk.PhotoImage( image ) ) )

EMPTY_MESSAGE = "---"

# model
# slots list holds value of each of the three slot windows;
# initialize each to a random icon
LAST_ICON_IDX = len( icons ) - 1
slots = [
    random.randint( 0, LAST_ICON_IDX ),
    random.randint( 0, LAST_ICON_IDX ),
    random.randint( 0, LAST_ICON_IDX ),
]

# controller
MIN_TICKS, MAX_TICKS = (300, 400)
def pull_lever():
    msg.set( EMPTY_MESSAGE )
    playButton.config( state = 'disabled' )
    cycle( random.randint( MIN_TICKS, MAX_TICKS ), 0, [ 3, 2, 1 ] )
    playButton.config( state = 'normal' )

SLOT_COUNT = len(slots)
def cycle(total_ticks, current_tick, speeds):
    # check each slot
    for i in range( 0, SLOT_COUNT ):
        # the following logic determines how many ticks each slot should run
        # (1st runs for 1/2 of total ticks, second runs for 3/4 of total ticks,
        # and third runs for all ticks). It also controls the speed of each slot.
        ticks_for_slot = total_ticks * ( i + 2 ) / (SLOT_COUNT+1)
        slow_down = current_tick > total_ticks * ( i + 2 ) / 11
        if current_tick < ticks_for_slot and current_tick % speeds[i] == 0:
            update_slot( i )
            if slow_down and current_tick % 3 == 0:
                speeds[i] *= 2
    # delay before updating screen and repeating repeating
    sleep(.02)
    canvas.update()
    # update victory status if all ticks have run, and exit method
    if current_tick > total_ticks:
        return updateVictoryStatus()
    # run another cycle
    cycle(total_ticks, current_tick + 1, speeds)

ICON_COUNT = len( icons )
def update_slot(n):
    slots[n] = ( slots[n] + 1 ) % ICON_COUNT
    canvas.itemconfig( slot_image[n], image=icons[ slots[n] ][ 1 ] )

def updateVictoryStatus():
    if all_match(slots):
        msg.set("Holy crap! You won $1,000,000!")
    elif pair_match(slots):
        msg.set("You win a nickel!")
    else:
        msg.set("You get NOTHING!")

def pair_match( items ):
    ok = False
    for i in range( 0, len( items ) ):
        for j in range( i + 1, len( items ) ):
            if items[ i ] == items[ j ]:
                ok = True
    return ok

def all_match(items):
    ok = True
    for i in range( 1, len( items ) ):
        if items[ 0 ] != items[ i ]:
            ok = False
    return ok

# view
canvas = tk.Canvas( window, width = 450, height = 350, background = '#FFFFFF' )
canvas.grid(column = 0,row = 0)
canvas.create_image(0, 0, image=background_image, anchor = tk.NW)

slot_image = []
width=icons[0][0].width + 14
offset=134
for i in range(0, len(slots)):
    slot_image.append(canvas.create_image(
        i*width+offset, 175,
        image = icons[ slots[ i ] ][ 1 ], anchor = tk.NW
    ))

playButton = tk.Button(window, text="Pull Lever!", command=pull_lever)
playButton.grid( row=1, column=0 )

msg = tk.StringVar()
msg.set( EMPTY_MESSAGE )
winOrLose = tk.Label(window, textvariable=msg)
winOrLose.grid( row=2, column=0 )

window.mainloop()
