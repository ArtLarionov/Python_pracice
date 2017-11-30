import re

print(re.match)  # берет строку и шаблон и проверяет: подходит ли строка под наш шаблон
print(re.search)  # берет нашу строку и выводит первую подстроку, которая подходит под наш шаблон
print(re.findall)  # находит все подстроки, которые подходят под наш шаблон
print(re.sub)  # позволит заменить все вхождения подстрок чем-нибудь другим
print()

pattern = r"abc"
string = "abc"
match_object = re.match(pattern, string)
print(match_object)
print()

# [] - можно указать множество подходящих символов(метасимволы)
# . ^ $ * + ? { } [ ] \ | ( ) -- метасимволы

# можем написать [a-zA-Z]
# [^a-z] - нам не подходят символы от a до z
# \d ~ [0-9]
# \D ~ [^0-9]
# \s ~ [ \t\n\r\f\v] -- пробельные символы
# \S ~ [^ \t\n\r\f\v]
# \w ~ [a-zA-Z0-9_] -- буквы + цифры + _
# \W ~ [^a-zA-Z0-9_]
# r"a.c" -- мы бы наши все сочетания, которые начинаются на а, заканчиваются на с
pattern = r"a[abc]c"  # можем написать [a-c]
string = "abc"  # строки aac, abc, acc - будут подходить под шаблон
match_object = re.match(pattern, string)
print(match_object)
print()


string = "abc, acc, aac"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
print()


fixed_typos = re.sub(pattern, "abc", string)
print(fixed_typos)


