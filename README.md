# F1 22 Telemetry Analyzer
## Disclaimer
This project is very much not finished at all and was started as a training project.  
Do not expect it to work flawlessly or even at all.  
I still appreciate any feedback and suggestions for improvements.
## Installation & Setup
### Clone the project
```shell
git clone https://github.com/lassewolpmann/F1-22_Telemetry
cd F1-22_Telemetry/
pip install -r requirements.txt
mkdir cache/
```
### F1 22 Settings
Find the Telemetry Settings and make sure the settings are as following
* UDP Telemetry - On
* UDP Broadcast Mode - Off
* UDP-IP Address - 127.0.0.1
* UDP-Port - 27001
* UDP Send Rate - 60Hz
* UDP Format - 2022
* Your Telemetry - Public
### Run
```shell
./main.py
```
## Use Instructions
**This tool for now is best used in the Hot Lap Mode!**  
Start a Session  
Drive as many laps as you want, **but at least one full lap**  
When you want your best lap time analyzed, end the session and the tool will automatically stop the data recording.  
After a short while, a window with two lines should pop up.