# hello guys today i will show you how to make a prank virus ;)
# so let's get started 
import os
from gtts import gTTS # my vs code has problem i don't know why (

msg = "You have been Hacked"
language = "en"

obj = gTTS(text=msg, lang=language, slow=False)

obj.save("Virus.mp4")

for i in range(5):
    os.system("mpg321 Virus.mp4")


# basically this program run a mp4 file called Virus.mp4 
# in that file "You have been Hacked" named music will launch 
# this is a prank so this will not harm your computer
# sorry for my bad english and bad quality of video
# source will be available in discription
# Bbye guys ;)