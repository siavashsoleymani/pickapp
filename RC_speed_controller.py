import os  # importing os library so as to communicate with the system
import time  # importing time library to make Rpi wait because its too impatient

os.system("sudo pigpiod")  # Launching GPIO library
time.sleep(1)  # As i said it is too impatient and so if this delay is removed you will get an error
import pigpio  # importing GPIO library

ESC = 4  # Connect the ESC in this GPIO pin

pi = pigpio.pi();
pi.set_servo_pulsewidth(ESC, 0)

max_value = 2000  # change this if your ESC's max value is different or leave it be
min_value = 700  # change this if your ESC's min value is different or leave it be
print
"For first time launch, select calibrate"
print
"Type the exact word for the function you want"
print
"calibrate OR manual OR control OR arm OR stop"


# def manual_drive():  # You will use this function to program your ESC if required
#     print
#     "You have selected manual option so give a value between 0 and you max value"
#     while True:
#         inp = raw_input()
#         if inp == "stop":
#             stop()
#             break
#         elif inp == "control":
#             control(1500)
#             break
#         elif inp == "arm":
#             arm()
#             break
#         else:
#             pi.set_servo_pulsewidth(ESC, inp)


# def calibrate():  # This is the auto calibration procedure of a normal ESC
#     pi.set_servo_pulsewidth(ESC, 0)
#     print("Disconnect the battery and press Enter")
#     inp = raw_input()
#     if inp == '':
#         pi.set_servo_pulsewidth(ESC, max_value)
#         print(
#             "Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then press Enter")
#         inp = raw_input()
#         if inp == '':
#             pi.set_servo_pulsewidth(ESC, min_value)
#             print
#             "Wierd eh! Special tone"
#             time.sleep(7)
#             print
#             "Wait for it ...."
#             time.sleep(5)
#             print
#             "Im working on it, DONT WORRY JUST WAIT....."
#             pi.set_servo_pulsewidth(ESC, 0)
#             time.sleep(2)
#             print
#             "Arming ESC now..."
#             pi.set_servo_pulsewidth(ESC, min_value)
#             time.sleep(1)
#             print
#             "See.... uhhhhh"
#             control(1500)  # You can change this to any other function you want
#

speed = 1500


def control(inp):
    global speed  # change your speed if you want to.... it should be between 700 - 2000
    if speed >= 2000:
        speed = 1500
    elif speed <= 700:
        speed = 1500
    pi.set_servo_pulsewidth(ESC, speed)
    print(inp)
    if inp == "q":
        speed -= 100  # decrementing the speed like hell
        print
        "speed = %d" % speed
    elif inp == "e":
        speed += 100  # incrementing the speed like hell
        print
        "speed = %d" % speed
    elif inp == "w":
        speed += 10  # incrementing the speed
        print
        "speed = %d" % speed
    elif inp == "s":
        speed -= 10  # decrementing the speed
        print
        "speed = %d" % speed
    elif inp == " ":
        speed = 1500
    # elif inp == "stop":
    #     stop()  # going for the stop function
    # elif inp == "manual":
    #     manual_drive()
    # elif inp == "arm":
    #     arm()
    # else:
    #     print
    #     "WHAT DID I SAID!! Press a,q,d or e"


# def arm():  # This is the arming procedure of an ESC
#     print
#     "Connect the battery and press Enter"
#     inp = raw_input()
#     if inp == '':
#         pi.set_servo_pulsewidth(ESC, 0)
#         time.sleep(1)
#         pi.set_servo_pulsewidth(ESC, max_value)
#         time.sleep(1)
#         pi.set_servo_pulsewidth(ESC, min_value)
#         time.sleep(1)
#         control(1500)


def stop():  # This will stop every action your Pi is performing for ESC ofcourse.
    pi.set_servo_pulsewidth(ESC, 0)
    pi.stop()


# This is the start of the program actually, to start the function it needs to be initialized before calling... stupid python.
# inp = raw_input()
# inp = "control"
# if inp == "manual":
#     manual_drive()
# elif inp == "calibrate":
#     calibrate()
# elif inp == "arm":
#     arm()
# elif inp == "control":
#     control(1500)
# elif inp == "stop":
#     stop()
# else:
#     print
#     "Thank You for not following the things I'm saying... now you gotta restart the program STUPID!!"
