s = input()
print(s + "es" if s[int(len(s))-1] == "s" else s + "s")