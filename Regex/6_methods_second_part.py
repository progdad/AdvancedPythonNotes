import re

##########
numbers = "+1(302)207-46-76 +1(333)954-98-02 +380(63)207-54-43 +1(302)902-79-28 +40(755)165-54-66"
# "re.match(pattern, string, flags)" returns a match only if it matches precisely from the first symbol of the string
print(re.match(r"\+1\(302\)\d{3}-\d{2}-\d{2}", numbers))  # <re.Match object; span=(0, 16), match='+1(302)207-46-76'>
print(re.match(r"\+1\(333\)\d{3}-\d{2}-\d{2}", numbers))  # None
###

###
a_dict = "key1:value1; key2:value2, key3: value3;; key4 : value4..."  # No explanation needed :))
print(re.split(r"[\n,;]+", a_dict))  # ['key1:value1', ' key2:value2', ' key3: value3', ' key4 : value4...']
##########

hero_cities = "Mariupol. Bucha. Gostomel. Kharkiv. Kherson. Kyiv."  # Just a small part
##########
# re.sub(pattern, repl, string, count, flags) -- returns new string.
honored = re.sub(r"\s*\b([A-Z][a-z]+).", r"Ukrainian \1 city.\n", hero_cities)
print(honored)
# Ukrainian Mariupol city.
# Ukrainian Bucha city.
# Ukrainian Gostomel city.
# Ukrainian Kharkiv city.
# Ukrainian Kherson city.
# Ukrainian Kyiv city.
###

###
# We can use python functions to fill the text dynamically
def set_id(match):  # match is "re.Match" instance
    set_id.count += 1
    return f'<p id="{set_id.count}">{match.group(1)}</p>\n'

set_id.count = 0
perform_to_html = re.sub(r"\s*\b([A-Z][a-z]+).", set_id, hero_cities)
print(perform_to_html)
# <p id="1">Mariupol</p>
# <p id="2">Bucha</p>
# <p id="3">Gostomel</p>
# <p id="4">Kharkiv</p>
# <p id="5">Kherson</p>
# <p id="6">Kyiv</p>
###

###
# There is also the "re.subn(pattern, repl, string, count, flags)" method,
# that is completely the same as "re.sub", but it also returns a quantity of made substitutions.
##########

##########
# If we need to reuse some pattern more than once, we can compile this pattern with "re.compile(pattern, flags)"
pattern = re.compile(r"\s*\b([A-Z][a-z]+).")  # "re.Pattern" instance is returned
best_cities1 = pattern.subn(r"I love \1 | ", hero_cities)  # ('I love Mariupol | I love Bucha | I love Gostomel | I love Kharkiv | I love Kherson | I love Kyiv | ', 6)
best_cities2 = pattern.sub(r"ruzzians are fertilizer in \1 | ", hero_cities)  # ruzzians are fertilizer in Mariupol | ruzzians are fertilizer in Bucha | ruzzians are fertilizer in Gostomel | ruzzians are fertilizer in Kharkiv | ruzzians are fertilizer in Kherson | ruzzians are fertilizer in Kyiv |
