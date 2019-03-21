import GameImplementation as GI

def Main(undetectedAttackSuccess, detectedAttackSuccess, costOfSignalling,
    residentSignalChance, mutantSignalChance, detectionProbability, attackProbablility):
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
        #print("run")
        GI.predPrey(undetectedAttackSuccess, detectedAttackSuccess, costOfSignalling,
        residentSignalChance, mutantSignalChance, detectionProbability, attackProbablility)

Main(60,30,20,30,50,50,50)
