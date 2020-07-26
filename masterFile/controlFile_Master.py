from time import sleep
import RPi.GPIO as GPIO
import  sqlite3

DIR_VER = 20   # Direction GPIO Pin "Vertical"
STEP_VER = 21  # Step GPIO Pin "Vertical"
DIR_HORI = 19   # Direction GPIO Pin "Horizontal"
STEP_HORI = 26  # Step GPIO Pin "Horizontal"
CW = 1     # Clockwise Rotation
CCW= 0    # Counterclockwise Rotation
SPR = 200   # Steps per Revolution (360 / 1.8)

GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_VER, GPIO.OUT)
GPIO.setup(STEP_VER, GPIO.OUT)
GPIO.setup(DIR_HORI, GPIO.OUT)
GPIO.setup(STEP_HORI, GPIO.OUT)




##def StepMove(X):
##    print(X)
##    step_count = SPR * int(X)
##    delay = .00125    #delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
##    GPIO.output(DIR_VER, CW)
##    GPIO.output(DIR_HORI, CW)
##    for x in range(step_count):
##        GPIO.output(STEP_VER, GPIO.HIGH)
##        GPIO.output(STEP_HORI, GPIO.HIGH)
##        sleep(delay)
##        GPIO.output(STEP_VER, GPIO.LOW)
##        GPIO.output(STEP_HORI, GPIO.LOW)
##        sleep(delay)
##
##
##    sleep(.5)
##    GPIO.output(DIR_VER, CCW)
##    GPIO.output(DIR_HORI, CCW)
##    for x in range(step_count):
##        GPIO.output(STEP_VER, GPIO.HIGH)
##        GPIO.output(STEP_HORI, GPIO.HIGH)
##        sleep(delay)
##        GPIO.output(STEP_VER, GPIO.LOW)
##        GPIO.output(STEP_HORI, GPIO.LOW)
##        sleep(delay)
##
##    #GPIO.cleanup()

def StepMove(xxx):
    locx = xxx[0][1]
    locy = xxx[0][2]
    print(locy)
    print(locx)
    step_count_H = SPR * int(locx)
    step_count_V = SPR * int(locy)
    delay = .00125  # delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
    
    StepClk(step_count_H,step_count_V)

def StepClk(locx,locy):
    print(locx)
    print(locy)
    delay = .00125    #delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
    GPIO.output(DIR_VER, CW)
    GPIO.output(DIR_HORI, CW)
    clk_h = GPIO.HIGH
    clk_v = GPIO.HIGH
    status_h = False
    status_v = False
    while True:
        GPIO.output(STEP_HORI, clk_h)
        GPIO.output(STEP_VER, clk_v)
        sleep(delay)
        GPIO.output(STEP_HORI, GPIO.LOW)
        GPIO.output(STEP_VER, GPIO.LOW)
        sleep(delay)
        
        if locx == 0 :
            clk_h = GPIO.LOW
            status_h = True
        else :
            locx = locx - 1
        
        if locy == 0 :
            clk_v = GPIO.LOW
            status_v = True
        else :
            locy = locy - 1
            
        if status_h == True and status_v == True :
            break


def select_DB(datas):
    xxx = []
    for i in range(len(datas)):
        data = datas[i]
        connection = sqlite3.connect('project_test.db')
        cursor = connection.cursor()
        sql_command = "SELECT * FROM medicine_data WHERE indexd = %d;" % int(data)  
        cursor.execute(sql_command)
        results = cursor.fetchall()
        for row in results:
            print (row)
            name = row[1]
            locx = row[2]
            locy = row[3]
            xxx.append([name, locx, locy])
            
    
        connection.close()
    print(xxx)
    StepMove(xxx)
    
def Datarecv(data):
    datas = data.split('-')
    datas.pop(0)
    datas.pop(len(datas)-1)
    print(datas)
    print(len(datas))
    select_DB(datas)

