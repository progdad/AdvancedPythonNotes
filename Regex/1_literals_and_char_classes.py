import re


text1 = "Some text with 'map' word and 'port mapping'"
match1 = re.findall("map", text1)  # ['map', 'map']

text2 = "Eats, eats"
match2 = re.findall(r"[Ee]ats", text2)  # ['Eats', 'eats']

text3 = "666 766 566. 866 5g66."
match3 = re.findall(r"[^5]66", text3)  # ['666', '766', '866', 'g66']

text4 = "This is a CS50 course. A year ago it was CS17, two years ago - CS9"
match4_1 = re.findall(r"CS\d\d", text4)  # ['CS50', 'CS17']
match4_2 = re.findall(r"CS\d\d\S", text4)  # ['CS17,']
