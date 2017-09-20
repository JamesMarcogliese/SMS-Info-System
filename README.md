# Capstone-SIS
SMS Information System (SIS)

This repository contains the technical culmination of a Senior Engineering Project (4FD3) for McMaster University.
Authors of this work are: James Marcogliese, Guarav Sharma, and Ibadullah Usmani.

**Rationale:** Cellular phone users that do not own a smartphone or subscribe to cellular data plans do not
have access to information that can be found on smartphone applications or through services
available on the world wide web. A solution is to deliver on-demand information through an existing cellular 
service: the Short Message Service (SMS).

**Solution:** Operating in a client-server relationship, the solution consists of a central server that shall
receive queries submitted to it by a client's cellular text message (SMS), perform lookups on the
world wide web via APIs, and respond with the gathered information back to the requester. The
program to undertake the required functions is programmed in Python and run on a single-
board computer (Raspberry Pi 2) connected to the internet. A GSM module connected to the machine allows
sending and receiving of text messages to and from clients.

<p align="center">
  <img src="https://user-images.githubusercontent.com/8539492/30645888-250c784e-9de5-11e7-9330-fe5883141ee6.png" width="200"/>
  <img src="https://user-images.githubusercontent.com/8539492/30645906-34708e60-9de5-11e7-8cd0-7c8f459b19ee.png" width="200"/>
  <img src="https://user-images.githubusercontent.com/8539492/30645915-3e7f095e-9de5-11e7-9576-f036a4ea7bc6.png" width="200"/>
</p>

PLEASE NOTE: RPi's serial debug interface must be disabled prior to use by the GSM Model shield.
Browse to: /boot/firmware/cmdline.txt
  * sudo cp /boot/firmware/cmdline.txt /boot/firmware/cmdline_backup.txt
  * sudo nano /boot/firmware/cmdline.txt
 
ORIGINAL FILE CONTENTS: 
net.ifnames=0 dwc_otg.lpm_enable=0 console=ttyAMA0,115200 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
CHANGE CONTENTS TO:
net.ifnames=0 dwc_otg.lpm_enable=0 console=tty1 root=/dev/mmcblk0p2 rootfstype=ext4 elevator=deadline rootwait
  * sudo cp /etc/init/ttyAMA0.conf /etc/init/ttyAMA0_backup.conf
  * sudo nano /etc/init/ttyAMA0.conf
  
COMMENT OUT THE FOLLOWING LINES:
stty -F /dev/ttyAMA0 -a 2> /dev/null > /dev/null || { stop ; exit 0; } 			
exec /sbin/getty -L ttyAMA0 115200 vt102
