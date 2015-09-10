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

import re

from gi.repository import GLib, GObject, Gio

from .gpu import Gpu

class IntelGpu(Gpu):

	def __init__(self):
		Gpu.__init__(self)

		#return
		self.cancel = Gio.Cancellable()
		try:
			# FIXME: Not closing on shutdown
			# TODO: Poll rate
			launcher = Gio.SubprocessLauncher.new(Gio.SubprocessFlags.STDOUT_PIPE)
			proc = launcher.spawnv(['pkexec', 'intel_gpu_top', '-o', '-'])
			stream = proc.get_stdout_pipe()
			data_stream = Gio.DataInputStream.new(stream)
			data_stream.read_line_async(GLib.PRIORITY_LOW, self.cancel, self.on_new_data)
		except GLib.GError as e:
			print(e)

	def on_new_data(self, stream, res, data=None):
		try:
			output = stream.read_line_finish_utf8(res)

			if output[0][0] != '#': # First line is the column titles
				self.usage = int(re.split(r'\s+', output[0], maxsplit=2)[1])

			stream.read_line_async(GLib.PRIORITY_LOW, self.cancel, self.on_new_data)
		except GLib.GError as e:
			print(e)

