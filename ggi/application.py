# Copyright (C) 2015 Patrick Griffis <tingping@tingping.se>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import signal
from gettext import gettext as _

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio, GLib

from .window import GGIWindow

class GGIApplication(Gtk.Application):

	__gtype_name__ = 'GGIApplication'

	def __init__(self):
		Gtk.Application.__init__(self, application_id='org.gnome.gpu-info',
		                         flags=Gio.ApplicationFlags.FLAGS_NONE)
		self.window = None

	def do_startup(self):
		Gtk.Application.do_startup(self)
		signal.signal(signal.SIGINT, signal.SIG_DFL) # Handle Ctrl+C

		action = Gio.SimpleAction.new("about", None)
		action.connect("activate", self.about_cb)
		self.add_action(action)

		action = Gio.SimpleAction.new("quit", None)
		action.connect("activate", self.quit_cb)
		self.add_action(action)

	def do_activate(self):
		if not self.window:
			self.window = GGIWindow(application=self)
			self.window.show_all()

		self.window.present()

	def do_shutdown(self):
		Gtk.Application.do_shutdown(self)
		self.window.destroy()

	def about_cb(self, action, param):
		about = Gtk.AboutDialog(transient_for=self.window, modal=True,
		                        program_name="Gnome GPU Info", license_type=Gtk.License.GPL_3_0,
		                        authors=['Patrick Griffis',])
		about.show()

	def quit_cb(self, action, param):
		self.quit()

def main():
    app = GGIApplication()
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)

if __name__ == '__main__':
    main()
