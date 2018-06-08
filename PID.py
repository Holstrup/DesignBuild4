def TempPID(measuredTemp, pastError, integralTerm):
    desiredTemp = 17 # Target Temperature
    deltaT = 1
    
    P = 1
    I = 1
    D = 0.3

    currentError = desiredTemp - measuredTemp

    integralTerm = (sum(integralTerm))*deltaT
    derivativeTerm = (currentError - pastError)/deltaT
    
    
    PID_out = P*currentError + I*integralTerm + D*derivativeTerm
    pastError = currentError
    return (PID_out, pastError, integralTerm)


