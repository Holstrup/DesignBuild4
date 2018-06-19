

def TempPID(measuredTemp, pastError, integralTerm, desiredTemp, P, I, D):
    deltaT = 1

    currentError = desiredTemp - measuredTemp

    integralTerm = (sum(integralTerm))*deltaT
    derivativeTerm = (currentError - pastError)/deltaT


    PID_out = P*currentError + I*integralTerm + D*derivativeTerm
    pastError = currentError
    return (PID_out, pastError)

