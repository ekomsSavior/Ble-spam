BLE SPAM 

Prepare Your Environment
	•	Ensure Your BLE Adapter is Recognized:
> hciconfig

•	If it’s down, activate it:
> sudo hciconfig hci0 up

•	Install Required Tools:
	•	Update and upgrade your system:
 > sudo apt update && sudo apt upgrade -y

•	Install bluez, hcxdumptool, and bettercap:
> sudo apt install bluez hcxdumptool bettercap -y

2. Choose a BLE Spamming Tool

There are several tools you can use to spam BLE packets. Below are two popular options:

Option 1: Using Bettercap

Bettercap is versatile for BLE scanning and manipulation.
	1.	Start Bettercap:
 > sudo bettercap -caplet ble

2.	Enable BLE Advertising Spam:
	•	In the Bettercap session, run:
> ble.recon on
> ble.advertise on
> ble.advertise.custom "Your Custom Message Here"

•	Replace "Your Custom Message Here" with the payload or advertisement you want to spam.

	3.	Monitor and Adjust:
	> 	Use ble.show to see nearby BLE devices and monitor your spam.

*Using Custom Python Scripts

You can use Python with the bluepy or pybluez library to create custom BLE advertisements.
	1.	Install Dependencies:
 > pip install bluepy 

Write a BLE Advertisement Script: see ble_spam.py file 

Run 5e Script:
> python3 ble_spam.py

Test Your Setup
	•	Use a BLE scanner (e.g., nRF Connect on your phone) to verify that your BLE spam is being broadcast.
	•	Adjust payloads and frequencies as needed.

Compliance: Be mindful of local laws and regulations regarding BLE spamming.


