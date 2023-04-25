a = "0" + "221" * 23 + "0"

while "00" not in a:
    a = a.replace("011", "20", 1)
    a = a.replace("022", "10", 1)
    a = a.replace("01", "220", 1)
    a = a.replace("02", "110", 1)

print(a, a.count("1"),  a.count("2"))

