import re

# Base
text1 = "We have several system environment language variables (come up with by myself). " \
        "There are necessary ones: default=EN, local=UA, remote=RO, and some others." \
        "And optional ones as well: bash=EN, null=None"
match1_1 = re.findall(r"(default|local|remote)=[A-Z]{2,3}", text1)    # ['default', 'local', 'remote']
match1_2 = re.findall(r"(?:default|local|remote)=[A-Z]{2,3}", text1)  # ['default=EN', 'local=UA', 'remote=RO']
match1_3 = re.findall(r"((default|local|remote)=[A-Z]{2,3})", text1)  # [('default=EN', 'default'), ('local=UA', 'local'), ('remote=RO', 'remote')]
match1_4 = re.findall(r"(default|local|remote)=([A-Z]{2,3})", text1)  # [('default', 'EN'), ('local', 'UA'), ('remote', 'RO')]
#####

# Find <img ...> tag
text2 = "<div>Again. HTML block <img src={bracket}image.jpg'> with two images. <img></div>"

pattern2_1 = r"<img\s+[^>]*?src\s*=\s*['\"](.+?)['\"].*>"
match2_1_1 = re.findall(pattern2_1, text2.format(bracket="'"))  # ['image.jpg']
match2_1_2 = re.findall(pattern2_1, text2.format(bracket="\""))  # ['image.jpg']  -- that's not valid, because the brackets are different

# To get rid of this flaw, we need the next pattern:
pattern2_2 = r"<img\s+[^>]*?src\s*=\s*(['\"])(.+?)\1.*>"
match2_2_1 = re.findall(pattern2_2, text2.format(bracket="'"))  # [("'", 'image.jpg')]
match2_2_2 = re.findall(pattern2_2, text2.format(bracket="\""))  # []

# Setting custom identifier
match2_3_1 = re.findall(r"<img\s+[^>]*?src\s*=\s*(?P<bracket>['\"])(.+?)(?P=bracket).*>", text2.format(bracket="'"))  # [("'", 'image.jpg')]
#####
