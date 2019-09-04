# importing the pyttsx library 
import pyttsx3 

# initialisation 
engine = pyttsx3.init() 

# testing 
engine.say("Arjunram Pal") 
engine.say("Thank you, Paul? Bhai ki jai ho")
engine.say("Thank you for using me!!!")

#engine.say("Can I tell you something just between you and me? When I hear your voice, I know I'm finally free Every single word is perfect as it can be And I need you here with meWhen you lift me up, I know that I'll never falI can speak to you by saying nothing at alEvery single time")
engine.runAndWait()
print("successfully done!!!!!!")
