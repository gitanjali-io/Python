#  insatll an external module and use it to perform an operation of your intrest 
import pyttsx3
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('''Hello! Welcome to my Python text-to-speech program.
This program converts written text into spoken words using Python.
I am currently learning Python and exploring different programming concepts.
Every small project I create helps me understand programming better.
Learning to code is not about being perfect; it is about improving one step at a time.
Thank you for listening!''')
engine.runAndWait()
