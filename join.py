import process as p
import info
from termcolor import colored

def joinTest():
	p.clrscr()
	p.botRimender(info.nowTime)
	print(colored('\n    Joining to Test lecture...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.demo)
	p.checkLeav()
	p.quit()
	p.clrscr()

def joinMaths():
	p.clrscr()
	p.botRimender(info.mathsTime)
	print(colored('\n    Joining to Maths lecture...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.maths)
	p.wait()
	p.endMeet()
	p.quit()
	p.clrscr()

def joinEnglish():
	p.clrscr()
	p.botRimender(info.englishTime)
	print(colored('\n    Joining to English lecture...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.english)
	p.wait()
	p.endMeet()
	p.quit()
	p.clrscr()

def joinHindi():
	p.clrscr()
	p.botRimender(info.hindiTime)
	print(colored('\n    Joining to Hindi lecture...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.maths)
	
	p.wait()
	p.endMeet()
	p.quit()
	p.clrscr()

def joinPhysics():
	p.clrscr()
	p.botRimender(info.physicsTime)
	print(colored('\n    Joining to maths Physics...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.physics)
	p.wait()
	p.endMeet()
	p.quit()
	p.clrscr()

def joinChemistry():
	p.clrscr()
	p.botRimender(info.chemistryTime)
	print(colored('\n    Joining to maths Chemistry...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.chemistry)
	p.wait()
	p.endMeet()
	p.quit()
	p.clrscr()

def joinBiology():
	p.clrscr()
	p.botRimender(info.biologyTime)
	print(colored('\n    Joining to maths Biology...','yellow'))
	p.initBrowser()
	p.login()
	p.attendMeet(info.biology)
	p.wait()
	p.endMeet()
	p.quit()
	p.clrscr()