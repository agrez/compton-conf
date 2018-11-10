%global     commit 9a013cd28ae13c848ab0de267067aad526d2cc7d
%global     commit_short %(c=%{commit}; echo ${c:0:7})

Name:           compton-conf
Version:        0.4.0
Release:        1.%{commit_short}%{?dist}
Summary:        GUI configuration tool for compton
License:        LGPL-2.1+
Group:          User Interface/X
URL:            https://github.com/lxde/%{name}
Source0:        https://github.com/lxde/%{name}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit_short}.tar.gz
BuildRequires:  cmake
BuildRequires:  git
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  cmake(KF5WindowSystem)
BuildRequires:  cmake(Qt5LinguistTools)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libconfig)
BuildRequires:  pkgconfig(lxqt)

Requires:       compton
Requires(post): desktop-file-utils
Requires(pre):  desktop-file-utils


%description
%{name} is a configuration tool for X composite manager Compton.

%prep
%autosetup -n %{name}-%{commit}


%build
%cmake
make %{?_smp_mflags}


%install
%{makeinstall} DESTDIR=%{buildroot}

desktop-file-edit --remove-category=LXQt --add-category=X-LXQt \
%{buildroot}%{_datadir}/applications/%{name}.desktop

desktop-file-edit --remove-only-show-in=LXQt --add-only-show-in=X-LXQt \
%{buildroot}%{_sysconfdir}/xdg/autostart/lxqt-compton.desktop

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md compton.conf.example
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}
%{_sysconfdir}/xdg/autostart/*.desktop


%changelog
* Fri Aug 11 2017 Vaughan <devel at agrez dot net> - 0.2.1-3.786ad3f
- Fix autostart desktop file

* Tue Jul 25 2017 Vaughan <devel at agrez dot net> - 0.2.1-2.786ad3f
- Update to  git commit: 786ad3fae93a4ba1efb3c76e239fddd1f604a30d

* Tue Feb 14 2017 Vaughan <devel at agrez dot net> - 0.2.1-1.5603f30
- New release
- Update to  git commit: 5603f30b447357964be065eb05ae35e39745a302

* Sun Oct 16 2016 Vaughan <devel at agrez dot net> - 0.2.0-1.e71ee4c
- New release (git commit e71ee4c9a6e3a3b579543bb0e6d969b585ff3209)
- Add Buildrequires: git

* Wed Sep 14 2016 Vaughan <devel at agrez dot net> - 0.1.0-1.c6d6efb
- Initial package
- Git commit: c6d6efbe40995a7d8ef44a89e17a547836008757
