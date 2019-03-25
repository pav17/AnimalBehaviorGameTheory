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

    print("Total resident payoff: " , sum(residentPayoffList), "for an average payoff of: ", sum(residentPayoffList)/n)
    print("Total mutant payoff: " , sum(mutantPayoffList), "for an average payoff of: ", sum(mutantPayoffList)/n)

    situation1Count = endSituationList.count(1)
    situation2Count = endSituationList.count(2)
    situation3Count = endSituationList.count(3)
    situation4Count = endSituationList.count(4)
    situation5Count = endSituationList.count(5)
    situation6Count = endSituationList.count(6)
    situation7Count = endSituationList.count(7)
    situation8Count = endSituationList.count(8)
    situation9Count = endSituationList.count(9)
    situation10Count = endSituationList.count(10)
    situation11Count = endSituationList.count(11)
    situation12Count = endSituationList.count(12)
    situation13Count = endSituationList.count(13)
    situation14Count = endSituationList.count(14)

    print("Both detected, both signaled, and the predator attacked", situation1Count, "times.")
    print("Both detected, both signaled, and the predator didn't attack", situation2Count, "times.")
    print("Both detected, resident signaled, and the predator attacked", situation3Count, "times.")
    print("Both detected, resident signaled, and the predator didn't attack", situation4Count, "times.")
    print("Both detected, mutant signaled, and the predator attacked", situation5Count, "times.")
    print("Both detected, mutant signaled, and the predator didn't attack", situation6Count, "times.")
    print("Both detected, neither signaled, and the predator attacked", situation7Count, "times.")
    print("Resident detected, resident signaled, and the predator attacked", situation8Count, "times.")
    print("Resident detected, resident signaled, and the predator didn't attack", situation9Count, "times.")
    print("Resident detected, resident didn't signal, and the predator attacked", situation10Count, "times.")
    print("Mutant detected, mutant signaled, and the predator attacked", situation11Count, "times.")
    print("Mutant detected, mutant signaled, and the predator didn't attack", situation12Count, "times.")
    print("Mutant detected, mutant didn't signal, and the predator attacked", situation13Count, "times.")
    print("Neither detected, neither signaled, and the predator attacked", situation14Count, "times.")


Main(60,30,20,30,50,50,50)
