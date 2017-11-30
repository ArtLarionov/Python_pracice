print('abc' in 'abcba')
print('abce' in 'abcba')

print("cabcd".find("abc"))  # индекс первого вхождения или -1
print("cabcd".rfind("abc"))  # правосторонний аналог find
print("cabcd"[1:].find("abc"))
print(str.find.__doc__)

print("cabcd".index("abc"))  # индекс первого вхождения или ValueError
print("cabcd".index("aec"))

s = "The man in black fled across the desert, and the gunslinger followed"
print(s.startswith("The man in black"))  # для проверки начаинается ли строка с другой строки
print(s.startswith.__doc__)
print(s.startswith(("The woman", "The dog", "The man in black")))

s = "image.png"
print(s.endswith(".png"))  # заканчивается ли строка на эту строку

s = "abacadabra"
print(s.count("aba"))

s = "1,2,3,4"
print(s.replace(".", ", "))

