import platform
import subprocess
import sys

def install_requirements():
    system = platform.system().lower()
    if system == "windows":
        req_file = "requirements.txt"
    else:
        req_file = "requirements.linux.txt"

    print(f"🔧 Installing dependencies from: {req_file}")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", req_file])
    except subprocess.CalledProcessError as e:
        print(f"❌ Error during installation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_requirements()
