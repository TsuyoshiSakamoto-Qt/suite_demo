# -*- coding: utf-8 -*-

import names


def main():
    app1 = startApplication("testQML")
    app2 = startApplication("testWidget")
    
    snooze(1)
    setApplicationContext(app1)
    mouseClick(waitForObject(names.hello_World_push_me_Button), Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.hello_World_clicked_Text).text), "clicked!")
    
    # testSettings.setWrappersForApplication("sakura", ("Windows", ""))
    # startApplication("sakura")

    snooze(1)
