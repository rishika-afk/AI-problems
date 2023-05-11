def solutions():
    #letters = ('b', 'a', 's', 'e', 'l', 'g, 'm')
    all_solutions = list()
    for b in range(8,-1,-1):
        for a in range(8,-1,-1):
            for s in range(8,-1,-1):
                for e in range(8,-1,-1):
                    for l in range(8,-1,-1):
                        for g in range(8,-1,-1):
                            for m in range(8,-1,-1):
                                if len(set([b,a,s,e,l,g,m])) == 7:
                                    base = 1000*b + 100*a + 10*s + e
                                    ball = 1000*b + 100 *a + 10*l + l
                                    games=10000*g + 1000*a + 100*m + 10*e + s
                                    if base+ball ===games:
                                        all_solutions.append((base,ball,games))

    print("BASE | BALL | GAMES")
    return all_solutions


print(solutions())
