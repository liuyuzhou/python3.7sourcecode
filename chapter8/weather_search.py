#! /usr/bin/python3
# -*- coding:UTF-8 -*-

class WeatherSearch(object):
    def __init__(self, input_daytime):
        self.input_daytime = input_daytime

    def seach_visibility(self):
        visible_leave = 0
        if self.input_daytime == 'daytime':
            visible_leave = 2
        if self.input_daytime == 'night':
            visible_leave = 9
        return visible_leave

    def seach_temperature(self):
        temperature = 0
        if self.input_daytime == 'daytime':
            temperature = 26
        if self.input_daytime == 'night':
            temperature = 16
        return temperature
