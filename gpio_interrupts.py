import RPi.GPIO as GPIO  
GPIO.setmode(GPIO.BCM)  

GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

def my_callback(channel):  
    print ("falling edge detected on 17")  
  
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)  





def Main():
    print("Select the opiton : 1: random Data ")
    print("                    2: show random data")
    print("                    3: sort and show data")
    print("                    4: Send data to stm32 with I2C protocol")
    print("                    0: To Exit")
    select = input()
    if int(select) == 1 :
        print("1")
        #random_data()
        Main()
    elif int(select) == 2:
        print("2")
        #show_data()
        Main()
    elif int(select) == 3:
        print("3")
        #sort_data()
        Main()
    elif int(select) == 4: 
        print("4")
        #print(b)
        #if(b == 97):
            #send_data()
        #elif(b == 98):
            #print("Unfinish move")
        Main()
    elif int(select) == 0 :
        #connection = sqlite3.connect('project_test.db')
        #connection.close() 
        print("End")
        GPIO.cleanup()
    else:
        Main()


if __name__ == '__main__':
        #print("Server Start")
        Main()


GPIO.cleanup()
