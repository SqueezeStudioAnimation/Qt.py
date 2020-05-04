# -*- coding: utf-8 -*-
name = 'python_qtpy'

version = '1.0.0'

description = 'Minimal Python 2 & 3 shim around all Qt bindings - PySide, PySide2, PyQt4 and PyQt5. (SqueezeStudioAnimation fork)'

help = 'https://github.com/SqueezeStudioAnimation/Qt.py'

requires = ['python-2']

def commands():
    env.QT_PREFERRED_BINDING = "PySide2"
    env.PYTHONPATH.append("{root}/build/python")

