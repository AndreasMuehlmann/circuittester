# circuittester

A program for testing digital circuits with the arduino.


# Development environment for arduino

Code written in cpp files.
Not using arduino-ide because it doesn't work properly with just using cpp
Arduino.h has to be included.

To compile from the commandline and get clangd to work properly:

```
arduino-cli config init
arduino-cli board list
arduino-cli core install <board>
arduino-cli board attach -p /dev/ttyACM0 -b arduino:sam:arduino_due_x_dbg circuittester/circuittester.ino 
arduino-cli compile --build-path ./build circuittester.ino // with build-path for getting the compile_commands.json into the right place without to compile and upload
arduino-cli upload
```
