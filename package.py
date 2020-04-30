# -*- coding: utf-8 -*-
name = 'python_qtpy'

version = '0.6.9'

description = 'Minimal Python 2 & 3 shim around all Qt bindings - PySide, PySide2, PyQt4 and PyQt5. (SqueezeStudioAnimation fork)'

help = 'https://github.com/SqueezeStudioAnimation/Qt.py'

build_command = "mkdir {root}/build/python/ && cp -f {root}/Qt.py {root}/build/python/Qt.py"

requires = ['python-2']

def commands():
    env.QT_PREFERRED_BINDING = "PySide2"
    env.PYTHONPATH.append("{root}/build/python")

