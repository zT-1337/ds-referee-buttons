import RPi.GPIO as GPIO

#---Variablen-----------
#Head_Judge
headJudgeRed = 8
headJudgeYellow = 10
headJudgeBlue = 12
headJudgeWithe = 16
headJudgeTimer = 18
#Left_Judge
leftJudgeRed = 22
leftJudgeYellow = 24
leftJudgeBlue = 26
leftJudgeWithe = 32
#Right_Judge
rightJudgeRed = 36
rightJudgeYellow = 38
rightJudgeBlue = 40
rightJudgeWithe = 37
#-----------------------

def setup():
    print("Let's Start!")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #Head_Judge
    GPIO.setup(headJudgeRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(headJudgeYellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(headJudgeBlue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(headJudgeWithe, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(headJudgeTimer, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Left_Judge
    GPIO.setup(leftJudgeRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(leftJudgeYellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(leftJudgeBlue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(leftJudgeWithe, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Right_Judge
    GPIO.setup(rightJudgeRed, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(rightJudgeYellow, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(rightJudgeBlue, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(rightJudgeWithe, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#----------Callbacks_Head_Judge------------------------
def button_callback_headJudgeRed(channel):
    print("Head Judge Red + Red")

def button_callback_headJudgeYellow(channel):
    print("Head Judge Red + Yellow")

def button_callback_headJudgeBlue(channel):
    print("Head Judge Red + Blue")

def button_callback_headJudgeWithe(channel):
    print("Head Judge Withe")

def button_callback_headJudgeTimer(channel):
    print("timer Startet")

#----------Callbacks_Left_Judge------------------------
def button_callback_leftJudgeRed(channel):
    print("Left Judge Red + Red")

def button_callback_leftJudgeYellow(channel):
    print("Left Judge Red + Yellow")

def button_callback_leftJudgeBlue(channel):
    print("Left Judge Red + Blue")

def button_callback_leftJudgeWithe(channel):
    print("Left Judge Withe")

#----------Callbacks_Right_Judge------------------------
def button_callback_rightJudgeRed(channel):
    print("Right Judge Red + Red")

def button_callback_rightJudgeYellow(channel):
    print("Right Judge Red + Yellow")

def button_callback_rightJudgeBlue(channel):
    print("Right Judge Red + Blue")

def button_callback_rightJudgeWithe(channel):
    print("Right Judge Withe")


def destroy():
    GPIO.cleanup()

def geteyeson():
    #----------------------Head_Judge-----------------------------------------------------------
    GPIO.add_event_detect(headJudgeRed, GPIO.FALLING, callback=button_callback_headJudgeRed, bouncetime = 300)
    GPIO.add_event_detect(headJudgeYellow, GPIO.FALLING, callback=button_callback_headJudgeYellow, bouncetime = 300)
    GPIO.add_event_detect(headJudgeBlue, GPIO.FALLING, callback=button_callback_headJudgeBlue, bouncetime = 300)
    GPIO.add_event_detect(headJudgeWithe, GPIO.FALLING, callback=button_callback_headJudgeWithe, bouncetime = 300)
    GPIO.add_event_detect(headJudgeTimer, GPIO.FALLING, callback=button_callback_headJudgeTimer, bouncetime=300)

    #----------------------Left_Judge-----------------------------------------------------------
    GPIO.add_event_detect(leftJudgeRed, GPIO.FALLING, callback=button_callback_leftJudgeRed, bouncetime = 300)
    GPIO.add_event_detect(leftJudgeYellow, GPIO.FALLING, callback=button_callback_leftJudgeYellow, bouncetime = 300)
    GPIO.add_event_detect(leftJudgeBlue, GPIO.FALLING, callback=button_callback_leftJudgeBlue, bouncetime = 300)
    GPIO.add_event_detect(leftJudgeWithe, GPIO.FALLING, callback=button_callback_leftJudgeWithe, bouncetime = 300)

    #----------------------Right_Judge-----------------------------------------------------------
    GPIO.add_event_detect(rightJudgeRed, GPIO.FALLING, callback=button_callback_rightJudgeRed, bouncetime = 300)
    GPIO.add_event_detect(rightJudgeYellow, GPIO.FALLING, callback=button_callback_rightJudgeYellow, bouncetime = 300)
    GPIO.add_event_detect(rightJudgeBlue, GPIO.FALLING, callback=button_callback_rightJudgeBlue, bouncetime = 300)
    GPIO.add_event_detect(rightJudgeWithe, GPIO.FALLING, callback=button_callback_rightJudgeWithe, bouncetime = 300)

if __name__ == '__main__':
    setup()
    geteyeson()
    try:
        eingabe = input("Zum Beenden srg + C")

    except KeyboardInterrupt:
        destroy()
