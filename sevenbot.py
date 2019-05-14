import serial
#import config
import warnings
import numpy as np
from threading import Thread,Lock
from time import sleep

NUM_SERVO = 7; #should not be changed
class Flag:
    begin = 0xFE
    status = 0xF5
    speed = 0xF7
    angle = 0xF9
    IK6 = 0xFA
    IK5 = 0xFB
    IK3 = 0xFC
    read = 0xF9
    mask = 0x7F


# Utility functions
def appendTwoByteVal(buf, val):
    buf.append((int(val) // 128) & 0x7F)
    buf.append(int(val) & 0x7F)

def appendVecToSend(buf, vec):
    for el in vec:
        val = int(abs(el)) + (0 if el >= 0 else 1024)
        appendTwoByteVal(buf, val)
   
def constrain(val, valMin, valMax):
    if val < valMin:
        return valMin
    if val > valMax:
        return valMax
    return val

class SevenBot:
    def __init__(self, port_name, baud_rate, timeout=0.1):
        try:
            self.port = serial.Serial(port_name, baud_rate, timeout=0.1);
        except:
            warnings.warn("can't open the serial port to control the robot arm");
            #raise x;

        self.lock_isallconverged = Lock();
        self.isAllConverged = True;
        self.thread_done = False;
        #to be set to control the arm
        self.fluent = np.array([True]*NUM_SERVO, dtype=np.bool);
        self.speed = np.array([50]*NUM_SERVO, dtype=np.int);
        self.angle = np.array([90,115,65,90,90,90,75],dtype=np.float32);
        assert(len(self.angle) == NUM_SERVO);
        self.status = 0;
        self.setForceStatus(1)
        self._doFluentSpeed();
        self._doAngle();
        #read from the arm
        self.rforce = np.array([0]*NUM_SERVO, dtype=np.int);
        self._pos = np.array([0]*NUM_SERVO, dtype=np.float32);
        self.t_read = Thread(target = self._read);
        self.t_read.start()
        while not self.isAllConverged:
            sleep(0.1)
        self._offset = self.angle - self._pos;

    def __del__(self):
        self.thread_done = True
        self.t_read.join()
        self.port.close()
    
    def _do(self, command):
        self.port.write(command)
        self.port.flush()

    def _doFluentSpeed(self):
        s = np.clip(self.speed,0,250)//10;
        s[self.fluent] += 64;
        command = bytes([Flag.begin,Flag.speed] + [Flag.mask & x for x in s]);
        self._do(command)

    def _doAngle(self): 
        with self.lock_isallconverged:
            self.isAllConverged = False
        c = np.array(self.angle * 50/9, dtype = np.int16)
        command = [Flag.begin,Flag.angle]
        for x in c:
            command += [(x//128) & Flag.mask, x & Flag.mask]
        command = bytes(command)
        self._do(command)

    def _read(self):#get force and position, 
        #read bytes
        while True:
            if self.thread_done:
                break
            try:
                while True:
                    c = self.port.read()[0]
                    if c == Flag.begin:
                        c = self.port.read()[0]
                        if c == Flag.read:
                            break
                while self.port.in_waiting<2*NUM_SERVO+1:
                    sleep(0.1)
                data = self.port.read(2*NUM_SERVO+1);
            except:
               continue 
            if data[-1] == 1:
                if not self.isAllConverged:
                    with self.lock_isallconverged:
                        self.isAllConverged = True
            else:
                if self.isAllConverged:
                    with self.lock_isallconverged:
                        self.isAllConverged = False
            for i in range(NUM_SERVO):
                f = data[i*2]>>3;
                # -7 to 7
                self.rforce[i] = (f & 0x07) * (1 if (f>>3)==0 else 0);
                # 0 to 180 degree
                self._pos[i] = (9.0/50)*((data[i*2] & 0x07) * 128 + data[i*2+1]);

    def setForceStatus(self, status):#0-forceless, 1-normal, 2-protected
        if self.status == status:
            return
        else:
            self.status = status
        c = bytes([Flag.begin, Flag.status, Flag.mask & status]);
        self._do(c)

    def setSpeed(self,servo_speed):  #set servo speed , 0-250
        for servo,sp in np.ndenumerate(servo_speed):
            self.speed[servo] = sp;
        self._doFluentSpeed();
    
    def setFluent(self,servo_fluent): #set servo fluent or not, true or false
        for servo,fl in np.ndenumerate(servo_fluent):
            self.fluent[servo] = fl;
        self._doFluentSpeed();

    def setFluentSpeed(self, servo_fluent, servo_speed):
        for servo,sp in np.ndenumerate(servo_speed):
            self.speed[servo] = sp;
        for servo,fl in np.ndenumerate(servo_fluent):
            self.fluent[servo] = fl;
        self._doFluentSpeed();
    
    def setAngle(self,servo_angle): #set servo angles
        if self.status != 1:
            print("can't set angle, not in the correct mode")
            return
        for servo,ang in np.ndenumerate(servo_angle):
            self.angle[servo] = ang;
        ##shoudn't we limit the range of the angels here!!
        self._doAngle();
        
           


    def rangle(self): #get the read angle
        return [x+y for x,y in zip(self._pos, self._offset)];

    
    
    def setIK5(self, j6, vec56, theta5, theta6):
        global isAllConverge
        isAllConverge = False
    
        # 1- Process Data
        j6_c = np.array([constrain(j6[0], -500, 500), constrain(j6[1], -500, 500), constrain(j6[2], -500, 500)])
#        vec56_c = np.copy(vec56)
#        vec56_c /= np.linalg.norm(vec56_c)
#        vec56_c *= 500

    
        sendData = bytearray([0xFE, 0xFB])
        appendVecToSend(sendData, j6_c)
        appendVecToSend(sendData, vec56)
        appendTwoByteVal(sendData, int((theta5*50/9)))
        appendTwoByteVal(sendData, int((theta6*50/9)))    
        # 2- Send Data
        # for dat in sendData:
        #     print("%02X " % dat, end = "")
        self.port.write(sendData)
        self.port.flush()
    
    def setIK6(self, j6, vec56, vec67, theta6):
        global isAllConverge
        isAllConverge = False
    
        # 1- Process Data
        j6_c = np.array([constrain(j6[0], -500, 500), constrain(j6[1], -500, 500), constrain(j6[2], -500, 500)])
#        vec56_c = np.copy(vec56)
#        vec56_c /= np.linalg.norm(vec56_c)
#        vec56_c *= 500
#        vec67_c = np.copy(vec67)
#        vec67_c /= np.linalg.norm(vec67_c)
#        vec67_c *= 500
    
        sendData = bytearray([0xFE, 0xFA])
        appendVecToSend(sendData, j6_c)
        appendVecToSend(sendData, vec56)
        appendVecToSend(sendData, vec67)
        appendTwoByteVal(sendData, int((theta6*50/9)))
    
        # 2- Send Data
        # for dat in sendData:
        #     print("%02X " % dat, end = "")
        self.port.write(sendData)
        self.port.flush()
    
    def disconnect(self):
        self.port.close()
