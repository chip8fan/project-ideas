import sys # import sys for one reason
sys.path.pop() # to get rid of external libraries
import tkinter as tk # import tkinter
try: # make sure the program does not use any external libraries
    import requests # by importing requests (which should fail)
    sys.exit() # if the import does not fail the program will exit as this means the program can still access external libs
except ImportError: # if import requests fails
    print("Success!") # success, no external libraries
def evaluate(char): # this deals with button presses
    global input_string # get the input string
    if char != "=": # if = not pressed
        input_string.set(input_string.get()+char) # add the character to input string
    else: # if = pressed
        input_string.set(eval(input_string.get())) # set the input string to the result
root = tk.Tk() # create the root window
root.geometry("512x384") # make it 512*384
root.title("Calculator") # set the title of the window
input_string = tk.StringVar(value="") # input string
output = tk.Label(root, textvariable=input_string) # label to display the input string
output.place(x=0, y=0, width=512, height=128) # place the label in the top third of the screen
characters = [["1", "2", "3", "+"], ["4", "5", "6", "-"], ["7", "8", "9", "*"], [".", "0", "=", "/"]] # loop through these characters
for row in range(len(characters)): # get each row
    for char in range(len(characters[row])): # and each character
        button = tk.Button(root, text=characters[row][char], command=lambda character=characters[row][char]: evaluate(character)) # create a button for each character
        button.place(x=char*128, y=(row*64)+128, width=128, height=64) # and place it
root.mainloop() # this is blocking