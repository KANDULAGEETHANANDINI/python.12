#print a list of all matches ("in") from a text
import re
txt = "use of python in machine Learning"
x = re.findall("in", txt)
print(x)