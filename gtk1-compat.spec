Name:		gtk1-compat
Summary:	Compatibility Wrappers for Old Versions of GLib, GTK+, GDK-Pixbuf, and libglade
Version:	0.9
Release:	0.1
License:	GNU Library General Public License v. 2.0 and 2.1 (LGPL)
Group:		Libraries
# http://download.opensuse.org/distribution/10.2/repo/src-oss/suse/src/gtk1-compat-0.9-2.src.rpm
Source0:	%{name}-%{version}.tar.bz2
# Source0-md5:	87e29c60512560a1cd2f50ea6129181e
BuildRequires:	libglade2-devel
BuildRequires:	libxml2-devel
BuildRequires:	gtk+2-devel
Requires:	libxml2-devel
Requires:	libglade2-devel
Requires:	pkgconfig
Requires:	python
Requires:	glib2-devel
Requires:	gtk+2-devel
Conflicts:	libglade-devel
Conflicts:	glib-devel
Conflicts:	gtk-devel
Conflicts:	gdk-pixbuf-devel
Conflicts:	libxml-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wrapper headers, M4 macros, configuration scripts, and library
symlinks, which simulate the presence of GLib1, GTK+1, GDK-Pixbuf1,
and libglade1 development packages, but use GLib2, GTK+2, and
libglade2.

Using it, you can forcibly link some old applications with new
libraries without any effort.

The package also provides the gtk1-compat-autofix script, which does
some source code modifications that cannot be worked around any other
way, and a static library with some obsolete functions.

Authors:
  Stanislav Brabec <sbrabec@suse.cz>

%prep
%setup -q

%build
%configure

cd m4macros
cp %{_aclocaldir}/gtk-2.0.m4 gtk.m4
patch < gtk_m4.patch
cd ..

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_aclocaldir}/*
%{_pkgconfigdir}/*
%{_includedir}/*
%{_libdir}/*.a
