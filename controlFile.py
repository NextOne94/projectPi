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


def StepMove(xxx):
    locxold=0
    locyold=0
    
    for i in range(len(xxx)):
        print("len =",len(xxx))
        if locxold == 0 and locyold == 0 :
            print(i ,": new")
            locxnew = xxx[i][1]
            locynew = xxx[i][2]
            print(locxnew)
            print(locynew)
            dir_V = CCW
            dir_H = CW
            step_count_H = SPR * int(locxnew)*16
            step_count_V = SPR * int(locynew)*16
            delay = 0.007/16  # delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
            
            StepClk(step_count_H,step_count_V,dir_V,dir_H)
            print(i, ": END")
            locxold = locxnew
            locyold = locynew
        else :
            print(i, ": OLD")
            locxnew = xxx[i][1]
            locynew = xxx[i][2]
            print(locxnew)
            print(locynew)
            locxnewgo = locxnew - locxold
            locynewgo = locynew - locyold
            print(locxnewgo)
            print(locynewgo)
            if locxnewgo >= 0 :
                dir_H = CW
            elif locxnewgo < 0:
                locxnewgo = locxnewgo * (-1)
                dir_H = CCW
            if locynewgo >= 0:
                dir_V = CCW
            elif locynewgo < 0:
                locynewgo = locynewgo * (-1)
                dir_V = CW
                
            step_count_H = SPR * int(locxnewgo)*16
            step_count_V = SPR * int(locynewgo)*16
            delay = 0.007/16 # delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
            
            StepClk(step_count_H,step_count_V,dir_V,dir_H)
            print(i,": END")
            locxold = locxnew
            locyold = locynew
            if i+1 == len(xxx):
                dir_H = CCW
                dir_V = CW
                step_count_H = SPR * int(locxold)*16
                step_count_V = SPR * int(locyold)*16
                StepClk(step_count_H,step_count_V,dir_V,dir_H)
                print(i,": END Round")
    

def StepClk(locx,locy,dir_V,dir_H):
    print(locx)
    print(locy)
    delay = 0.005/16    #delay = Time to turn around 1 cycle / Steps ###0.25/200=0.00125
    GPIO.output(DIR_VER, dir_V)
    GPIO.output(DIR_HORI, dir_H)
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
        elif locx > 0:
            locx = locx - 1
            #print("locx =",locx)
        
        if locy == 0 :
            clk_v = GPIO.LOW
            status_v = True
        elif locy > 0 :
            locy = locy - 1
            #print("locy =",locy)
            
        if status_h == True and status_v == True :
            print("TrueTrue")
            sleep(1)
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

