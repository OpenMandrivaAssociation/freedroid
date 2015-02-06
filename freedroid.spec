%define	name	freedroid
%define	version	1.0.2
%define release 12
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
Patch1:		freedroid-1.0.2-format-strings.patch
License:	GPLv2+
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
%patch1 -p1
%{__cp} %SOURCE1 .
autoconf

%build
%configure2_5x --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make CC="%{__cc} $RPM_OPT_FLAGS"

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std transform=""
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
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

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README AUTHORS ChangeLog NEWS TODO Freedroid_Manual.ps.bz2
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_mandir}/man6/%{name}.6*
%_datadir/applications/mandriva*
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png


%changelog
* Mon Jul 25 2011 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-11mdv2012.0
+ Revision: 691505
- rebuild

* Sat Jul 24 2010 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-10mdv2011.0
+ Revision: 558094
- rebuild

* Thu Jul 23 2009 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-8mdv2010.0
+ Revision: 398785
- fix format strings
- update license

* Tue Jul 22 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-7mdv2009.0
+ Revision: 240721
- rebuild
- drop old menu
- kill re-definition of %%buildroot on Pixel's request
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sun Aug 26 2007 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-5mdv2008.0
+ Revision: 71620
- Import freedroid



* Thu Aug 24 2006 Götz Waschk <waschk@mandriva.org> 1.0.2-5mdv2007.0
- fix vorbis detection
- fix buildrequires
- xdg menu

* Mon Dec 05 2005 GÃ¶tz Waschk <waschk@mandriva.org> 1.0.2-4mdk
- Rebuild

* Fri Dec  3 2004 Götz Waschk <waschk@linux-mandrake.com> 1.0.2-3mdk
- rebuild

* Thu Nov 27 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-2mdk
- remove macosx devel files
- macroized

* Thu Nov 27 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.0.2-1mdk
- 1.0.2
- cosmetics

* Tue May  6 2003 Götz Waschk <waschk@linux-mandrake.com> 1.0.1-1mdk
- add the man page
- new version

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-5mdk
- fix buildrequires

* Mon Apr 28 2003 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-4mdk
- fix distriblint warning

* Sat Apr 26 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 0.8.4-3mdk
- dropped Prefix tag
- compile with $RPM_OPT_FLAGS
- added icons

* Fri Dec 20 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-2mdk
- add the manual to the docs

* Fri Dec 20 2002 Götz Waschk <waschk@linux-mandrake.com> 0.8.4-1mdk
- initial package
