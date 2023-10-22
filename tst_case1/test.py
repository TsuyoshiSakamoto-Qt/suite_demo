# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")

    test.compare(str(waitForObjectExists(names.hello_World_text1_Text).text), "default text")
    snooze(0.5)
    mouseClick(waitForObject(names.hello_World_push_me_Button), Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.hello_World_text1_Text).text), "clicked!")
