import subprocess
import sys

def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError:
        print(f"Error: Failed to execute command: {command}")
        revert_changes()
        sys.exit(1)

def revert_changes():
    # Add commands to revert any changes made during the installation process
    print("Reverting changes...")
    # Example: Reverting Docker installation
    subprocess.run("sudo apt remove --purge -y docker-ce docker-ce-cli containerd.io", shell=True, check=True)
    subprocess.run("sudo rm -rf /var/lib/docker", shell=True, check=True)
    # Example: Reverting NVIDIA Container Toolkit installation
    subprocess.run("sudo apt remove --purge -y nvidia-docker2", shell=True, check=True)
    subprocess.run("sudo rm /etc/apt/sources.list.d/nvidia-docker.list", shell=True, check=True)
    subprocess.run("sudo apt-key del AAB75B78B3C1F4AD5ACA6D2935D3E26772C5B491", shell=True, check=True)

def main():
    print("Updating packages and installing dependencies...")
    #run_command("script")
    run_command("sudo apt update && sudo apt -y upgrade")
    run_command("sudo apt install -y curl python3-pip nano")

    print("Installing Docker...")
    run_command("curl https://get.docker.com | sh && sudo systemctl --now enable docker")
    run_command("docker --version")

    print("Setting up NVIDIA Container Toolkit...")
    run_command("distribution=$(. /etc/os-release;echo $ID$VERSION_ID) \
                && curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add - \
                && curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list")
    run_command("sudo apt-get update")
    run_command("sudo apt-get install -y nvidia-docker2")
    run_command("sudo systemctl restart docker")

    print("Testing NVIDIA Docker installation...")
    run_command("sudo docker run --rm --gpus all nvidia/cuda:11.6.2-base-ubuntu20.04 nvidia-smi")

    print("Installation completed successfully!")

if __name__ == "__main__":
    main()
