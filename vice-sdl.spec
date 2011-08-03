%define Werror_cflags %nil
%define	name	vice-sdl
%define oname	vice
%define version 2.3
%define release %mkrel 1

Summary:	VICE, the Versatile Commodore Emulator
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2
Group:		Emulators
Source0:	http://www.zimmers.net/anonftp/pub/cbm/crossplatform/emulators/VICE/%{oname}-%{version}.tar.gz
Source1:	vice-normalicons.tar.bz2
Source2:	vice-largeicons.tar.bz2
Source3:	vice-miniicons.tar.bz2
Patch0:		vice-2.1-fix-str-fmt.patch
Patch1:		vice-2.1-fix-alsa-fragment.patch
Patch2:		vice-2.1-elif-without-condition.patch
URL:		http://www.viceteam.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	readline-devel
BuildRequires:	libncurses-devel
BuildRequires:	SDL-devel SDL_sound-devel
BuildRequires:	libungif-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  libalsa-devel
BuildRequires:  libopencbm-devel
BuildRequires:	gtkglext-devel
BuildRequires:	libxxf86vm-devel
BuildRequires:	flex
BuildRequires:	mkfontdir bdftopcf
BuildRequires:	libxt-devel
BuildRequires:	gettext-devel
BuildRequires:	SDL_sound-devel
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
Requires(post):	info-install
Requires(preun):	info-install
Conflicts:	vice

%description
VICE is a set of accurate emulators for the Commodore 64, 128, VIC20,
PET and CBM-II 8-bit computers, all of which run under the X Window
System.

%prep
%setup -q -n %{oname}-%{version}
# %patch0 -p0
# %patch1 -p2
# %patch2 -p1

%build
export CFLAGS="$RPM_OPT_FLAGS -DNO_REGPARM" 
%configure2_5x --enable-sdlui --enable-fullscreen \
%ifarch alpha
--disable-inline
%endif

%make

%install
rm -rf %{buildroot}
%makeinstall_std
#xdg menu
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-x64.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-x128.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-xpet.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-xvic.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-xcbm2.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-xplus4.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-c1541.desktop << EOF
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
cat > %{buildroot}%{_datadir}/applications/mandriva-vsid.desktop << EOF
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
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps
tar xjf %{SOURCE1} -C %{buildroot}%{_iconsdir}/hicolor/32x32/apps
tar xjf %{SOURCE2} -C %{buildroot}%{_iconsdir}/hicolor/48x48/apps
tar xjf %{SOURCE3} -C %{buildroot}%{_iconsdir}/hicolor/16x16/apps

%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%_install_info vice.info
%if %mdkversion < 200900
%update_desktop_database
%{update_menus}
%endif

%preun
%_remove_install_info vice.info

%if %mdkversion < 200900
%postun
%clean_desktop_database
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS FEEDBACK INSTALL README ChangeLog doc/html/plain/*
%{_bindir}/*
%{_prefix}/lib/vice
%{_mandir}/man1/*
%{_infodir}/*info*
%_datadir/applications/mandriva-*
%{_iconsdir}/hicolor/*/apps/*.png
# %{_datadir}/info/vice.txt 

