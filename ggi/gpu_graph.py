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

import gi
gi.require_version('Rg', '0.1')
from gi.repository import GLib, GObject, Rg

from .gpu import Gpu

class GpuGraph(Rg.Graph, GObject.Object):

	gpu = GObject.Property(type=Gpu)

	def __init__(self, gpu, name=''):
		Rg.Graph.__init__(self)
		self.gpu = gpu

		self.table = Rg.Table()
		column = Rg.Column.new(name, float)
		self.table.add_column(column)

		renderer = Rg.LineRenderer(column=0, stroke_color='#73d216')
		self.add_renderer(renderer)

		self.set_table(self.table)

class GpuUsageGraph(GpuGraph):

	def __init__(self, *args, **kwargs):
		GpuGraph.__init__(self, *args, name='usage', **kwargs)

		self.gpu.connect('notify::usage', self.on_usage)

	def on_usage(self, obj, spec):
		it = self.table.push(GLib.get_monotonic_time())
		it.set_column(0, self.gpu.props.usage)

