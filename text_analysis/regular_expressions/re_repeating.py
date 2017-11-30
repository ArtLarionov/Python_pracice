import re

pattern = r"ab*a"  # нас интересует любое число символов b, включая 0
# pattern = r"ab+a" -- нас интересует "+" число символов b, без 0
# pattern = r"ab?a" -- нас интересует 0 или 1 число символов b
# pattern = r"ab{3}a" -- {3}/{2,4}=(от 2 до 4)- число интересующих нас вхождений b
string = "aa, aba, abba, abbba, abbbbbba"
all_inclusions = re.findall(pattern, string)
print(all_inclusions)
