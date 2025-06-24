# -*- coding: utf-8 -*-

import names

def handleDescriptionQPushButton(obj):
    test.log("PushButton cliked!")

    
def main():
    startApplication("testQML")
    # mouseClick(waitForObject(names.hello_World_push_me_Button), 112, 27, Qt.LeftButton)
    
    obj = waitForObject(names.hello_World_push_me_Button)
    installSignalHandler(obj, "clicked()", "handleDescriptionQPushButton")
    installSignalHandler("Button", "clicked()", "handleDescriptionQPushButton")

    
    obj.clicked()
    
    waitForSignal(waitForObject(names.hello_World_push_me_Button), "clicked()", 5000)
    test.log("test end!")
    
    snooze(2)
