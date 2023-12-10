# -*- coding: utf-8 -*-

import names
from toplevelwindow import *


def main():
    startApplication("testQML")
    # win = waitForObject(names.hello_World_QQuickWindowQmlImpl)
    
    snooze(3)
    
    win = ToplevelWindow.byName(names.hello_World_QQuickWindowQmlImpl)
    # ToplevelWindow.setForeground(win)
    ToplevelWindow.setFullscreen(win)
    geom = win.geometry
    test.log("Focused window is " + str(geom.width) + " by " + str(geom.height))
    
    