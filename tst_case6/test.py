# -*- coding: utf-8 -*-

import names
source(findFile("scripts", "function.py"))

def main():
    startApplication("testQML")
    # mouseClick(waitForObject(names.hello_World_push_me_Button), 122, 31, Qt.LeftButton)
    # mouseClick(waitForObject(names.hello_World_set_default_Button), 45, 27, Qt.LeftButton)
    # mouseClick(waitForObject(names.hello_World_CustomButton_2), 213, 30, Qt.LeftButton)


    switch = getChildrenOfType(names.hello_World_Switch_Text_0_Text, "Switch", 1, 2)
    for child in switch:
        mouseClick(waitForObject(child), Qt.LeftButton)
        
    # snooze(1)
    
    # switch = getChildrenWithProperty(names.hello_World_Switch_Text_0_Text, "id", "button_switch", 1, 2)
    # switch = getChildrenWithProperty(names.hello_World_Switch_Text_0_Text, "id", "button_switch", 0, 1)
    # for child in switch:
    #     mouseClick(waitForObject(child), Qt.LeftButton)
        
        
    text = getChildrenOfType(names.hello_World_Switch_Text_0_Text, "Text", 1, 2) 
    # switch = getChildrenOfType(names.hello_World_Switch_Text_0_Text, "Switch", 1, 2)
    for index, child in enumerate(text):
        # test.log(str(child.text))
        if str(child.text) == "Switch Text 1":
            mouseClick(waitForObject(switch[index]), Qt.LeftButton)
        
