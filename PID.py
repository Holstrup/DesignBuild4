

def TempPID(measuredTemp, pastError, integralTerm, desiredTemp, P, I, D):
    deltaT = 1

    currentError = desiredTemp - measuredTemp

    integralTerm = (sum(integralTerm))*deltaT
    derivativeTerm = (currentError - pastError)/deltaT


    PID_out = P*currentError + I*integralTerm + D*derivativeTerm
    pastError = currentError
    return (PID_out, pastError)


def odpid(mearsuredOD,pastError,integralTerm,desiredOD,Po,Io,Do):
    deltaT = 1

    currentError = desiredOD - mearsuredOD

    integralTerm = (sum(integralTerm)) * deltaT
    derivativeTerm = (currentError - pastError) / deltaT

    PIDo_out = Po * currentError + Io * integralTerm + Do * derivativeTerm
    pastError = currentError
    return (PIDo_out, pastError)