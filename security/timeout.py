import subprocess
import sys
import time

subprocess.Popen([sys.executable, "-I", "-c", "import time; time.sleep(60)"])
time.sleep(60)
