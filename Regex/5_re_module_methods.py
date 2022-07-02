import re


text = "color: #000; font-size: 30px; background: #FA43E9;"

# "re.search" method saves only first match.
match1 = re.search(r"\b([\w-]+)\s*:\s*(#[0-9a-zA-Z]{3,6});", text)
print(match1.groups())  # ('color', '#000')
print(match1.group(0))  # color: #000;
print(match1.group(1))  # color
print(match1.group(2))  # #000
print(match1.group(0, 1, 2))  # ('color: #000;', 'color', '#000')
print(match1.lastindex)  # ('color: #000;', 'color', '#000')
print(match1.start(1), match1.end(1), ' --- ', match1.span(1))  # 0 5  ---  (0, 5)
print(match1.start(2), match1.end(2), ' --- ', match1.span(2))  # 7 11  ---  (7, 11)
print(match1.pos, match1.endpos)  # 0 50
print(match1.re)  # re.compile('\\b([\\w-]+)\\s*:\\s*(#[0-9a-zA-Z]{3,6});')
print(match1.string)  # color: #000; font-size: 30px; background: #FA43E9;

# We can work with groups as with python dicts.
match2 = re.search(r"\b(?P<style>[\w-]+)\s*:\s*(?P<value>#[0-9a-zA-Z]{3,6});", text)
print(match2.groupdict())  # {'style': 'color', 'value': '#000'}
print(match2.lastgroup)  # value
print(match2.expand(r"Style '\g<style>' has value '\g<value>'"))  # Style 'color' has value '#000'
#####

# "re.finditer" is an iterator, that saves all the matches. 
# And for each object in the iterator we can use the same methods as we used with "re.search"
matches = re.finditer(r"\b(?P<style>[\w-]+)\s*:\s*(?P<value>#[0-9a-zA-Z]{3,6});", text)
print(matches, iter(matches) is matches)  # <callable_iterator object at 0x7fc93b56b6a0> True

for match in matches:
    print(match)
    # <re.Match object; span=(0, 12), match='color: #000;'>
    # <re.Match object; span=(30, 50), match='background: #FA43E9;'>
    print(match.groups())
    # ('color', '#000')
    # ('background', '#FA43E9')
