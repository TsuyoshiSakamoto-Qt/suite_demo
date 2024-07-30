# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    test.compare(str(waitForObjectExists(names.hello_World_labelText1_Text).text), "default text")
    mouseClick(waitForObject(names.hello_World_push_me_Button),  Qt.LeftButton)
    test.compare(str(waitForObjectExists(names.hello_World_labelText1_Text).text), "clicked!")
    
    # wait until "push me button" clicked.
    # test.compare(str(waitForObjectExists(names.hello_World_labelText1_TextSearch).text), "clicked!")

    
    
