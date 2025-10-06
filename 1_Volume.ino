#include <Wire.h>
#include <SigmaDSP.h>
#include "SigmaDSP_parameters.h"

SigmaDSP dsp(Wire, DSP_I2C_ADDRESS, 48000.00f);

void setup() 
{
  Serial.begin(9600);
  Wire.begin();
  dsp.begin();
  
  Serial.println(F("SigmaDSP Volume Control Example"));
  
  // Load DSP program
  Serial.println(F("Loading DSP program..."));
  loadProgram(dsp);
  Serial.println(F("Done!\n"));

  // Set initial volume to 0dB
  dsp.volume_slew(MOD_SWVOL1_ALG0_TARGET_ADDR, 0);
  Serial.println(F("Volume initialized to 0dB."));
}

void processSerialCommand() {
    if (Serial.available()) {
        String command = Serial.readStringUntil('\n');
        command.trim();
        
        if (command.startsWith("Volume:")) {
            float volume = command.substring(7).toFloat(); // Extract volume value
            dsp.volume_slew(MOD_SWVOL1_ALG0_TARGET_ADDR, (int)volume); // Update DSP volume
            Serial.print(F("Volume updated to: "));
            Serial.println(volume);
        }
    }
}

void loop() 
{
    processSerialCommand();
}