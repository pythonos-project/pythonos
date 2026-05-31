# PythonOS

PythonOS è un mini-sistema operativo sviluppato in Python con interfaccia grafica Tkinter.

![GitHub Repo stars](https://img.shields.io/github/stars/pythonos-project/pythonos)
![GitHub followers](https://img.shields.io/github/followers/pythonos-project)
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
![version](https://img.shields.io/badge/versione-v1.0.0-green)
[![Python version](https://img.shields.io/badge/python-3.8_|_3.9_|_3.10_|_3.11_|_3.12_|_3.13_|_3.14-blue)](#requisiti)

---

## Tabella dei Contenuti

- [Caratteristiche](#caratteristiche)
- [Requisiti](#requisiti)
- [Installazione ed Esecuzione](#installazione-ed-esecuzione)
- [Struttura del progetto](#struttura-del-progetto)
- [Note](#note)
---


## Caratteristiche

- Interfaccia desktop stile mini-OS con barre e icone
- Finestre interne trascinabili per app multiple
- Terminale integrato
- Editor di appunti
- File manager
- Impostazioni di sistema e lockscreen

---

## Requisiti

- Python 3.8+ (Raccomandati 3.9+)
- tkinter (incluso con la maggior parte delle distribuzioni Python)
- pyos-gaps (Si installa automaticamente installando le dispendenze con `pip install -r requirements.txt`)

---

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

---

## Struttura del progetto

- `main.py` - punto di ingresso dell'applicazione
- `pythonos/gui.py` - logica dell'interfaccia grafica
- `pythonos/os.py` - stato e comandi del mini-OS
- `translations/` - Traduzioni
- `clis/` - Le varie CLIs di PythonOS
- `docs/` - Documentazione

---

## Note

Questo progetto è pensato come base per un mini-sistema operativo in Python e può essere esteso con nuove applicazioni e funzionalità.
