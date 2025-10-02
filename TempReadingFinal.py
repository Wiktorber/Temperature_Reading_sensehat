#Import the SennseHat Libraries from the /lib directory. sense_emu is virtual while sense_hat is phyisical.
from sense_hat import SenseHat

#This will initalize a new SenseHat object, allowing changes to be made and to use pre-made function.
sense = SenseHat()

#Colour Values - used for recording the Sense Hat on a phone
Foreground_Colour = (200,0,0) #Red
Background_Colour = (0,0,0) #Black

#Team Members
names = "Group 2 Team members: David Clifford, Wiktor Bernacki, Arunas Strolis, Maoliosa Flynn, Jonathan Dean"

#Infinite Loop
while True:
    
    #Read in temp from the sense object and store in a variable
    temp = sense.temp
    tempRounded = round(temp) #Rounds the int to make an the number easier to read
    tempString = "Temperature: " + str(tempRounded) + " Celcius" #Converts the int value to a string
    
    #Read the Pressure, round and convert to string
    pressure = sense.get_pressure()
    presRounded = round(pressure) 
    presString = "Pressure: " + str(presRounded) + "Pa" 
    
    #Read the humidity, round and convert to string
    humidity = sense.get_humidity()
    humRounded = round(humidity) 
    humString = "Humidity: " + str(humRounded) + "%" 
    
    #Condense all the strings into one, allowing control of formatting
    hatReading = tempString + " " + presString + " " + humString + " " + names
    
    
    sense.show_message(hatReading, scroll_speed=0.07 ,text_colour=Foreground_Colour, back_colour=Background_Colour)  #Adding a name along wi