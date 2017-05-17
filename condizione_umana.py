# Condizione Umana 2017 by Catodo & Effemeride
import sys, pygame, random, time, os, copy
import RPi.GPIO as GPIO

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

sample = [
    [ '16_1.wav', '16_2.wav', '16_3.wav' ],
    [ '24_1.wav', '24_2.wav', '24_3.wav', '24_4.wav' ],
    [ '29_1.wav', '29_2.wav', '29_3.wav', '29_4.wav' ],
    [ '48_1.wav', '48_2.wav', '48_3.wav', '48_4.wav' ],
    [ '52_1.wav', '52_2.wav', '52_3.wav', '52_4.wav' ],
    [ '69_1.wav', '69_2.wav', '69_3.wav', '69_4.wav' ],
    [ '39_1.wav', '39_2.wav', '39_3.wav' ],
    [ '43_1.wav', '43_2.wav', '43_3.wav', '43_4.wav' ]
]

for foglio in range(len(sample)):
    for index in range(len(sample[foglio])):
        sample[foglio][index] = pygame.mixer.Sound(os.path.join('sounds',sample[foglio][index]))
# GPIO
led = [ 17, 27, 22, 10, 9, 11, 23, 24 ]

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

for index in range(len(led)):
    GPIO.setup(led[index], GPIO.OUT)
    GPIO.output(led[index], GPIO.HIGH)
GPIO.setup(4, GPIO.IN) #PIR sensor
time.sleep(2)
for index in range(len(led)):
    GPIO.output(led[index], GPIO.LOW)

prev = foglio = -1
play = [ [], [], [], [], [], [], [], [] ]
while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit

    if pygame.mixer.music.get_busy():
        continue

    pir = GPIO.input(4)
    if pir == 0:
        continue

    while (foglio == prev):
      foglio = random.randint(0,len(sample)-1)
    prev = foglio

    GPIO.output(led[foglio], GPIO.HIGH)

    if not play[foglio]:
        random.shuffle(sample[foglio])
        play[foglio] = copy.copy(sample[foglio])

    s = play[foglio].pop()
    s.play()
    time.sleep(s.get_length()+.5)

    GPIO.output(led[foglio], GPIO.LOW)
