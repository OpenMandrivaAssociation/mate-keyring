%define	major	0
%define libgcr	%mklibname mategcr %{major}
%define libgck	%mklibname mategck %{major}
%define devname	%mklibname mate-keyring -d

Summary:	Keyring and password manager for the MATE desktop
Name:		mate-keyring
Version:	1.4.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Networking/Remote access
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz

BuildRequires:	gtk-doc
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	libtasn1-tools
BuildRequires:	libgcrypt-devel
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(dbus-1) >= 1.0
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libtasn1)

#gw for keyring management GUI
#Suggests:	seahorse

%description
mate-keyring is a program that keep password and other secrets for
users. It is run as a damon in the session, similar to ssh-agent, and
other applications can locate it by an environment variable.
 
The program can manage several keyrings, each with its own master
password, and there is also a session keyring which is never stored to
disk, but forgotten when the session ends.

%package -n %{libgcr}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libgcr}
This package contains a shared library for %{name}.

%package -n %{libgck}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libgck}
This package contains a shared library for %{name}.

%package -n %{devname}
Group: Development/C
Summary: Development files for %{name}
Requires: %{libgcr} = %{version}-%{release}
Requires: %{libgck} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
%autopatch -p1

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-static \
	--enable-pam \
	--with-pam-dir=/%{_lib}/security \
	--disable-schemas-compile

%make LIBS='-lgmodule-2.0' 

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc README NEWS
%{_sysconfdir}/xdg/autostart/%{name}-gpg.desktop
%{_sysconfdir}/xdg/autostart/%{name}-pkcs11.desktop
%{_sysconfdir}/xdg/autostart/%{name}-secrets.desktop
%{_sysconfdir}/xdg/autostart/%{name}-ssh.desktop
%{_bindir}/%{name}
%{_bindir}/%{name}-daemon
/%{_lib}/security/pam_mate*.so
%{_libdir}/%{name}
%{_libdir}/mate-keyring-prompt
%{_libdir}/pkcs11
%{_datadir}/MateConf/gsettings/org.mate.crypto.cache.convert
%{_datadir}/MateConf/gsettings/org.mate.crypto.pgp.convert
%{_datadir}/dbus-1/services/org.mate-freedesktop.secrets.service
%{_datadir}/dbus-1/services/org.mate.keyring.service
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/mate-keyring
%{_datadir}/mategcr

%files -n %{libgcr}
%{_libdir}/libmategcr.so.%{major}*

%files -n %{libgck}
%{_libdir}/libmategck.so.%{major}*

%files -n %{devname}
%{_libdir}/libmategcr.so
%{_libdir}/libmategck.so
%{_libdir}/pkgconfig/mate-gcr-0.pc
%{_libdir}/pkgconfig/mate-gck-0.pc
%dir %{_includedir}/gck
%{_includedir}/gck/*
%dir %{_includedir}/mate-gck
%{_includedir}/mate-gck/*
%dir %{_includedir}/mategcr
%dir %{_includedir}/mategcr/gcr
%{_includedir}/mategcr/gcr/*
%doc %{_datadir}/gtk-doc/*



%changelog
* Mon Jul 30 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.4.0-1
+ Revision: 811416
- fix files list

  + Matthew Dawkins <mattydaw@mandriva.org>
    - new version 1.4.0

* Thu May 31 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 801631
- imported package mate-keyring

