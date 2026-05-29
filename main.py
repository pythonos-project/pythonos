from pyos_gaps.decorators import verify_pyos_dir
import os

os.path.abspath(os.path.dirname(__file__))

verify_pyos_dir()

from pythonos.gui import PythonOSApp

def main():    
    app = PythonOSApp()
    app.run()

if __name__ == "__main__":
    main()