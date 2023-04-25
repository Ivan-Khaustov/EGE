# РОСОМАХА

count = 0

for a1 in "РСМХ":
    for a2 in "ОА":
        for a3 in "РСМХ":
            for a4 in "ОА":
                for a5 in "РСМХ":
                    for a6 in "ОА":
                        for a7 in "РСМХ":
                            for a8 in "ОА":
                                a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

                                b1 = a.count("Р")
                                b2 = a.count("С")
                                b3 = a.count("М")
                                b4 = a.count("Х")
                                b5 = a.count("А")
                                b6 = a.count("О")

                                if b1 == b2 == b3 == b4 == 1 and b5 == b6 == 2:
                                    count += 1

for a1 in "ОА":
    for a2 in "РСМХ":
        for a3 in "ОА":
            for a4 in "РСМХ":
                for a5 in "ОА":
                    for a6 in "РСМХ":
                        for a7 in "ОА":
                            for a8 in "РСМХ":
                                a = a1 + a2 + a3 + a4 + a5 + a6 + a7 + a8

                                b1 = a.count("Р")
                                b2 = a.count("С")
                                b3 = a.count("М")
                                b4 = a.count("Х")
                                b5 = a.count("А")
                                b6 = a.count("О")

                                if b1 == b2 == b3 == b4 == 1 and b5 == b6 == 2:
                                    count += 1

print(count)