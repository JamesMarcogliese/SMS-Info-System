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
