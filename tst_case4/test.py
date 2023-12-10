# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    mouseClick(waitForOcrText("PUSH ME!"))
    test.compare(str(waitForObjectExists(names.hello_World_clicked_Text).text), "clicked!")
