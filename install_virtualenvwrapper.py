import os
import subprocess
import sys

# Step 1: Install pip for Python3
print("Installing pip for Python3...")
try:
    subprocess.run(["sudo", "apt-get", "update"], check=True)
    subprocess.run(["sudo", "apt-get", "install", "-y", "python3-pip"], check=True)
    print("pip for Python3 installed successfully.")
except subprocess.CalledProcessError:
    print("Failed to install pip for Python3.", file=sys.stderr)
    exit(1)

# Step 2: Create the Virtual Environments Directory
print("Creating virtual environments directory...")
os.makedirs(os.path.expanduser("~/.virtualenvs"), exist_ok=True)
print("Virtual environments directory created successfully.")

# Step 3: Confirm pip3 Installation
print("Confirming pip3 installation...")
try:
    pip3_version = subprocess.check_output(["pip3", "--version"], universal_newlines=True)
    print(f"pip3 installation confirmed: {pip3_version.strip()}")
except subprocess.CalledProcessError:
    print("pip3 is not installed properly.", file=sys.stderr)
    exit(1)

# Step 4: Install virtualenv
print("Installing virtualenv...")
try:
    subprocess.run(["sudo", "pip3", "install", "virtualenv"], check=True)
    print("virtualenv installed successfully.")
except subprocess.CalledProcessError:
    print("Failed to install virtualenv.", file=sys.stderr)
    exit(1)

# Step 5: Install virtualenvwrapper
print("Installing virtualenvwrapper...")
try:
    subprocess.run(["sudo", "pip3", "install", "virtualenvwrapper"], check=True)
    print("virtualenvwrapper installed successfully.")
except subprocess.CalledProcessError:
    print("Failed to install virtualenvwrapper.", file=sys.stderr)
    exit(1)

# Step 6: Modify .bashrc
print("Modifying .bashrc...")
bashrc_path = os.path.expanduser("~/.bashrc")
with open(bashrc_path, "a") as bashrc_file:
    bashrc_file.write("# Virtualenvwrapper settings:\n")
    bashrc_file.write("export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3\n")
    bashrc_file.write("export WORKON_HOME=$HOME/.virtualenvs\n")
    bashrc_file.write("export VIRTUALENVWRAPPER_VIRTUALENV=/usr/local/bin/virtualenv\n")
    bashrc_file.write("source /usr/local/bin/virtualenvwrapper.sh\n")
print(".bashrc modified successfully.")

# # Step 7: Reload .bashrc
# print("Sourcing .bashrc to apply changes...")
# try:
#     subprocess.run(["bash", "-c", "source ~/.bashrc"], check=True)
#     print(".bashrc reloaded successfully.")
# except subprocess.CalledProcessError:
#     print("Failed to reload .bashrc.", file=sys.stderr)
#     exit(1)


# # Step 8: Install OpenCV and Dependencies
# print("Installing OpenCV and dependencies...")
# try:
#     #subprocess.run(["source", "/usr/local/bin/virtualenvwrapper.sh"], shell=True, check=True)
#     subprocess.run(["mkvirtualenv", "ui"], check=True)
#     subprocess.run(["workon", "ui"], shell=True, check=True)
#     subprocess.run(["pip3", "install", "opencv-python==4.6.0.66", "opencv-contrib-python==4.6.0.66"], check=True)
#     print("OpenCV and dependencies installed successfully.")
# except subprocess.CalledProcessError as e:
#     print(f"Failed to install OpenCV and dependencies: {e}", file=sys.stderr)
#     exit(1)

# # Step 9: Install Numba
# print("Installing Numba...")
# try:
#     subprocess.run(["pip3", "install", "numba"], check=True)
#     print("Numba installed successfully.")
# except subprocess.CalledProcessError:
#     print("Failed to install Numba.", file=sys.stderr)
#     exit(1)

# # Step 10: Install PyQt5
# print("Installing PyQt5...")
# try:
#     subprocess.run(["pip3", "install", "pyqt5"], check=True)
#     print("PyQt5 installed successfully.")
# except subprocess.CalledProcessError:
#     print("Failed to install PyQt5.", file=sys.stderr)
#     exit(1)

# Step 11: Instruction for pymongo installation
print("Please open a new terminal window (do not activate the 'ui' virtual environment) and run the following command to install pymongo:")
print("pip3 install pymongo")
#subprocess.run(["gnome-terminal", "--", "bash", "-c", "pip3 install pymongo; exec bash"], check=True)
subprocess.run(["pip3", "install", "pymongo"], check=True)