%define	name	freedroid
%define	version	1.0.2
%define release %mkrel 5
%define	Summary	Clone of the C64 Game Paradroid

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	http://freedroid.sourceforge.net/Freedroid_Manual.ps.bz2
Source11:	%{name}-16x16.png
Source12:	%{name}-32x32.png
Source13:	%{name}-48x48.png
Patch:		freedroid-1.0.2-vorbis.patch.bz2
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://freedroid.sourceforge.net/
BuildRequires:	SDL_mixer-devel SDL_image-devel jpeg-devel png-devel
BuildRequires:	libvorbis-devel

%description
This is a clone of the classic game "Paradroid" on Commodore 64
with some improvements and extensions to the classic version.

In this game, you control a robot, depicted by a small white ball with
a few numbers within an interstellar spaceship consisting of several
decks connected by elevators.

The aim of the game is to destroy all enemy robots, depicted by small
black balls with a few numbers, by either shooting them or seizing
control over them by creating connections in a short subgame of
electric circuits.

%prep
%setup -q
%patch -p1
%{__cp} %SOURCE1 .
autoconf

%build
%configure2_5x --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make CC="%{__cc} $RPM_OPT_FLAGS"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std transform=""
%{__install} -d %{buildroot}%{_menudir}
%{__cat} <<EOF > %{buildroot}%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
		  needs="x11" \
		  icon="%{name}.png" \
		  section="More Applications/Games/Arcade" \
		  title="Freedroid"\
		  longtitle="%{Summary}" xdg="true"
EOF
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Freedroid
Comment=%Summary
Exec=%_gamesbindir/%name
Icon=%name
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Games-Arcade;Game;ArcadeGame;
EOF

%{__install} -m644 %{SOURCE11} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} -m644 %{SOURCE12} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} -m644 %{SOURCE13} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%{__rm} -rf $RPM_BUILD_ROOT%{_gamesdatadir}/%{name}/mac-osx

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TODO Freedroid_Manual.ps.bz2
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/%{name}.6*
%_datadir/applications/mandriva*
%{_menudir}/%{name}
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png
