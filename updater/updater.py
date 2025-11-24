import os
import sys
import time
import shutil
import subprocess

def update(old_exe, new_exe, debug_mode):
    # Ensure main app closes
    time.sleep(0.5)

    # Try multiple times (Windows locks files briefly)
    for _ in range(50):
        try:
            os.remove(old_exe)
            break
        except PermissionError:
            time.sleep(0.1)

    # Replace old exe
    shutil.move(new_exe, old_exe)

    # Relaunch updated app
    if not debug_mode:
        print("starting exe path:", old_exe)
        subprocess.Popen([old_exe])

def main():
    # This will run in production when the App_Updater.exe is started with subprocess
    if len(sys.argv) != 4:
        return

    update(sys.argv[1], sys.argv[2], int(sys.argv[3]))

if __name__ == "__main__":
    main()
