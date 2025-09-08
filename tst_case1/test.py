# -*- coding: utf-8 -*-

import names
import os

def main():
    startApplication("testQML" )
    # startApplication("testQML", "127.0.0.1", 4322)
    # test.log("Memory: %d" % ctx.usedMemory) 
    # startApplication("testQML", "192.168.1.15", 4322)

    test.compare(str(waitForObjectExists(names.hello_World_labelText1_Text).text), "default text")
    snooze(1)
    mouseClick(waitForObject(names.hello_World_push_me_Button), 109, 21, Qt.LeftButton)
    snooze(1)
    test.compare(str(waitForObjectExists(names.hello_World_labelText1_Text).text), "clicked!")
    
    obj = waitForObjectExists(names.hello_World_labelText1_Text)
    obj.text = "modified by squish!"
    
    # path = os.getcwd()
    # test.log(path)
    # print(path)
    
    snooze(3)
    
