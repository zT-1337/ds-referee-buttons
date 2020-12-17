import RPi.GPIO as GPIO
from Config import Config
from ApiService import ApiService, RefereeDecision, RefereeType
from CurrentAthleteRefresher import CurrentAthleteRefresher

config = Config()
apiService = ApiService(config.get("username"), config.get("password"), config.get("competitionId"))
currentAthleteRefresher = CurrentAthleteRefresher(apiService, config.get("pollingInterval"))

def setup():
    print("Let's Start!")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    #Head_Judge
    GPIO.setup(config.get("headJudgeRed"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("headJudgeYellow"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("headJudgeBlue"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("headJudgeWhite"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("headJudgeTimer"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Left_Judge
    GPIO.setup(config.get("leftJudgeRed"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("leftJudgeYellow"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("leftJudgeBlue"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("leftJudgeWhite"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    #Right_Judge
    GPIO.setup(config.get("rightJudgeRed"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("rightJudgeYellow"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("rightJudgeBlue"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(config.get("rightJudgeWhite"), GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

#----------Callbacks_Head_Judge------------------------
def button_callback_headJudgeRed(channel):
    apiService.sendRefereeDecision(RefereeType.MAIN, RefereeDecision.RED)
    print("Head Judge Red + Red")

def button_callback_headJudgeYellow(channel):
    apiService.sendRefereeDecision(RefereeType.MAIN, RefereeDecision.YELLOW)
    print("Head Judge Red + Yellow")

def button_callback_headJudgeBlue(channel):
    apiService.sendRefereeDecision(RefereeType.MAIN, RefereeDecision.BLUE)
    print("Head Judge Red + Blue")

def button_callback_headJudgeWhite(channel):
    apiService.sendRefereeDecision(RefereeType.MAIN, RefereeDecision.WHITE)
    print("Head Judge White")

def button_callback_headJudgeTimer(channel):
    print("timer Startet")

#----------Callbacks_Left_Judge------------------------
def button_callback_leftJudgeRed(channel):
    apiService.sendRefereeDecision(RefereeType.LEFT, RefereeDecision.RED)
    print("Left Judge Red + Red")

def button_callback_leftJudgeYellow(channel):
    apiService.sendRefereeDecision(RefereeType.LEFT, RefereeDecision.YELLOW)
    print("Left Judge Red + Yellow")

def button_callback_leftJudgeBlue(channel):
    apiService.sendRefereeDecision(RefereeType.LEFT, RefereeDecision.BLUE)
    print("Left Judge Red + Blue")

def button_callback_leftJudgeWhite(channel):
    apiService.sendRefereeDecision(RefereeType.LEFT, RefereeDecision.WHITE)
    print("Left Judge White")

#----------Callbacks_Right_Judge------------------------
def button_callback_rightJudgeRed(channel):
    apiService.sendRefereeDecision(RefereeType.RIGHT, RefereeDecision.RED)
    print("Right Judge Red + Red")

def button_callback_rightJudgeYellow(channel):
    apiService.sendRefereeDecision(RefereeType.RIGHT, RefereeDecision.YELLOW)
    print("Right Judge Red + Yellow")

def button_callback_rightJudgeBlue(channel):
    apiService.sendRefereeDecision(RefereeType.RIGHT, RefereeDecision.BLUE)
    print("Right Judge Red + Blue")

def button_callback_rightJudgeWhite(channel):
    apiService.sendRefereeDecision(RefereeType.RIGHT, RefereeDecision.WHITE)
    print("Right Judge White")


def destroy():
    GPIO.cleanup()

def geteyeson():
    #----------------------Head_Judge-----------------------------------------------------------
    GPIO.add_event_detect(config.get("headJudgeRed"), GPIO.FALLING, callback=button_callback_headJudgeRed, bouncetime = 300)
    GPIO.add_event_detect(config.get("headJudgeYellow"), GPIO.FALLING, callback=button_callback_headJudgeYellow, bouncetime = 300)
    GPIO.add_event_detect(config.get("headJudgeBlue"), GPIO.FALLING, callback=button_callback_headJudgeBlue, bouncetime = 300)
    GPIO.add_event_detect(config.get("headJudgeWhite"), GPIO.FALLING, callback=button_callback_headJudgeWhite, bouncetime = 300)
    GPIO.add_event_detect(config.get("headJudgeTimer"), GPIO.FALLING, callback=button_callback_headJudgeTimer, bouncetime=300)

    #----------------------Left_Judge-----------------------------------------------------------
    GPIO.add_event_detect(config.get("leftJudgeRed"), GPIO.FALLING, callback=button_callback_leftJudgeRed, bouncetime = 300)
    GPIO.add_event_detect(config.get("leftJudgeYellow"), GPIO.FALLING, callback=button_callback_leftJudgeYellow, bouncetime = 300)
    GPIO.add_event_detect(config.get("leftJudgeBlue"), GPIO.FALLING, callback=button_callback_leftJudgeBlue, bouncetime = 300)
    GPIO.add_event_detect(config.get("leftJudgeWhite"), GPIO.FALLING, callback=button_callback_leftJudgeWhite, bouncetime = 300)

    #----------------------Right_Judge-----------------------------------------------------------
    GPIO.add_event_detect(config.get("rightJudgeRed"), GPIO.FALLING, callback=button_callback_rightJudgeRed, bouncetime = 300)
    GPIO.add_event_detect(config.get("rightJudgeYellow"), GPIO.FALLING, callback=button_callback_rightJudgeYellow, bouncetime = 300)
    GPIO.add_event_detect(config.get("rightJudgeBlue"), GPIO.FALLING, callback=button_callback_rightJudgeBlue, bouncetime = 300)
    GPIO.add_event_detect(config.get("rightJudgeWhite"), GPIO.FALLING, callback=button_callback_rightJudgeWhite, bouncetime = 300)

if __name__ == '__main__':
    setup()
    geteyeson()
    try:
        eingabe = input("Zum Beenden srg + C")

    except KeyboardInterrupt:
        destroy()
