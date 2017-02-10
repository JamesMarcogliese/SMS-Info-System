

#poweron the RPI GSM SIM900 module
def PowerON_SIM900_module():
    GPIO.setup(17,GPIO.OUT)
    GPIO.output(17,GPIO.HIGH)
    return;



