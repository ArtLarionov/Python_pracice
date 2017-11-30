import re

pattern = r" english?"
string = "Do you speak english\?"  # ? знак является метасимволом, поэтому для включения его в поиск необходимо ставить \
match = re.search(pattern, string)
print(match)
