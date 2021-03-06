import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

overlay = Gtk.Overlay()
window.add(overlay)

textview = Gtk.TextView()
textview.set_wrap_mode(Gtk.WrapMode.WORD_CHAR)
textbuffer = textview.get_buffer()
textbuffer.set_text("Welcome to the PyGObject Tutorial\n\nThis guide aims to provide an introduction to using Python and GTK+.\n\nIt includes many sample code files and exercises for building your knowledge of the language.", -1)
overlay.add(textview)

button = Gtk.Button(label="Overlayed Button")
button.set_valign(Gtk.Align.CENTER)
button.set_halign(Gtk.Align.CENTER)

image = Gtk.Image()
image.set_from_file("okaun_icon_alpha.png")
image.set_valign(Gtk.Align.CENTER)
image.set_halign(Gtk.Align.CENTER)

overlay.set_property("opacity",0.5)
overlay.add_overlay(image)
#overlay.add_overlay(button)

overlay.show_all()

window.show_all()

Gtk.main()
