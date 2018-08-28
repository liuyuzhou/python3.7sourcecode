#! /usr/bin/python3
# -*- coding:UTF-8 -*-
from chapter8.weather_search import WeatherSearch

class OutAdvice(WeatherSearch):
    def __init__(self, input_daytime):
        WeatherSearch.__init__(self, input_daytime)

    def seach_temperature(self):
        vehicle = ''
        if self.input_daytime == 'daytime':
            vehicle = 'bike'
        if self.input_daytime == 'night':
            vehicle = 'taxi'
        return vehicle

    def out_advice(self):
        visible_leave = self.seach_visibility()
        if visible_leave == 2:
            print(f'The weather is good,suitable for use {self.seach_temperature()}.')
        elif visible_leave == 9:
            print(f'The weather is bad,you should use {self.seach_temperature()}.')
        else:
            print('The weather is beyond my scope,I can not give you any advice')


check = OutAdvice('daytime')
check.out_advice()

