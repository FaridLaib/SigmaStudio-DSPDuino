# SigmaStudio-DSPDuino

This program enables an Arduino or ESP32 to communicate with an Analog Devices ADAU1701 SigmaDSP over the I²C (Wire) interface.
It allows real-time volume adjustment through serial commands.


⚙️ How It Works

Initialization
Sets up I²C communication using the Wire library.
Initializes the SigmaDSP using the SigmaDSP library.
Loads a precompiled DSP program (SigmaDSP_parameters.h).
Sets the initial volume to 0 dB.
Runtime Control
Continuously listens for serial input.
When receiving a command like:
Volume: -10
it updates the DSP’s software volume control block (MOD_SWVOL1_ALG0_TARGET_ADDR) accordingly.
Feedback
Prints confirmation messages to the Serial Monitor for debugging and verification.


🧾 Key Components
MCUdude is a fantastic library to understand the parameters and values.
https://github.com/MCUdude/SigmaDSP

SigmaDSP.h — Handles communication and control of the ADAU1701.
SigmaDSP_parameters.h — Contains the DSP program binary and address definitions exported from SigmaStudio.
Wire (I²C) — Interface used for data transfer between the microcontroller and DSP.


![IMG_8471](https://github.com/user-attachments/assets/3aebf091-40dc-4280-851f-b7ee66ea2d7f)
