#import GameImplementation.py as GI

print("How many times?")
while True:
    try:
        n = int(input())
    except ValueError:
        print("Please type a numeric value.")
        print("")
        continue
    else:
        #print("We'll repeat the simulation " + str(n) + " time(s).")
        break

for x in range(n):
    print("run")
    #GI.predPrey()


