ACLOCAL_AMFLAGS = -I m4

pypkgdir = $(pythondir)/ggi
pypkg_PYTHON = $(wildcard ggi/*py)

bin_SCRIPTS = bin/gnome-gpu-info
bin/gnome-gpu-info: bin/gnome-gpu-info.in
	$(AM_V_GEN)sed                          \
		-e s!\@prefix\@!$(prefix)!          \
		-e s!\@datadir\@!$(datadir)!        \
		-e s!\@pkgdatadir\@!$(pkgdatadir)!  \
		-e s!\@pkglibdir\@!$(pkglibdir)!    \
		-e s!\@localedir\@!$(localedir)!    \
		-e s!\@pythondir\@!$(pythondir)!    \
		-e s!\@pyexecdir\@!$(pyexecdir)!    \
		< $< > $@
	chmod a+x $@

pkgdata_DATA = ggi.gresource
ggi.gresource: data/ggi.gresource.xml $(shell $(GLIB_COMPILE_RESOURCES) --sourcedir=data --generate-dependencies data/ggi.gresource.xml)
	$(AM_V_GEN) $(GLIB_COMPILE_RESOURCES) --target=$@ --sourcedir=data --generate $<

polkit_policydir = $(datadir)/polkit-1/actions
polkit_policy_in_files = data/org.gnome.gpu-info.policy.in
polkit_policy_DATA = $(polkit_policy_in_files:.policy.in=.policy)
@INTLTOOL_POLICY_RULE@

run: ggi.gresource bin/gnome-gpu-info
	$(srcdir)/bin/gnome-gpu-info

BUILT_SOURCES = bin/gnome-gpu-info ggi.gresource
CLEANFILES = $(BUILT_SOURCES)
SUBDIRS = po contrib/rg
EXTRA_DIST = autogen.sh .editorconfig
