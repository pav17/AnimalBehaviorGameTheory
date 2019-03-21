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

    residentPayoffList = []
    mutantPayoffList = []
    endSituationList = []

    for x in range(n):
        #print("run")
        residentPayoff, mutantPayoff, endSituation = GI.predPrey(undetectedAttackSuccess, detectedAttackSuccess, costOfSignalling,
        residentSignalChance, mutantSignalChance, detectionProbability, attackProbablility)
        residentPayoffList.append(residentPayoff)
        mutantPayoffList.append(mutantPayoff)
        endSituationList.append(endSituation)
    print("Total resident payoff: " , sum(residentPayoffList))
    print("Total mutant payoff: " , sum(mutantPayoffList))












Main(60,30,20,30,50,50,50)
