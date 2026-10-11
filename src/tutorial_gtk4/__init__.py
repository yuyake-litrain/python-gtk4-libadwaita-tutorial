import gi
from gi.repository import GLib, Gtk
gi.require_version("Gtk", "4.0")


class MyApp(Gtk.Application):
    def __init__(self):
        super().__init__(application_id="com.example.MyGtkApp")
        GLib.set_application_name('My Gtk Application')

    def do_activate(self):
        window = Gtk.ApplicationWindow(application=self, title="Hello World")
        window.present()


def main() -> None:
    app = MyApp()
    app.run()
    print("Hello from tutorial-gtk4!")
