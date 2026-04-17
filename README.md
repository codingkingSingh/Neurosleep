# Neurosleep

Brain-inspired Python network: cleans itself and optimizes traffic using simulated sleep cycles.

## Computer Networks - CPSI 38403 GitHub Repository  
**Group:** Sun

## Project Summary

- The goal of our project is to build a Python server that will act as the sleep cycle of dolphins in order to clean its memory and improve the packet routing without any network downtime.

- When Computer networks go through high traffic, they store data temporarily that eventually fills up and causes the whole system to slow down and start dropping packets.

- Our approach fixes this by integrating concepts of cognitive neuroscience and biology of animals such as dolphins (Cetaceans). The server will use a multithreaded architecture.

### Threads

- **"Awake" Thread:** It will continously route message between clients.  
- **"Sleeping" Thread:** It will run in the backgroud and enter "Deep Sleep" to delete old messages and then "REM" sleep to organize a list of priority users.



By implementing these naps, the network will maintain a 100% uptime and run smoothly.
