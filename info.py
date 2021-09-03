import datetime

now1 = datetime.datetime.now()
strA = str(now1)
time = strA[11:]
hor = time[:-13]
hor = int(hor)
minA = time[3:-10]
minA = int(minA)
now = (f"{hor}:{minA}")

nowTime = (now)
mathsTime     =   ("3:32 pm")
englishTime   =   ("2:39 pm")
hindiTime     =   ("12:15 pm")
chemistryTime =   ("12:15 pm")
physicsTime   =   ("12:15 pm")
biologyTime   =   (now)

demo      =  "https://meet.google.com/zfo-hqtx-dts"

maths     =  ""

english   =  ""

hindi     =  ""

chemistry =  ""

physics   =  ""

biology   =  "https://meet.google.com/xwm-rarx-yrj"

numCheck = 15

waitTime = 3600

joinMessage = "Bot is joinde at the lecture."

leaveMessage = "Bot is leaved from the lecture."

errSms = "Error during leaving lecture."

