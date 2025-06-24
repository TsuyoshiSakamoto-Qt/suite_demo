# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    combo = waitForObject(names.hello_World_comboBox_ComboBox)
    
    combo.incrementCurrentIndex()
    test.log(str(combo.currentText))
    
    for index in range(combo.count):
        test.log(str(combo.textAt(index)))
        
    combo.currentIndex = combo.find("peach", 0)
    test.log(str(combo.currentText))
    

    # highlightObject(names.hello_World_comboBox_ComboBox)
    
