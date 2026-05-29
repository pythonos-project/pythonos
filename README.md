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

## Installazione ed Esecuzione

1. Clona il repository:

```bash
https://github.com/pythonos-project/pythonos.git
```

2. Crea un ambiente virtuale:

```bash
python -m venv venv
```

3. Attiva l'ambiente:

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
  source venv\bin\activate
  ```

  </details>

4. Installa le dipendenze:

```bash
pip install -r requirements.txt
```

5. Eseguiscilo

```bash
python main.py
```

## Struttura del progetto

- `main.py` - punto di ingresso dell'applicazione
- `pythonos/gui.py` - logica dell'interfaccia grafica
- `pythonos/os.py` - stato e comandi del mini-OS

## Note

Questo progetto è pensato come base per un mini-sistema operativo in Python e può essere esteso con nuove applicazioni e funzionalità.
