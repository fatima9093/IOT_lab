import network
import time

WIFI_SSID = "Ahmad Home"
WIFI_PASS = "Hm@123579"

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASS)

    for _ in range(10):
        if wlan.isconnected():
            print("Connected! IP:", wlan.ifconfig()[0])
            return True
        time.sleep(1)
    print("Failed to connect.")
    return False

connect_wifi()