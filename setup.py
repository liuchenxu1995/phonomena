import os
import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

if __name__ == '__main__':
    packages = ['matplotlib', 'PyQt5', 'numpy', 'h5py', 'numba', 'requests', 'dill', 'PyInstaller']

    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "pip"])

    if os.name == 'nt':
        packages.append('pypiwin32')
    elif os.name == 'posix':
        packages.append('bohrium')

    for package in packages:
         install(package)
