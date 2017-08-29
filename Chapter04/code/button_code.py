import time
#initialise a previous input variable to 0 (assume button not pressed last)
prev_input = 0
state = 0

while True:
  input = GPIO.input(17)
  input = GPIO.input(27)
  
  if ((not prev_input) and input):
    print("Button pressed")
    if(state == 0):
        state = 1
        // code to play the first playlist
    else:
        state = 0
        // code to play the second playlist
        
  #update previous input
  prev_input = input
  
  #slight pause to debounce
  time.sleep(0.05)

