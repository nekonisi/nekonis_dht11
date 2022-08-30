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

class Dht11:
    def __init__(self, sensor_pin=4, max_retry=10):
        """
        コンストラクタ
        Args:
            sensor_pin: int : 温湿度センサーのピンの番号
            max_retru: int : リトライ回数
        """
        self.temp_sensor_pin = sensor_pin
        self.max_retry = max_retry
        self.sensor = dht11.DHT11(pin=self.temp_sensor_pin)

    def getTempeatureAndHumidity(self):
        """
        温度と湿度を取得
        Returns:
            (温度, 湿度)
        """
        count = 0
        while True:
            count += 1
            if self.max_retry <= count:
                break
            result = self.sensor.read() # 値読み込み
            if result.is_valid():
                return result.temperature, result.humidity
            sleep(1)
