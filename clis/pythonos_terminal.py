class PythonOSTerminal:
    def __init__(self):
        self.files = [
            "documento.txt",
            "immagine.png",
            "appunti.md",
            "config.sys"
        ]

    def run_command(self, command: str) -> str:
        command = command.strip().lower()

        if command == "help":
            return (
                "Comandi disponibili:\n"
                "help - mostra questo messaggio\n"
                "list - mostra i file\n"
                "clear - pulisce lo schermo\n"
                "exit - chiude il terminale"
            )

        if command == "list":
            return "\n".join(self.files)

        if command == "clear":
            return "[schermo pulito]"

        if command == "exit":
            return "Chiudi la finestra del terminale o torna al desktop."

        if not command:
            return ""

        return f"Comando non riconosciuto: {command}"

    def get_file_listing(self):
        return [f"- {name}" for name in self.files]


# Avvio del terminale
pythonosterminal = PythonOSTerminal()

while True:
    command = input("> ")
    result = pythonosterminal.run_command(command)

    print(result)
