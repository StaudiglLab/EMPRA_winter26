# import key parts of the PsychoPy library:
from psychopy import visual, core

targetLocation=0.2
targetDisplacement=0.05
fixationDuration=1.0  #in seconds
delayDuration=0.5 #in seconds
blankDuration=0.250 #in seconds

# create a visual window:
win = visual.Window(size=[1400, 800],units="height")


target=visual.Circle(win,fillColor='black',lineColor='black',pos=[0.0,0],radius=0.01,units='height')

target.draw()

win.flip()



#changing target position

core.wait(fixationDuration)
target.setPos([targetLocation,0.0])
target.draw()
win.flip()
core.wait(delayDuration)

win.flip()
core.wait(blankDuration)


target.setPos([targetLocation+targetDisplacement,0.0])
target.draw()
win.flip()

core.wait(3)

#TODO in class: bring circle back to centre and move to left
#TODO in class: demonstrate use of variables.

win.close()
core.quit()