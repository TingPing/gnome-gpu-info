pkglib_LTLIBRARIES = librg.la

librg_la_SOURCES = \
	realtime-graphs.h \
	rg-column.c \
	rg-column.h \
	rg-column-private.h \
	rg-graph.c \
	rg-graph.h \
	rg-line-renderer.c \
	rg-line-renderer.h \
	rg-renderer.c \
	rg-renderer.h \
	rg-ring.c \
	rg-ring.h \
	rg-table.c \
	rg-table.h \ 
	egg-signal-group.c \
	egg-signal-group.h

librg_la_CFLAGS = \
	$(RG_CFLAGS)

librg_la_LIBADD = \
	$(RG_LIBS)

librg_la_LDFLAGS = \
	$(RG_LDFLAGS)

include $(INTROSPECTION_MAKEFILE)
if HAVE_INTROSPECTION
Rg-0.1.gir: librg.la
Rg_0_1_gir_CFLAGS = $(librg_la_CFLAGS)
Rg_0_1_gir_INCLUDES = Gtk-3.0 Gio-2.0
Rg_0_1_gir_LIBS = librg.la
Rg_0_1_gir_FILES = $(filter-out egg-%,$(librg_la_SOURCES))
Rg_0_1_gir_SCANNERFLAGS = --warn-all --c-include="realtime-graphs.h"
INTROSPECTION_GIRS = Rg-0.1.gir

pkgdata_DATA = $(INTROSPECTION_GIRS)
typelibsdir = $(pkglibdir)
typelibs_DATA = $(INTROSPECTION_GIRS:.gir=.typelib)

BUILT_SOURCES = $(pkgdata_DATA) $(pkglib_DATA)
CLEANFILES = $(BUILT_SOURCES)
endif

