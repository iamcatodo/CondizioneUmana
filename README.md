# Condizione Umana

Interactive art installattion using a Raspberry Pi, Python, LEDs, PIR sensor,
audio.


## Run the script

You can use python to run the scripts, using the following command:

```bash
python condizione_umana.py
```

The scripts assume that you have configured the LEDS and the PIR sensor using
the following GPIO ports:

```python
GPIO.setmode(GPIO.BCM)
led = [ 17, 27, 22, 10, 9, 11, 23, 24 ]
pir = GPIO.input(4)
```

(C) Copyright 2017 by Catodo & Effemeride.
