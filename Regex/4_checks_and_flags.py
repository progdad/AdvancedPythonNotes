import re


text1 = "quit, qwerty, acquaintance, word, squirrel, qibla"
match1 = re.findall(r"\b\w*q(?=u)\w*\b", text1)  # ['quit', 'acquaintance', 'squirrel']

text2 = """
<!DOCTYPE html>
<html lang="en        ">
<head>
<meta charset = "UTF-8   ">
<title>Title</title>
</head>
<body>
<div class="just-a-link ">
<a href="#">A link</a>    
</div>
<div id="11         р">
<small>Fак</small>
<p>ruZZia[ns]</p>
</div>
</body>
</html>
"""
match2_1 = re.findall(r"([\w-]+)[\t ]*=[\t ]*[\"']([^'\"]+)(?!\s)", text2)  # [('lang', 'en        '), ('charset', 'UTF-8   '), ('class', 'just-a-link '), ('href', '#'), ('id', '11         ')]
match2_2 = re.findall(r"([\w-]+)[\t ]*=[\t ]*[\"']([^'\"]+)(?<!\s)", text2)  # [('lang', 'en'), ('charset', 'UTF-8'), ('class', 'just-a-link'), ('href', '#'), ('id', '11')]

text3 = 'Java JAVASCRIPT java javascript JavaScript Джава ЖС'
match3 = re.findall(r"(?ia)java\w*\b",text3)  # ['Java', 'JAVASCRIPT', 'java', 'javascript', 'JavaScript']
