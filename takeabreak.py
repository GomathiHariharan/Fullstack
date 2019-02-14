import webbrowser, time
'''
The aim of this program to alert an employee to a break every 2 hours 3 times 
'''
breakCounter=0
totalBreakNeeded=3
print("program started at", time.ctime())
while breakCounter<totalBreakNeeded:
    time.sleep(10)
    webbrowser.open("https://youtu.be/RmwakhQEjo8")
    breakCounter+=1

print("program ended at", time.ctime())
