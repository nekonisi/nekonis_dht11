# -*- coding: utf-8 -*-
"""
温度、湿度センサーのテスト
@author: nekonisi
"""

import RPi.GPIO as GPIO
import dht11
from time import sleep

# オマジナイ
GPIO.setwarnings(False) # GPIO.cleanup()をしなかった時のメッセージを非表示にする
GPIO.setmode(GPIO.BCM) # ピンをGPIOの番号で指定

TEMP_SENSOR_PIN = 4 # 温湿度センサーのピンの番号 環境によって切り分けてください
MAX_RETRY = 10 # リトライ回数

sensor = dht11.DHT11(pin=TEMP_SENSOR_PIN)
count = 0

while True:
    count += 1
    if MAX_RETRY <= count:
        break
    result = sensor.read() # 値読み込み
    if result.is_valid():
        print("temperature:", result.temperature, "humidity:", result.humidity)
        break
    sleep(1)
