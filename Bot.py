import time
from datetime import datetime

def check_signal():
    # nanti diganti dengan logika deteksi engulfing
    print("Cek candlestick...")
    return "Belum ada sinyal"

while True:
    signal = check_signal()
    print(datetime.now(), signal)
    time.sleep(300)  # cek tiap 5 menit
