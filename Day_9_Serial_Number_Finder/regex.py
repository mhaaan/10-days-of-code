#####REGEX#####
# CHAR         DESCRIPTION
# /d          numeric digit
# /w          alphanumeric character
# /s          white space
# /D          not a digit
# /W          not alphanumeric
# /S          not a whitespace
# +           appears 1 or more times
# {n}         character is repeated exactly that amount of times
# {n, m}      character is repreated n to m times
# {n,}        from n upwards
# *           0 or more
# ?           appears 1 or 0


import re

text = 'If you need help call 658-598-9977 any time for online help'
pencil = 'pencil'

# search = re.search(pattern, pencil)

help = 'help'
# search = re.search(help, text)
# search = re.findall(help, text)

# for finding in re.finditer(help, text):
#     print(finding.span())

# pattern = re.compile('(\d{3})-(\d{3})-(\d{4})')

# search = re.search(pattern, text)
# print(search.group(2))

# password = input("Password:")
# pattern = r'\D{1}\w{7}'

# check = re.search(pattern, password)
# print(check)

text_1 = 'Saturday and Sunday this store is closed'

search = re.search(r'Sunday|monday', text_1)
print(search)