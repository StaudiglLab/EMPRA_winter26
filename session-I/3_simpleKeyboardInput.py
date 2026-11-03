
# import key parts of the PsychoPy library:
from psychopy import visual, core
from psychopy.hardware.keyboard import Keyboard

# create a visual window:
win = visual.Window(size=[1400, 800],units="height")

#creating an object for your keyboard
kb=Keyboard()

#resetting clock to get reaction time
#kb.clock.reset()

msg = visual.TextBox2(win, text="Please press any key", alignment='center',letterHeight=0.08, color='black', pos=(0, 0.2)) 
msg.draw()
win.flip()

# Will wait for a maximum of 10s
key=kb.waitKeys(maxWait=10.0)
keyName=key[0].value
#NOTE: please change the above to key[0].name if you have the older version of pyschopy 



if(keyName=="left"):
    msg.setText("Correct!")
    response="correct"
elif(keyName=="right"):
    msg.setText("Incorrect")
    response="incorrect"
else:
    msg.setText("Invalid")
    response="invalid"
#msg.setText("The key you pressed is: "+keyName)
msg.draw()
win.flip()
core.wait(3)
#TODO in class: show addition of key specific wait
#TODO in class: replace with variables
#TODO in class: first introduction to if statement


win.close()
core.quit()