import board
import digitalio
# Configures the internal GPIO
ledR = digitalio.DigitalInOut(board.GP15)
ledR.direction = digitalio.Direction.OUTPUT

ledG = digitalio.DigitalInOut(board.GP16)
ledG.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.GP14)
button.direction = digitalio.Direction.INPUT
button.pull = digitalio.Pull.UP # Sets the internal resistor to pull-up

#define states
state = 0

def R(): #red only
    ledR.value = True
    ledG.value = False
def G(): #green only
    ledR.value = False
    ledG.value = True
def RG(): #red and green
    ledR.value = True
    ledG.value = True

states = {0: R, 1:G, 2:RG}

# Print a message on the serial console
print('Greenhouse Lights Engaged! Use the button to cycle states.')
# Loop so the code runs continuously
while True:
    states[state]()
    if button.value:
        state = state+1 if state < 2 else 0
        while button.value:
            pass


