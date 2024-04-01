import subprocess
import os

# Create a Python virtual environment
subprocess.run(["python", "-m", "venv", ".venv"])

# Activate the virtual environment
subprocess.run([".venv\\Scripts\\activate.bat"], shell=True)

# Check if requirements.txt exists

if os.path.exists("requirements.txt"):
    # Install requirements from requirements.txt
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
else:
    print("requirements.txt file not found.")

# Check if prefect is installed
try:
    import prefect
    print("Prefect is installed.")
except ImportError:
    print("Prefect is not installed. Installing...")
    subprocess.run(["pip", "install", "prefect"])

# Run prefect init
subprocess.run(["prefect", "init"])