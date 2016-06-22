import os
import subprocess
from .config import read_conf
from PyQt4 import QtGui

def image_tray(image):
    root = __file__
    if os.path.islink(root):
        root = os.path.realpath(root)
    img_path = os.path.dirname(os.path.dirname(os.path.abspath(root))) + '/images/'
    return QtGui.QIcon(img_path + image)


def run(when):
    command = read_conf('run_commands', when, True)
    cmd_list = command.split()
    if cmd_list:
        subprocess.Popen(cmd_list)
