# RegEx Module

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
y = re.findall("^The.*Spain$", txt)

# The search function

import re

txt = "The rain in Spain"
x = re.findall("Spa", txt)
print(x)
y = re.findall("Portugal", txt)
print(y)
z = re.search("ain", txt)
print(z)
