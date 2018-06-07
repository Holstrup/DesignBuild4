import time
import numpy as np
#////////////////////////////////////////////////////////////////////////////
class PID:
    def __init__(self, P=0.2, I=0, D=0):

        self.Kp = P    # constant proportional
        self.Ki = I    # constant integral
        self.Kd = D    # constant derivative
        self.interval = 0.00    # interval is the sampling time
        self.current_time = time.time() # calculate the current time
        self.last_time = self.current_time  # calculate last time we checked
        self.clear()                  # clear

    def clear(self):
        self.SetPoint = 19       # our theoretical set point is 0
        self.PTerm = 0.0             # so is all our term
        self.ITerm = 0.0             # init is only called once  
        self.DTerm = 0.0
        self.last_error = 0.0       # we have no last erroe yet
        self.output = 0.0       

    def update(self, feedback_value):
        
        # update error        
        error = self.SetPoint - feedback_value  
        
        self.current_time = time.time()
        delta_time = self.current_time - self.last_time
        delta_error = error - self.last_error

        if (delta_time >= self.interval):  # compare to interval time
            self.PTerm = self.Kp * error    #Pterm
            self.ITerm += error * delta_time  # integral time

            

            self.DTerm = 0.0
            if delta_time > 0:
                self.DTerm = delta_error / delta_time  # derivative term

            # Remember last time and last error for next calculation
            self.last_time = self.current_time
            self.last_error = error

            self.output = self.PTerm + (self.Ki * self.ITerm) + (self.Kd * self.DTerm)

    def setKp(self, proportional_gain):
        self.Kp = proportional_gain

    def setKi(self, integral_gain):
        self.Ki = integral_gain

    def setKd(self, derivative_gain):
        self.Kd = derivative_gain


    def setSampleTime(self, interval):
       self.interval = interval
 #//////////////////////////// end of class PID ////////////////////////////////////
pid = PID()

feedback = np.array([25,23,22,21,20])

for x in range(np.size(feedback)):
    pid.update(feedback[x])
    print("last error : " ,pid.last_error) 
    print("*******************")
    print("prop term : " ,pid.PTerm) 
    print("integral term : " ,pid.ITerm) 
    print("derivative term : " ,pid.DTerm) 
    print("*******************")
    print("PID output",pid.output) 
       


  


    