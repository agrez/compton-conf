%global     commit c6d6efbe40995a7d8ef44a89e17a547836008757
%global     commit_short %(c=%{commit}; echo ${c:0:7})

Name:           compton-conf
Version:        0.1.0
Release:        1.%{commit_short}%{?dist}
Summary:        GUI configuration tool for compton
License:        LGPL-2.1+
Group:          User Interface/X
URL:            https://github.com/lxde/%{name}
Source0:        https://github.com/lxde/%{name}/archive/%{commit}.tar.gz#/%{name}-%{version}-%{commit_short}.tar.gz
BuildRequires:  cmake
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


%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.md compton.conf.example
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/%{name}


%changelog
* Wed Sep 14 2016 Vaughan <devel at agrez dot net> - 0.1.0-1.c6d6efb
- Initial package
- Git commit: c6d6efbe40995a7d8ef44a89e17a547836008757
