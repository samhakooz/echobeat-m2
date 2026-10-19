# Intended Pico wiring (prototype; verify before powering)

| Connection | Pico | Other end |
|---|---|---|
| Left servo signal | GP14 | Left servo orange/yellow signal wire |
| Right servo signal | GP15 | Right servo orange/yellow signal wire |
| Left input button | GP10 | Other button terminal to GND |
| Right input button | GP11 | Other button terminal to GND |
| Record/play button | GP12 | Other button terminal to GND |
| Shared reference ground | Pico GND | External 5 V adapter negative/servo ground |
| Servo positive | **NOT** from Pico 3V3 | External regulated +5 V |
| Servo negative | **NOT** from Pico 3V3 | External 5 V GND |
| Pico own power/programming | USB micro-B | Computer USB |

For buttons configure `Pin(..., Pin.IN, Pin.PULL_UP)` and treat pressed as logic low. Verify the button's paired pins with a continuity check so the input isn't permanently shorted.

For servo PWM use `machine.PWM(Pin(14), freq=50)` and pin 15 likewise. Start with calibrated narrow travel (around neutral), NOT unverified full-range pulse commands. Manufacturer PWM docs: https://docs.micropython.org/en/latest/library/machine.PWM.html

**Power:** A separate 5 V / 2 A regulated servo supply is recommended. All grounds share a reference, but +5 V goes to servo V+ only, not Pico's 3V3. Confirm polarity of barrel adapter and connector current rating before powering. Use a compatible connector distribution, and adult help where appropriate for connections or soldering. Do not run arms when adjusting the striker by hand.
