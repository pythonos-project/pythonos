import sys
import subprocess
from pathlib import Path
import os

ROOT_DIR = Path(__file__).parent.parent

if len(sys.argv) > 1 and sys.argv[1] == "compile":
    subprocess.run(
        [sys.executable, "-m", "pip", "install", "pyinstaller"],
        check=True
    )

    subprocess.run(
        [
            sys.executable,
            "-m",
            "PyInstaller",
            "--onefile",
            "--hidden-import=pyos_gaps",
            str(ROOT_DIR / "main.py"),
            "--name=pythonos",
        ],
        check=True
    )

    print("Compilazione completata! Si trova in:", end=" ")

    if os.name == "nt":
        print(ROOT_DIR / "dist" / "pythonos.exe")
    else:
        print(ROOT_DIR / "dist" / "pythonos")

else:
    print("CLI PythonOS")
