import random as r

def predPrey(undetectedAttackSuccess, detectedAttackSuccess, costOfSignalling,
    residentSignalChance, mutantSignalChance, detectionProbability, attackProbablility):
    if undetectedAttackSuccess < detectedAttackSuccess:
        print("undetectedAttackSuccess must be greater than detectedAttackSuccess")
        sys.exit()

    if costOfSignalling > 50:
        print("costOfSignalling must be less than 50")
        sys.exit()

    r.seed()
    residentDetect, mutantDetect = Detection(detectionProbability)
    residentSignal, mutantSignal = Signal(residentSignalChance, mutantSignalChance)
    preditorAttack = Attack(attackProbablility)

    if (residentDetect == True and mutantDetect == True):
        print("Both detect")
        if (residentSignal == True and mutantSignal ==True):
            print("Both signal")
            if (preditorAttack == True):
                print("predator attacks")
                residentPayoff = 100-(50*detectedAttackSuccess)
                mutantPayoff = 100-(50*detectedAttackSuccess)
                endSituation = 1
            elif (preditorAttack == False):
                print("Predator does not attack")
                residentPayoff = 100
                mutantPayoff = 100
                endSituation = 2
        elif (residentSignal == True and mutantSignal == False):
            print("Resident signals")
            if (preditorAttack == True):
                print("predator attacks")
                residentPayoff = 100-((50+costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 100-((50-costOfSignalling)*detectedAttackSuccess)
                endSituation = 3
            elif (preditorAttack == False):
                print("Predator does not attack")
                residentPayoff = 100
                mutantPayoff = 100
                endSituation = 4
        elif (residentSignal == False and mutantSignal == True):
            print("Mutant signals")
            if (preditorAttack == True):
                print("predator attacks")
                residentPayoff = 100-((50-costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 100-((50+costOfSignalling)*detectedAttackSuccess)
                endSituation = 5
            elif (preditorAttack == False):
                print("Predator does not attack")
                residentPayoff = 100
                mutantPayoff = 100
                endSituation = 6
        elif (residentSignal == False and mutantSignal == False):
            print("Neither signals")
            print("predator attacks")
            residentPayoff = 100-(50*detectedAttackSuccess)
            mutantPayoff = 100-(50*detectedAttackSuccess)
            endSituation = 7
    elif (residentDetect == True and mutantDetect == False):
        print("Resident detects")
        if (residentSignal == True):
            print("Resident signals")
            if (preditorAttack == True):
                print("predator attacks")
                residentPayoff = 100-((50+costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 100-((50-costOfSignalling)*detectedAttackSuccess)
                endSituation = 8
            elif (preditorAttack == False):
                print("Predator does not attack")
                residentPayoff = 100
                mutantPayoff = 100
                endSituation = 9
        elif (residentSignal == False):
            print("Resident does not signal")
            print("predator attacks")
            residentPayoff = 100-(50*detectedAttackSuccess)
            mutantPayoff = 100-(50*undetectedAttackSuccess)
            endSituation = 10
    elif (residentDetect == False and mutantDetect == True):
        print("Mutant detects")
        if (mutantSignal == True):
            print("Mutant signals")
            if (preditorAttack == True):
                print("predator attacks")
                residentPayoff = 100-((50-costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 100-((50+costOfSignalling)*detectedAttackSuccess)
                endSituation = 11
            elif (preditorAttack == False):
                print("Predator does not attack")
                residentPayoff = 100
                mutantPayoff = 100
                endSituation = 12
        elif (mutantSignal == False):
            print("Mutant does not signal")
            print("predator attacks")
            residentPayoff = 100-(50*undetectedAttackSuccess)
            mutantPayoff = 100-(50*detectedAttackSuccess)
            endSituation = 13
    elif (residentDetect == False and mutantDetect == False):
        print("Neither detects/signals")
        print("predator attacks")
        residentPayoff = 100-(50*undetectedAttackSuccess)
        mutantPayoff = 100-(50*undetectedAttackSuccess)
        endSituation = 14

    print("residentPayoff: ", residentPayoff)
    print("mutantPayoff: ", mutantPayoff)

    return(residentPayoff, mutantPayoff, endSituation)



def Detection(detectionProbability):
    detection1 = r.randint(1, 100)
    detection2 = r.randint(1, 100)

    if (detection1 <= detectionProbability):
        residentDetect = True
    else:
        residentDetect = False

    if (detection2 <= detectionProbability):
        mutantDetect = True
    else:
        mutantDetect = False

    return(residentDetect, mutantDetect)

def Attack(attackProbablility):
    attack1 = r.randint(1, 100)

    if (attack1 <= attackProbablility):
        preditorAttack = True
    else:
        preditorAttack = False

    return(preditorAttack)


def Signal(residentSignalChance, mutantSignalChance):
    signal1 = r.randint(1, 100)
    signal2 = r.randint(1, 100)

    if (signal1 <= residentSignalChance):
        residentSignal = True
    else:
        residentSignal = False

    if (signal2 <= mutantSignalChance):
        mutantSignal = True
    else:
        mutantSignal = False

    return(residentSignal, mutantSignal)



if __name__ == "__main__":
    predPrey(60,30,20,30,50,40,40)
