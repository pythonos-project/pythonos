class OSState:
    def __init__(self):
        self.user_name = "Usee"
        self.theme = "dark"
        self.lock_code = "1234"
        self.notes = ""
        self.files = [
            "document.txt",
            "image.png",
            "notes.md",
            "config.sys",
        ]

    def run_command(self, command: str) -> str:
        command = command.strip().lower()
        if command == "help":
            return (
                "Avaibile Commands:\n"
                "help - view this message\n"
                "list - view the files\n"
                "clear - clear the screen\n"
                "exit - close the terminal"
            )
        if command == "list":
            return "\n".join(self.files)
        if command == "clear":
            return "[screen cleared]"
        if command == "exit":
            return "Close the Terminal window or return to the desktop."
        if not command:
            return ""
        return f"Command not recognized: {command}"

    def get_file_listing(self):
        return [f"- {name}" for name in self.files]
