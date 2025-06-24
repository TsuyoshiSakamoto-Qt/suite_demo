# -*- coding: utf-8 -*-

import names
import os

def main():
    startApplication("testQML")
    mouseClick(waitForObject(names.hello_World_push_me_Button), 69, 20, Qt.LeftButton)
    mouseClick(waitForObject(names.hello_World_set_default_Button), 48, 32, Qt.LeftButton)
    snooze(1)
    
    
    winAutName = "WpfApp1"
    winPackage = r"C:\Users\tssakamo\Squish for Windows 7.2.1"
    winHost = "localhost"
    winPort = 4328

    os.environ["SQUISH_PREFIX"] = winPackage
    testSettings.setWrappersForApplication(winAutName, ["Windows"])
    winContext = startApplication(winAutName, winHost, winPort)
    
    