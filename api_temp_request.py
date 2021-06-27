import requests
import json
import jsonpickle


class GetTemperatureFromApi:
    def __init__(self, response_info, data1, data2):
        self.response_info = response_info
        self.data1 = data1
        self.data2 = data2
