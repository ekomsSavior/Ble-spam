BLE Spammer Script

A Python script that continuously sends messages to a BLE device, flooding it with spam messages.

⚠️ Disclaimer

This script is for educational and research purposes only. Unauthorized BLE spamming may be illegal in your country. Use responsibly in controlled environments.

🔧 Requirements

Before running this script, ensure your Kali Linux environment has the necessary dependencies.

1️⃣ Install Dependencies

Run the following command to install required packages:

sudo apt update && sudo apt install -y python3-pip bluetooth libbluetooth-dev
pip3 install bluepy

2️⃣ Enable Bluetooth Interface

Make sure your Bluetooth adapter is properly recognized:

hciconfig

If your adapter is listed but not up, enable it:

sudo hciconfig hci0 up

3️⃣ Clone the Repository

Download the script from GitHub:

git clone https://github.com/yourusername/BLE-Spammer.git
cd BLE-Spammer

4️⃣ Edit the Script

Before running, open the script and replace XX:XX:XX:XX:XX:XX with the MAC address of your target BLE device:

target_mac = "XX:XX:XX:XX:XX:XX"

You can find the BLE MAC address by scanning with:

hcitool lescan

5️⃣ Run the Script

Start spamming the BLE device by running:

python3 ble_spam.py

🛑 Stop the Attack

Press CTRL + C to stop the script at any time.

🛠 Troubleshooting

✅ “bluepy not found” error

If bluepy is not installed correctly, try:

pip3 install --upgrade bluepy

✅ “Failed to connect to device” error
	•	Ensure the target BLE device is within range.
	•	Reset your Bluetooth adapter:

sudo hciconfig hci0 reset

	•	Try running the script again.

📜 Legal & Ethical Considerations
	•	This script should be used only on devices you own or have permission to test.
	•	DO NOT use this for malicious purposes.
	•	Use responsibly in controlled environments.

⸻

That should make it easy-to-follow for your GitHub followers! 🚀 Let me know if you need tweaks, fren! 🫂💖
