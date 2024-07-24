import os
 
def turn_off_one_hour():
   os.system('shutdown /s /t 3600')

def turn_off_half_hours():
   os.system('shutdown /s /t 1800')

def cancel_shutdown():
   os.system('shutdown /a')


# Para Linux
def turn_off_one_hour():
    os.system('shutdown -h +60')

def turn_off_half_hours():
    os.system('shutdown -h +30')

def cancel_shutdown():
    os.system('shutdown -c')

cancel_shutdown()