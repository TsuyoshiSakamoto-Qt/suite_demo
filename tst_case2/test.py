# -*- coding: utf-8 -*-

import names

def main():
    
    for i in range(3):
        startApplication("testQML")
        mouseClick(waitForObject(names.hello_World_push_me_Button), Qt.LeftButton)
        test.compare(str(waitForObjectExists(names.hello_World_labelText1_Text).text), "clicked!")
        for ctx in applicationContextList():
            ctx.detach()
        test.log("application detached:" + str(i))
        snooze(2)

    snooze(1)

