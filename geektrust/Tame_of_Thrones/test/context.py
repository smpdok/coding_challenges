import os
import sys

current_path = os.path.abspath(os.path.join(os.path.dirname(__file__)))
root_path, slash, test = current_path.rpartition("\\")
sys.path.insert(0, root_path)

from scripts.read_file import ReadFile
from scripts.message import Message
from geektrust import Southeros
