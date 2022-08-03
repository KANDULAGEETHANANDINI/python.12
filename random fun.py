import re
txt = "use of python in machine Learning"
x = re.search("^use.*Learning$", txt)
if(x):
    print("YES! we have a match!")
else:
    print("No match")