import re

pattern = r"(test)*"  # мы ищем повторы слова test
# pattern = r"(test|text)*" -- или test или text///   " | " - ИЛИ
# pattern = r"abc|(test|text)*" -- или abc или ...
string = "testtest"
match = re.match(pattern, string)
print(match)

