#This code takes in text and scrolls it across the Rasperberry Pi Sense Hat using the LEDs

#Imports the SenseHat Libraries, specifying if it is the hat device or emulator 
from sense_emu import SenseHat

#This allows us to write the senseHat in shorthand and allows us to write in commands.
sense = SenseHat()

#This variable will store the string of the group memebers.
names = "Group 2 Team members: David Clifford, Wiktor Bernacki, Arunas Strolis, Maoliosa Flynn, Jonathan Dean"

#Colour Variables
Foreground_Colour = (155,155,90) #Yellow-Green
Background_Colour = (0,0,0) #Lavender

#Allows the code to run continiously as there is no false condition
while True:
    sense.show_message(names, scroll_speed = 0.1, text_colour=Foreground_Colour, back_colour=Background_Colour)
#sense.show_nessage is the function to display text on the Sense Hat
