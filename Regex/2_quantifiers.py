import re

# Default quantifiers
text1 = "Omm Ommmmm Oooommmmmmm"
match1_1 = re.findall(r"[Oo]{1,3}m{2,7}", text1)  # ['Omm', 'Ommmmm', 'ooommmmmmm']
match1_2 = re.findall(r"Om{2}", text1)  # ['Omm', 'Omm']
match1_3 = re.findall(r"[Oo]{1,4}m{3,}", text1)  # ['Ommmmm', 'Oooommmmmmm']
###

# Lazy and greedy quantifiers
text2_1 = "(Several (parentheses) are out there. (Is that good), how do u think ?)"
match2_1_1 = re.findall(r"\(.+\)", text2_1)  # ['(Several (parentheses) out there. (Is that good), how do u think ?)']
match2_1_2 = re.findall(r"\(.+?\)", text2_1)  # ['(Several (parentheses)', '(Is that good)']

text2_2 = "<div>HTML block <img src='image.jpg'> with two images. <img></div>"
match2_2_1 = re.findall(r"<img.*>", text2_2)  # ["<img src='image.jpg'> with two images. <img></div>"]
match2_2_2 = re.findall(r"<img.*?>", text2_2)  # ["<img src='image.jpg'>", '<img>']
# OR
find_img_tag = re.findall(r"<img\s+[^>]*?src\s*=\s*[^>]+>", text2_2)  # ["<img src='image.jpg'>"]
###

# *, +, ?
text3 = "author = Prytula Serhiy; Bayraktars=True; quantity     =       4; price =600mln UA; error=; hello=;"
match3_1 = re.findall(r"\w+\s*=\s*[^;]+", text3)  # ['author = Prytula Serhiy', 'Bayraktars=True', 'quantity     =       4', 'price =600mln UA']
match3_2 = re.findall(r"\w+\s*=\s*[^;]*", text3)  # ['author = Prytula Serhiy', 'Bayraktars=True', 'quantity     =       4', 'price =600mln UA', 'error=', 'hello=']
###
