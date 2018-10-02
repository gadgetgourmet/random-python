for c in range(1,100):
    for p in range(1,100):
        for k in range(1,100):
            animals = c + p + k
            if animals == 100:
                price = c*10 + p*3 + k/2
                if price == 100:
                    print("cows=", c, " pigs=", p, " chickens=", k)
print("all done!")
exit(1)
