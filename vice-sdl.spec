%define Werror_cflags %nil

%define oname	vice

Summary:	VICE, the Versatile Commodore Emulator
Name:		vice-sdl
Version:	2.3.14
Release:	%mkrel 1
License:	GPLv2
Group:		Emulators
Source0:	http://www.zimmers.net/anonftp/pub/cbm/crossplatform/emulators/VICE/%{oname}-%{version}.tar.gz
Source1:	vice-normalicons.tar.bz2
Source2:	vice-largeicons.tar.bz2
Source3:	vice-miniicons.tar.bz2
URL:		http://www.viceteam.org/
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	readline-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_sound-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(gdkglext-1.0)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xxf86vm)
BuildRequires:	flex
BuildRequires:	mkfontdir
BuildRequires:	bdftopcf
%rename		%{oname}

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%prep
%setup -q -n %{oname}-%{version}

%build
export CFLAGS="%{optflags} -DNO_REGPARM"
%configure2_5x --enable-sdlui --enable-fullscreen

%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

#xdg menu
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/mandriva-x64.desktop << EOF
[Desktop Entry]
Name=C64 Emulator
Comment=Commodore 64 Emulator
Exec=%{_bindir}/x64 %U
Icon=c64icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-x128.desktop << EOF
[Desktop Entry]
Name=C128 Emulator
Comment=Commodore 128 Emulator
Exec=%{_bindir}/x128 %U
Icon=c128icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xpet.desktop << EOF
[Desktop Entry]
Name=PET Emulator
Comment=Commodore PET Emulator
Exec=%{_bindir}/xpet %U
Icon=peticon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xvic.desktop << EOF
[Desktop Entry]
Name=VIC 20 Emulator
Comment=Commodore VIC 20 Emulator
Exec=%{_bindir}/xvic %U
Icon=vic20icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2.desktop << EOF
[Desktop Entry]
Name=CBM2 Emulator
Comment=Commodore BM 2 Emulator
Exec=%{_bindir}/xcbm2 %U
Icon=c610icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4.desktop << EOF
[Desktop Entry]
Name=CPLUS4 Emulator
Comment=Commodore PLUS4 Emulator
Exec=%{_bindir}/xplus4 %U
Icon=plus4icon
Terminal=false
Type=Application
MimeType=application/x-d64;application/x-t64;application/x-x64;
StartupNotify=true
Categories=GNOME;GTK;Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-c1541.desktop << EOF
[Desktop Entry]
Name=VICE disk image tool
Comment=C1541 stand alone disk image maintenance program
Exec=%{_bindir}/c1541 %U
Icon=commodore
Terminal=true
Type=Application
StartupNotify=true
Categories=Emulator;
EOF

%__cat > %{buildroot}%{_datadir}/applications/mandriva-vsid.desktop << EOF
[Desktop Entry]
Name=VSID music player
Comment=VICE SID music player for Commodore tunes
Exec=%{_bindir}/vsid %U
Icon=commodore
Terminal=false
Type=Application
StartupNotify=true
Categories=Audio;Player;
EOF

#install icons
%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
tar xjf %{SOURCE1} -C %{buildroot}%{_iconsdir}/hicolor/32x32/apps
tar xjf %{SOURCE2} -C %{buildroot}%{_iconsdir}/hicolor/48x48/apps
tar xjf %{SOURCE3} -C %{buildroot}%{_iconsdir}/hicolor/16x16/apps

%clean
%__rm -rf %{buildroot}

%if %{mdvver} < 201200
%post
%_install_info vice.info

%preun
%_remove_install_info vice.info
%endif

%files
%doc AUTHORS FEEDBACK INSTALL README ChangeLog doc/html/plain/*
%{_bindir}/*
%{_prefix}/lib/vice
%{_mandir}/man1/*
%{_infodir}/*info*
%{_datadir}/applications/mandriva-*
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/info/vice.*

