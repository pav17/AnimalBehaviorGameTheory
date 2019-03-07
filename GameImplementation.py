import Random as r

def predPrey():
    r.seed()
    residentDetect, mutantDetect = Detection(detectionProbability = 40)

    if (residentDetect == True and mutantDetect == True):
        if (residentSignal == True and mutantSignal ==True):
            if (preditorAttack == True):
                pass
            elif (preditorAttack == False):
                pass
        elif (residentSignal == True and mutantSignal == False):
            if (preditorAttack == True):
                pass
            elif (preditorAttack == False):
                pass
        elif (residentSignal == False and mutantSignal == True):
            if (preditorAttack == True):
                pass
            elif (preditorAttack == False):
                pass
        elif (residentSignal == False and mutantSignal == False):
            if (preditorAttack == True):
                pass
            elif (preditorAttack == False):
                pass
    elif (residentDetect == True and mutantDetect == False):
        if (residentSignal == True):
            if (preditorAttack == True):
                pass
            elif (preditorAttack == False):
                pass
        elif (residentSignal == False):
           pass
    elif (residentDetect == False and mutantDetect == True):
        if (mutantSignal == True):
            if (preditorAttack == True):
                pass
            elif (preditorAttack == False):
                pass
        elif (mutantSignal == False):
            pass
    elif (residentDetect == False and mutantDetect == False):
        pass




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
