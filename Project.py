# Per, Kevin, Timothy, and Tom

def predpreysig (signalAttack,trange,stealthKillChance,signalKillChance,signalCost,detectionProbability,predatorTravelTime,predatoHandlingTime):
    """

    b - behaviours signal and attack - signalAttack
    s - prey resident signalling probability - signallingProbability
    a - predator attack probability - attackProbability
    k0 - predator's chance of successfully killing a prey that has not detected it - stealthKillChance
    k1 - predator's chance of successfully killing a prey when there is a signal (whether prey1 or prey2 signals) - signalKillChance
    phi - prey cost of signalling - signalCost
    p - prey probability of detecting predator - detectionProbability
    t - predator travel time - predatorTravelTime
    h - predator handling time - predatoHandlingTime
    """
    signallingProbability = signalAttack[0]
    attackProbability = signalAttack[1]


    ds = (1-detectionProbability)*detectionProbability*(((0.5)*signalKillChance) - attackProbability*signalKillChance*(0.5+signalCost)) + (detectionProbability**2.)*(signallingProbability*(1-(0.5)*attackProbability*signalKillChance) \
            + (1-signallingProbability)*(1-attackProbability*signalKillChance*(0.5+signalCost)) - signallingProbability*(1-attackProbability*signalKillChance*(0.5-signalCost)) - (1-signallingProbability)*(1-signalKillChance*(0.5)))

    if signallingProbability >= 1. and ds > 0.:
            ds = 0.
    if signallingProbability <= 0. and ds < 0.:
        ds = 0.


    da = (signalKillChance*(predatorTravelTime+predatoHandlingTime-(2.*predatoHandlingTime*detectionProbability*signallingProbability))) - (predatoHandlingTime*((((1.-detectionProbability)**2.)*stealthKillChance) + (detectionProbability*signalKillChance*(1.-signallingProbability))  \
             + (detectionProbability*stealthKillChance*(1.-detectionProbability)*(1.-signallingProbability)) + ((detectionProbability**2.)*signallingProbability*signalKillChance)))

    if attackProbability >= 1. and da > 0.:
        da = 0.

    if attackProbability <= 0. and da < 0.:
        da = 0.




    return [ds, da]
