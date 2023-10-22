# -*- coding: utf-8 -*-

import names
from toplevelwindow import * 

def handleObject(obj):
    test.log("Button `%s` clicked" % objectName(obj))


def main():
    startApplication("testQML")
    win = ToplevelWindow.focused()
    win.maximize()
    # setWindowSize(waitForObject(names.hello_World_QQuickWindowQmlImpl), 497, 339)

    btnObject = waitForObject(names.hello_World_push_me_Button)
    installEventHandler(btnObject, "QMouseEvent", "handleObject")
    
    try:
        waitForSignal(waitForObject(names.hello_World_push_me_Button), "clicked()", 3000)
        # test.xpass("button clicked!", "clicked within 3 seconds.")
        test.log("button clicked!", "clicked within 3 seconds.")
    except RuntimeError as err:
        test.xfail("button did not click.", str(err))
    
    snooze(3)
    


