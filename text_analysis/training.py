import re

lst = [str(input()) for line in range(1)]
pattern = r"\b(\w)(\w)"
for line in lst:
    line = line.rstrip()
    result = re.sub(pattern, r"\2\1", line)
    print(result)
