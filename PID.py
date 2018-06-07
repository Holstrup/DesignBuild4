# -*- coding: utf-8 -*-

# PYTHON PID

def TempPID(measuredTemp, pastError, integralTerm):
    desiredTemp = 19 # Target Temperature
    deltaT = 1
    
    P = 1
    I = 0.2
    D = 0.3
    
    currentError = desiredTemp - measuredTemp
    integralTerm = integralTerm + currentError*deltaT  
    derivativeTerm = (currentError - pastError)/deltaT
    
    
    PID_out = P*currentError + I*integralTerm + D*derivativeTerm
    pastError = currentError
    return (PID_out, pastError, integralTerm)

