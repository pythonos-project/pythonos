import sys
import subprocess
from pathlib import Path
import os
from .. import translations as langs


def main():
    if len(sys.argv) < 2:
        print("Uso: python select_lang.py <lingua>")
        sys.exit(1)

    lang_name = sys.argv[1]

    try:
        lang_function = getattr(langs, lang_name)
    except AttributeError:
        print(f"La lingua '{lang_name}' non esiste.")
        sys.exit(1)

    if callable(lang_function):
        lang_function()
    else:
        print(f"'{lang_name}' non è una funzione.")


if __name__ == "__main__":
    main()
