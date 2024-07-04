#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
# from ctypes import windll

from PySide6.QtWidgets import QApplication

from controllers import ControllerMain

if __name__ == '__main__':

    app = QApplication()
    # Not exit when the Windows is closed
    if app.setQuitOnLastWindowClosed(True):
        QApplication.quit()
    controller = ControllerMain()
    # event loop
    sys.exit(app.exec())