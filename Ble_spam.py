from bluepy.btle import Peripheral, ADDR_TYPE_RANDOM, DefaultDelegate

# Replace 'XX:XX:XX:XX:XX:XX' with your BLE adapter's MAC address
target_mac = "XX:XX:XX:XX:XX:XX"

class BLESpam(DefaultDelegate):
    def __init__(self):
        DefaultDelegate.__init__(self)

    def handleNotification(self, cHandle, data):
        print(f"Notification: {data}")

def spam_ble():
    try:
        peripheral = Peripheral(target_mac, ADDR_TYPE_RANDOM)
        peripheral.setDelegate(BLESpam())
        while True:
            peripheral.writeCharacteristic(0x0001, b"Spam Message")
            print("Spamming...")
    except Exception as e:
        print(f"Error: {e}")

spam_ble()
