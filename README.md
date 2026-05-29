# PythonOS

PythonOS è un mini-sistema operativo sviluppato in Python con interfaccia grafica Tkinter.

## Caratteristiche

- Interfaccia desktop stile mini-OS con barre e icone
- Finestre interne trascinabili per app multiple
- Terminale integrato
- Editor di appunti
- File manager
- Impostazioni di sistema e lockscreen

## Requisiti

- Python 3.8+
- tkinter (incluso con la maggior parte delle distribuzioni Python)

## Installazione

1. Crea un ambiente virtuale:

```bash
python -m venv venv
```

2. Attiva l'ambiente:

<details>
  <summary>Windows</summary>

  In **Powershell**
  ```powershell
  venv\Scripts\Activate
  ```

  In **Prompt dei comandi**
  ```cmd
  venv\Scripts\activate
  ```

  </details>

  <details>
  <summary>MacOS/Linux</summary>
    
  ```bash
  venv\bin\activate
  ```

  </details>

3. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

## Esecuzione

```bash
python main.py
```

## Struttura del progetto

- `main.py` - punto di ingresso dell'applicazione
- `pythonos/gui.py` - logica dell'interfaccia grafica
- `pythonos/os.py` - stato e comandi del mini-OS

## Note

Questo progetto è pensato come base per un mini-sistema operativo in Python e può essere esteso con nuove applicazioni e funzionalità.
