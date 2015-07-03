import sys
import os
from ten_ten import *

""" a test code to learn about the paths and
    importing from a different directory"""

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../chapter 11'))
sys.path.append(path)
print path
from eleven_six import *


