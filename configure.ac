AC_PREREQ(2.68)
AC_INIT([gnome-gpu-info], [0.0.1], [https://github.com/TingPing])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_SRCDIR([ggi/__init__.py])

AM_INIT_AUTOMAKE([1.11 dist-xz no-dist-gzip foreign subdir-objects -Wall -Wno-portability])
AM_SILENT_RULES([yes])
AM_PATH_PYTHON([3.3])

AC_PROG_CC
AC_PROG_CC_C99
AC_PROG_INSTALL
AM_PROG_AR
PKG_PROG_PKG_CONFIG([0.28])
LT_PREREQ([2.2.0])
LT_INIT([disable-static])

GETTEXT_PACKAGE=gnome-gpu-info
AC_SUBST(GETTEXT_PACKAGE)
IT_PROG_INTLTOOL([0.50.0])

AC_PATH_PROG(GLIB_COMPILE_RESOURCES, glib-compile-resources)
GOBJECT_INTROSPECTION_CHECK([0.9.3], [require])
dnl TODO
dnl DESKTOP_FILE
dnl APPSTREAM_XML

AC_DEFINE([GLIB_VERSION_MIN_REQUIRED], [GLIB_VERSION_2_44], [Dont warn using older APIs])
AC_DEFINE([GLIB_VERSION_MAX_ALLOWED], [GLIB_VERSION_2_44], [Prevents using newer APIs])
PKG_CHECK_MODULES([RG], [
	gio-2.0 >= 2.44
	gtk+-3.0 >= 3.16
])

AX_APPEND_LINK_FLAGS([ \
	-pie \
	-Wl,-z,relro \
	-Wl,-z,now \
])

AX_APPEND_COMPILE_FLAGS([ \
	-std=gnu99 \
	-funsigned-char \
	-fstack-protector-strong \
	-fPIE \
	-fPIC \
	-Wall \
	-Wextra \
	-Wconversion \
	-Winline \
	-Wno-padded \
	-Wno-unused-parameter \
	-Wstrict-prototypes \
	-Wmissing-prototypes \
	-Werror=implicit-function-declaration \
	-Werror=pointer-arith \
	-Werror=init-self \
	-Werror=format-security \
	-Werror=format=2 \
	-Werror=missing-include-dirs \
	-Werror=date-time \
])

AC_CONFIG_FILES([
	Makefile
	contrib/rg/Makefile
	po/Makefile.in
])
AC_OUTPUT

echo "
    $PACKAGE $VERSION

    prefix: ${prefix}
"
