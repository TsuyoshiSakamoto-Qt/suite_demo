# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    mouseClick(waitForObject(names.hello_World_push_me_Button), Qt.LeftButton)
    mouseClick(waitForObject(names.hello_World_screen01_ui), 214, 232, Qt.LeftButton)
    test.vp("VP1")
