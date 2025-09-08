# -*- coding: utf-8 -*-

import names


def main():
    startApplication("testQML")
    # test.imagePresent("qt-logo", {"tolerant":True, "threshold":97.859, "multiscale":True})
    # test.imagePresent("qt-logo", {"tolerant":True, "threshold":97.859, "multiscale":True, "maxscale":150, "minscale":100})
    # test.imagePresent("Qt-Dice", {"tolerant":True, "threshold":95.859, "multiscale":True})
    # test.imagePresent("qt-logo_2", {"tolerant":True, "threshold":90.859, "multiscale":True})
    # test.imagePresent("CMakeLogo")
    # test.vpWithImage("VP1", "../shared/searchImages/Qt-Dice.jpg")

    test.imagePresent("qt-logo")
    test.imagePresent("Qt-Dice")
    test.imagePresent("qt-logo_2")
    
        # test.vpWithImage("VP1", "../shared/searchImages/Qt-Dice.jpg")
