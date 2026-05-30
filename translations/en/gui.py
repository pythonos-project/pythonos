import tkinter as tk
from tkinter import messagebox, scrolledtext
from datetime import datetime
from .os import OSState


class AppWindow:
    def __init__(self, parent, title, width=520, height=340, x=40, y=40):
        self.parent = parent
        self.frame = tk.Frame(parent, bg="#3b3d59", bd=2, relief="raised")
        self.frame.place(x=x, y=y, width=width, height=height)

        self.title_bar = tk.Frame(self.frame, bg="#44475a", height=32)
        self.title_bar.pack(fill="x")

        self.title_label = tk.Label(self.title_bar, text=title, fg="#f8f8f2", bg="#44475a", font=("Segoe UI", 10, "bold"))
        self.title_label.pack(side="left", padx=8)

        self.close_btn = tk.Button(self.title_bar, text="✕", bg="#ff5555", fg="#f8f8f2", bd=0, width=3, command=self.close)
        self.close_btn.pack(side="right", padx=4, pady=2)

        self.content = tk.Frame(self.frame, bg="#282a36")
        self.content.pack(expand=True, fill="both")

        self._drag_data = {"x": 0, "y": 0}
        self.title_bar.bind("<ButtonPress-1>", self._start_drag)
        self.title_bar.bind("<ButtonRelease-1>", self._stop_drag)
        self.title_bar.bind("<B1-Motion>", self._do_drag)

    def _start_drag(self, event):
        self._drag_data["x"] = event.x
        self._drag_data["y"] = event.y

    def _stop_drag(self, event):
        self._drag_data["x"] = 0
        self._drag_data["y"] = 0

    def _do_drag(self, event):
        dx = event.x - self._drag_data["x"]
        dy = event.y - self._drag_data["y"]
        x = self.frame.winfo_x() + dx
        y = self.frame.winfo_y() + dy
        self.frame.place(x=x, y=y)

    def close(self):
        self.frame.destroy()


class PythonOSApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("PythonOS")
        self.root.geometry("1000x650")
        self.root.configure(bg="#1f1f2e")
        self.root.minsize(900, 600)

        self.state = OSState()
        self.windows = []
        self.start_menu = None
        self.lock_screen = None

        self._build_ui()
        self._show_welcome()
        self._show_lock_screen()
        self._update_clock()

    def _build_ui(self):
        self.top_bar = tk.Frame(self.root, bg="#1f1f2e", height=36)
        self.top_bar.pack(side="top", fill="x")

        self.start_btn = tk.Button(self.top_bar, text="Start", command=self._toggle_start_menu, bg="#6272a4", fg="#f8f8f2", bd=0, padx=12, pady=4)
        self.start_btn.pack(side="left", padx=8, pady=4)

        self.status_label = tk.Label(self.top_bar, text="Pronto", bg="#1f1f2e", fg="#f8f8f2", font=("Segoe UI", 9))
        self.status_label.pack(side="left", padx=12)

        self.clock_label = tk.Label(self.top_bar, text="00:00", bg="#1f1f2e", fg="#f8f8f2", font=("Segoe UI", 9, "bold"))
        self.clock_label.pack(side="right", padx=12)

        self.sidebar = tk.Frame(self.root, bg="#2b2b44", width=180)
        self.sidebar.pack(side="left", fill="y")

        self.desktop = tk.Frame(self.root, bg="#282a36")
        self.desktop.pack(side="right", expand=True, fill="both")

        title = tk.Label(self.sidebar, text="PythonOS", fg="#f8f8f2", bg="#2b2b44", font=("Segoe UI", 18, "bold"))
        title.pack(pady=20)

        self._add_sidebar_button("Terminal", self.open_terminal)
        self._add_sidebar_button("Notes", self.open_notes)
        self._add_sidebar_button("File Manager", self.open_file_manager)
        self._add_sidebar_button("Settings", self.open_settings)
        self._add_sidebar_button("Lock screen", self._show_lock_screen)

        self.status_bar = tk.Label(self.root, text="PythonOS mini-OS ready", bg="#1f1f2e", fg="#f8f8f2", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")

    def _add_sidebar_button(self, text, command):
        btn = tk.Button(self.sidebar, text=text, command=command, bg="#6272a4", fg="#f8f8f2", relief="flat")
        btn.pack(fill="x", padx=20, pady=8)

    def _show_welcome(self):
        for widget in self.desktop.winfo_children():
            widget.destroy()

        wallpaper = tk.Label(self.desktop, bg="#282a36")
        wallpaper.pack(expand=True, fill="both")

        self._create_desktop_icon(wallpaper, "Terminal", self.open_terminal, 60, 80)
        self._create_desktop_icon(wallpaper, "Notes", self.open_notes, 160, 80)
        self._create_desktop_icon(wallpaper, "File Manager", self.open_file_manager, 260, 80)
        self._create_desktop_icon(wallpaper, "Settings", self.open_settings, 360, 80)

        welcome = tk.Label(wallpaper, text=f"Welcome, {self.state.user_name}", fg="#f8f8f2", bg="#282a36", font=("Segoe UI", 24, "bold"))
        welcome.place(x=60, y=20)

        subtitle = tk.Label(wallpaper, text="PythonOS Operating System - Open an app from the desktop or sidebar.", fg="#f8f8f2", bg="#282a36", font=("Segoe UI", 11))
        subtitle.place(x=60, y=60)

    def _create_desktop_icon(self, parent, text, command, x, y):
        icon = tk.Button(parent, text=text, command=command, bg="#44475a", fg="#f8f8f2", bd=0, width=12, height=3)
        icon.place(x=x, y=y)

    def _toggle_start_menu(self):
        if self.start_menu and self.start_menu.winfo_exists():
            self.start_menu.destroy()
            self.start_menu = None
            return

        self.start_menu = tk.Frame(self.root, bg="#3b3d59", bd=2, relief="raised")
        self.start_menu.place(x=10, y=42, width=200, height=220)

        apps = [
            ("Terminale", self.open_terminal),
            ("Appunti", self.open_notes),
            ("File Manager", self.open_file_manager),
            ("Impostazioni", self.open_settings),
            ("Blocca", self._show_lock_screen),
        ]
        for idx, (name, action) in enumerate(apps):
            btn = tk.Button(self.start_menu, text=name, command=lambda action=action: [action(), self._toggle_start_menu()], bg="#6272a4", fg="#f8f8f2", relief="flat")
            btn.pack(fill="x", padx=10, pady=5)

    def _show_lock_screen(self):
        if self.lock_screen and self.lock_screen.winfo_exists():
            return

        self.lock_screen = tk.Frame(self.root, bg="#0f101a")
        self.lock_screen.place(relx=0, rely=0, relwidth=1, relheight=1)

        label = tk.Label(self.lock_screen, text="System Locked", fg="#f8f8f2", bg="#0f101a", font=("Segoe UI", 28, "bold"))
        label.pack(pady=80)

        pin_label = tk.Label(self.lock_screen, text="Enter PIN to unlock", fg="#f8f8f2", bg="#0f101a", font=("Segoe UI", 12))
        pin_label.pack(pady=10)

        self.pin_entry = tk.Entry(self.lock_screen, show="*", width=16, justify="center", font=("Segoe UI", 12))
        self.pin_entry.pack(pady=10)
        self.pin_entry.focus_set()

        unlock_btn = tk.Button(self.lock_screen, text="Unlock", command=self._unlock_screen, bg="#50fa7b", fg="#282a36", relief="flat", padx=12, pady=6)
        unlock_btn.pack(pady=10)

        self.lock_status = tk.Label(self.lock_screen, text="", fg="#ff5555", bg="#0f101a", font=("Segoe UI", 10))
        self.lock_status.pack(pady=4)

        self.root.bind("<Return>", self._unlock_screen_event)

    def _unlock_screen_event(self, event):
        if self.lock_screen and self.lock_screen.winfo_exists():
            self._unlock_screen()

    def _unlock_screen(self):
        if self.pin_entry.get() == self.state.lock_code:
            self.lock_screen.destroy()
            self.lock_screen = None
            self.status_bar.config(text="Screen unlocked")
        else:
            self.lock_status.config(text="Incorrect PIN. Try again.")
            self.pin_entry.delete(0, "end")

    def open_terminal(self):
        self.status_bar.config(text="Open terminal")
        self._open_terminal_window()

    def open_notes(self):
        self.status_bar.config(text="Open notes")
        self._open_notes_window()

    def open_file_manager(self):
        self.status_bar.config(text="File Manager open")
        self._open_file_manager_window()

    def open_settings(self):
        self.status_bar.config(text="Open Settings")
        self._open_settings_window()

    def open_about(self):
        messagebox.showinfo(
            "About PythonOS",
            "PythonOS is a mini-operating system built with Python and Tkinter.\n"
            "Version: 1.0.1 Stable",
        )

    def _open_terminal_window(self):
        window = AppWindow(self.desktop, "Terminal", width=520, height=320, x=120, y=120)
        console = scrolledtext.ScrolledText(window.content, bg="#1e1f2b", fg="#f8f8f2", insertbackground="#f8f8f2")
        console.pack(expand=True, fill="both", padx=10, pady=10)
        console.insert("end", "PythonOS Terminal\n> type 'help' and press Enter\n")
        console.bind("<Return>", lambda event: self._handle_terminal_command(console))
        self.windows.append(window)

    def _handle_terminal_command(self, console):
        text = console.get("1.0", "end-1c").strip().splitlines()[-1]
        command = text.replace("> ", "").strip()
        response = self.state.run_command(command)
        console.insert("end", f"\n{response}\n> ")
        console.see("end")
        return "break"

    def _open_notes_window(self):
        window = AppWindow(self.desktop, "Notes", width=520, height=320, x=140, y=130)
        text_area = scrolledtext.ScrolledText(window.content, bg="#1f1f2b", fg="#f8f8f2")
        text_area.pack(expand=True, fill="both", padx=10, pady=10)
        text_area.insert("1.0", self.state.notes)

        def save_notes():
            self.state.notes = text_area.get("1.0", "end-1c")
            self.status_bar.config(text="Appunti salvati")

        save_btn = tk.Button(window.content, text="Save", command=save_notes, bg="#50fa7b", fg="#282a36", relief="flat")
        save_btn.pack(pady=8)
        self.windows.append(window)

    def _open_file_manager_window(self):
        window = AppWindow(self.desktop, "File Manager", width=520, height=320, x=160, y=140)
        files_text = tk.Text(window.content, bg="#1e1f2b", fg="#f8f8f2")
        files_text.pack(expand=True, fill="both", padx=10, pady=10)
        files_text.insert("1.0", "\n".join(self.state.get_file_listing()))
        files_text.config(state="disabled")
        self.windows.append(window)

    def _open_settings_window(self):
        window = AppWindow(self.desktop, "Settings", width=520, height=340, x=180, y=160)

        theme_label = tk.Label(window.content, text="Theme:", fg="#f8f8f2", bg="#282a36", font=("Segoe UI", 10, "bold"))
        theme_label.pack(anchor="w", padx=12, pady=(12, 4))

        theme_frame = tk.Frame(window.content, bg="#282a36")
        theme_frame.pack(anchor="w", padx=12)
        light_btn = tk.Button(theme_frame, text="Light", command=lambda: self._set_theme("light"), bg="#50fa7b", fg="#282a36", relief="flat")
        dark_btn = tk.Button(theme_frame, text="Dark", command=lambda: self._set_theme("dark"), bg="#6272a4", fg="#f8f8f2", relief="flat")
        light_btn.pack(side="left", padx=4)
        dark_btn.pack(side="left", padx=4)

        username_label = tk.Label(window.content, text="User name:", fg="#f8f8f2", bg="#282a36", font=("Segoe UI", 10, "bold"))
        username_label.pack(anchor="w", padx=12, pady=(12, 4))
        username_entry = tk.Entry(window.content, bg="#1e1f2b", fg="#f8f8f2", insertbackground="#f8f8f2")
        username_entry.insert(0, self.state.user_name)
        username_entry.pack(fill="x", padx=12)

        lock_label = tk.Label(window.content, text="Screen lock PIN:", fg="#f8f8f2", bg="#282a36", font=("Segoe UI", 10, "bold"))
        lock_label.pack(anchor="w", padx=12, pady=(12, 4))
        lock_entry = tk.Entry(window.content, bg="#1e1f2b", fg="#f8f8f2", insertbackground="#f8f8f2")
        lock_entry.insert(0, self.state.lock_code)
        lock_entry.pack(fill="x", padx=12)

        
        def save_settings():
            self.state.user_name = username_entry.get().strip() or self.state.user_name
            self.state.lock_code = lock_entry.get().strip() or self.state.lock_code
            self.status_bar.config(text="Impostazioni salvate")
            self._show_welcome()

        info_label = tk.Button(window.content, text="System Information", command=self.open_about, bg="#6272a4", fg="#f8f8f2", relief="flat")
        info_label.pack(pady=12)

        save_btn = tk.Button(window.content, text="Save settings", command=save_settings, bg="#50fa7b", fg="#282a36", relief="flat")
        save_btn.pack(pady=12)

        self.windows.append(window)

    def _set_theme(self, theme_name):
        self.state.theme = theme_name
        if theme_name == "light":
            self.desktop.configure(bg="#dcdde1")
            self.status_bar.config(bg="#f0f0f0", fg="#1f1f2e")
            self.top_bar.config(bg="#f0f0f0")
            self.status_label.config(bg="#f0f0f0", fg="#1f1f2e")
            self.clock_label.config(bg="#f0f0f0", fg="#1f1f2e")
        else:
            self.desktop.configure(bg="#282a36")
            self.status_bar.config(bg="#1f1f2e", fg="#f8f8f2")
            self.top_bar.config(bg="#1f1f2e")
            self.status_label.config(bg="#1f1f2e", fg="#f8f8f2")
            self.clock_label.config(bg="#1f1f2e", fg="#f8f8f2")
        self.status_bar.config(text=f"Tema impostato su {theme_name}")

    def _update_clock(self):
        self.clock_label.config(text=datetime.now().strftime("%H:%M"))
        self.root.after(1000, self._update_clock)

    def run(self):
        self.root.mainloop()
