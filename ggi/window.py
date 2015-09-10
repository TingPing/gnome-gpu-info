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

from gi.repository import Gtk, GObject, Gio, GLib
from ._gi_composites import GtkTemplate

from .gpu_intel import IntelGpu
from .gpu_graph import GpuUsageGraph

@GtkTemplate(ui='resource:///org/gnome/gpu-info/ui/window.ui')
class GGIWindow(Gtk.ApplicationWindow):

	__gtype_name__ = 'GGIWindow'

	usage_box = GtkTemplate.Child()
	temp_box = GtkTemplate.Child()
	clock_box = GtkTemplate.Child()

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.init_template()

		# TODO: detect gpus
		gpu = IntelGpu()

		usage_graph = GpuUsageGraph(gpu)
		self.usage_box.pack_start(usage_graph, True, True, 0)

