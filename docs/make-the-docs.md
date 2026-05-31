# Mettere i Docs

Digitate:

```bash
pip install flask markdown
```

Avviate il server:

```bash
python pyos_docs.py
```

---

# `pyos_docs.py`

```python
from flask import Flask, abort
import markdown
import os

app = Flask(__name__)

@app.route("/pyos-docs/<path:file>")
def docs(file):
    if not os.path.exists(file):
        abort(404)

    if not file.endswith(".md"):
        abort(403)

    with open(file, "r", encoding="utf-8") as f:
        md = f.read()

    html = markdown.markdown(
        md,
        extensions=["fenced_code", "tables"]
    )

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>{file}</title>
        <style>
            body {{
                max-width: 900px;
                margin: auto;
                font-family: Arial, sans-serif;
                padding: 20px;
            }}
            pre {{
                background: #f4f4f4;
                padding: 10px;
                overflow-x: auto;
            }}
            code {{
                background: #eee;
                padding: 2px 4px;
            }}
        </style>
    </head>
    <body>
        {html}
    </body>
    </html>
    """

app.run(host="0.0.0.0", port=8000)
```

Ora potrai aprire http://localhost:8000/pyos-docs/01-start.md e http://localhost:8000/pyos-docs/02-apps.md
