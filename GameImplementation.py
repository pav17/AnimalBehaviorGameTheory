import random as r

def predPrey(undetectedAttackSuccess, detectedAttackSuccess, detectedAttackChance, costOfSignalling, residentSignalChance, mutantSignalChance):
    if undetectedAttackSuccess < detectedAttackSuccess:
        print("undetectedAttackSuccess must be greater than detectedAttackSuccess")
        sys.exit()

    if costOfSignalling > 0.5:
        print("costOfSignalling must be less than 0.5")
        sys.exit()

    r.seed()
    residentDetect, mutantDetect = Detection(detectionProbability = 40)
    residentSignal, mutantSignal = Signal(residentSignalChance, mutantSignalChance)
    preditorAttack = Attack(attackProbablility = 40)

    if (residentDetect == True and mutantDetect == True):
        if (residentSignal == True and mutantSignal ==True):
            if (preditorAttack == True):
                residentPayoff = 1-(0.5*detectedAttackSuccess)
                mutantPayoff = 1-(0.5*detectedAttackSuccess)
            elif (preditorAttack == False):
                residentPayoff = 1
                mutantPayoff = 1
        elif (residentSignal == True and mutantSignal == False):
            if (preditorAttack == True):
                residentPayoff = 1-((0.5+costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 1-((0.5-costOfSignalling)*detectedAttackSuccess)
            elif (preditorAttack == False):
                residentPayoff = 1
                mutantPayoff = 1
        elif (residentSignal == False and mutantSignal == True):
            if (preditorAttack == True):
                residentPayoff = 1-((0.5-costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 1-((0.5+costOfSignalling)*detectedAttackSuccess)
            elif (preditorAttack == False):
                residentPayoff = 1
                mutantPayoff = 1
        elif (residentSignal == False and mutantSignal == False):
            if (preditorAttack == True):
                residentPayoff = 1-(0.5*detectedAttackSuccess)
                mutantPayoff = 1-(0.5*detectedAttackSuccess)
            elif (preditorAttack == False):
                residentPayoff = 1
                mutantPayoff = 1
    elif (residentDetect == True and mutantDetect == False):
        if (residentSignal == True):
            if (preditorAttack == True):
                residentPayoff = 1-((0.5+costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 1-((0.5-costOfSignalling)*detectedAttackSuccess)
            elif (preditorAttack == False):
                residentPayoff = 1
                mutantPayoff = 1
        elif (residentSignal == False):
            residentPayoff = 1-(0.5*detectedAttackSuccess)
            mutantPayoff = 1-(0.5*undetectedAttackSuccess)
    elif (residentDetect == False and mutantDetect == True):
        if (mutantSignal == True):
            if (preditorAttack == True):
                residentPayoff = 1-((0.5-costOfSignalling)*detectedAttackSuccess)
                mutantPayoff = 1-((0.5+costOfSignalling)*detectedAttackSuccess)
            elif (preditorAttack == False):
                residentPayoff = 1
                mutantPayoff = 1
        elif (mutantSignal == False):
            residentPayoff = 1-(0.5*undetectedAttackSuccess)
            mutantPayoff = 1-(0.5*detectedAttackSuccess)
    elif (residentDetect == False and mutantDetect == False):
        residentPayoff = 1-(0.5*undetectedAttackSuccess)
        mutantPayoff = 1-(0.5*undetectedAttackSuccess)

    print("residentPayoff: ", residentPayoff)
    print("mutantPayoff: ", mutantPayoff)



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
    predPrey(60,30,40,0.2,30,50)
