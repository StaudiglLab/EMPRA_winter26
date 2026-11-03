"""
Show a very basic program: hello world.

Adapted from psychopy demo
"""

# import key parts of the PsychoPy library:
from psychopy import visual, core

colorOfText='black'


# create a visual window:
win = visual.Window(size=[1400, 800],units="height")

# create (but not yet display) some text:
msg = visual.TextBox2(win, text="Hello!", letterHeight=0.08, color=colorOfText, pos=(0, 0.2)) 

# draw the text to the hidden visual buffer:
msg.draw()

# show the hidden buffer - everything that has been drawn since the last win.flip():
win.flip()

# wait 3 seconds so people can see the message
core.wait(0.5)

# exit gracefully
win.close()
core.quit()
