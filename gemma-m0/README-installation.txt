
1. IMPORTANT! Disconnect the wires (if connected) between the Gemma M0 and
   the Teensy 4.x board, even if the Teensy 4.x board isn't plugged in.

2. Plug in the Gemma M0 to your computer with a USB cable. A new disk
   drive icon called CIRCUITPY will appear on your computer.

3. Press the RESET button twice (small black button, not the slider switch)
   on the Gemma M0 board. If this works, the RGB status LED(s) on the board
   will flash red and then stay green. The CIRCUITPY drive will disappear,
   and a new drive called GEMMABOOT will be mounted. (You may not see it
   right away; see step 4.)  If the LED doesn't stay green, try again --
   you have to get the timing right between the two button clicks. You will
   get a "Disk Not Ejected Properly" error -- ignore it.

4. Find the new drive, called GEMMABOOT. Sometimes it doesn't appear on
   your desktop; if this happens, go to the "top" of your file system
   (in Finder, select File-->Go-->Computer, and look for GEMMABOOT). Open
   the GEMMABOOT drive.

5. Drag the .uf2 file (e.g. adafruit-circuitpython-gemma_m0-en_US-7.3.3.uf2,
   but you may have downloaded a later version) into the GEMMABOOT folder.
   The Gemma-M0 will immediately install the new version and reboot.

6. The GEMMABOOT disk will disappear, and the CIRCUITPY disk icon
   should reappear on your desktop. (You may get another "Disk Not Ejected
   Properly" error -- ignore it.)

7. Drag the file code.py in this directory into the CIRCUITPY
   directory. The Gemma-M0's LED should blink a few times, then go off.

8. Eject the CIRCUITPY disk (drag it to the trash).

To test the Gemma-M0, touch the electrode contact labelled A0 (just to the
left of the USB cable. The red light should flicker dimly when you're near
the A0 electrode, and brightly if you touch it firmly.

All done -- you can unplug the Gemma-M0 from the USB. It is ready to use
as a proximity/touch detector.
