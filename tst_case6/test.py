# -*- coding: utf-8 -*-

import names
import json
from collections import OrderedDict

def main():
    # startApplication("C:\Qt_dc\MaintenanceTool.exe")

    startApplication("testQML")
    win = waitForObjectExists(names.hello_World_QQuickWindowQmlImpl)
    win.width = 600
    win.height = 600
    win.x = 1920
    win.y = 30
    # win.showFullScreen()
    # setWindowState(win, WindowState.Fullscreen)
    # setWindowState(win, WindowState.Minimize)
    
    temp = json.loads('{"zero":"0番"}', object_pairs_hook=OrderedDict)
    temp["fisrt"] = "1番"
    temp["second"] = "2番"
    temp["third"] = "3番"
    temp["fourth"] = "4番"
    temp["fifth"] = "5番"
    
    for key, value in temp.items():
        test.log(key + " : " + value)
        
    test.log(temp["zero"])
        

    snooze(2)