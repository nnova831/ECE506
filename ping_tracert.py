import platform    # For getting the operating system name
import subprocess  # For executing a shell command
import numpy as np
import csv
import os


hostname = "google.com" #example
response = os.system("ping -c 1 " + hostname)
