def riesenie():
    pocet = 0
    for s in range(5,10):
        for a in range(10):
            if a == s:
                continue
            for g in range(10):
                if g == s or g == a:
                    continue
                for o in range(10):
                    if o == s or o == a or o == g:
                        continue
                    for n in range(10):
                        if n == s or n == a or n == g or n == o:
                            continue
                        for f in range(10):
                            if f == s or f == a or f == g or f == o or f == n:
                                continue
                            for e in range(10):
                                if e == s or e == a or e == g or e == o or e == n or e == f:
                                    continue
                                for l in range(10):
                                    if l == s or l == a or l == g or l == o or l == n or l == f or l == e:
                                        continue
                                    for i in range(10):
                                        if i == s or i == a or i == g or i == o or i == n or i == f or i == e or i == l:
                                            continue
                                        for c in range(10):
                                            if c == s or c == a or c == g or c == o or c == n or c == f or c == e or c == l or c == i:
                                                continue
                                            sag = s * 1000 + a * 100 + g * 10 + o
                                            san = s * 1000 + a * 100 + n * 10 + o
                                            felic = f * 10000 + e * 1000 + l * 100 + i * 10 + c
                                            if sag + san == felic:
                                             
                                                pocet+=1
                                                print(f"SAGO = {s}{a}{g}{o} + SANO = {s}{a}{n}{o} = FELIC = {f}{e}{l}{i}{c}")
    print(f'Počet riešení je: {pocet}')                                            
riesenie()