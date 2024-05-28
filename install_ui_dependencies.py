import subprocess

try:
    # Step 1: Install OpenCV and Dependencies
    print("Installing OpenCV and its dependencies...")
    subprocess.run(["pip3", "install", "opencv-python==4.6.0.66", "opencv-contrib-python==4.6.0.66"], check=True)
    print("OpenCV and its dependencies installed successfully.")
    
    # Step 2: Install Numba
    print("Installing Numba...")
    subprocess.run(["pip3", "install", "numba"], check=True)
    print("Numba installed successfully.")
    
    # Step 2: Install PyQt5
    print("Installing PyQt5...")
    subprocess.run(["pip3", "install", "pyqt5"], check=True)
    print("PyQt5 installed successfully.")

    print("All steps completed successfully.")
except subprocess.CalledProcessError as e:
    print(f"An error occurred: {e}")
