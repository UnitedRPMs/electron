%global debug_package %{nil}
%global _hardened_build 1
%global __provides_exclude (libnode)
%global __requires_exclude (libnode|ffmpeg)
%global project electron
%global repo %{project}
%global electrondir %{_libdir}/%{name}/%{version}

#defining architectures
%ifarch x86_64
%global platform linux64
%global archele linux-x64
%else
%global platform linux32
%global archele linux-x86
%endif

Name:    electron
Version: 2.0.2
Release: 1%{?dist}
Summary: Framework for build cross-platform desktop applications
Group:   Applications/Editors
License: MIT
URL:     https://github.com/electron/electron
Source:  https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-%{archele}.zip
Source1: https://atom.io/download/atom-shell/v%{version}/node-v%{version}.tar.gz

Requires(post): chkconfig
Requires(postun): chkconfig
Obsoletes: %{name} < %{version}-%{release}

%description
The Electron framework lets you write cross-platform desktop applications
using JavaScript, HTML and CSS. It is based on Node.js and Chromium.

Visit http://electron.atom.io/ to learn more.

%prep
%setup -c -a 1

%build

%install

# Install electron
Files="content_shell.pak electron icudtl.dat libffmpeg.so libnode.so locales \
       natives_blob.bin resources snapshot_blob.bin version"
install -d %{buildroot}%{electrondir}
cp -a $Files %{buildroot}%{electrondir}

install -d %{buildroot}%{_bindir}
ln -sfv %{electrondir}/%{name} %{buildroot}%{_bindir}/%{name}-%{version}

# Install node headers
install -d %{buildroot}%{electrondir}/node
cp -r node-v%{version}/* %{buildroot}%{electrondir}/node

%post
if [ $1 -ge 1 ]; then
PRIORITY=90
/sbin/alternatives --install %{_bindir}/%{name} %{name} %{electrondir}/%{name} $PRIORITY
fi

%postun
if [ $1 -eq 0 ]; then
/sbin/alternatives --remove %{name} %{electrondir}/%{name}
fi

%files
%defattr(-,root,root,-)
%{_bindir}/%{name}-%{version}
%{_libdir}/%{name}/%{version}/

%changelog

* Tue May 22 2018 David Vásquez <davidva AT tutanota DOT com> 2.0.2-1
- Updated to 2.0.2

* Sun Mar 18 2018 David Vásquez <davidva AT tutanota DOT com> 1.8.4-1
- Updated to 1.8.4

* Mon Feb 26 2018 David Vásquez <davidva AT tutanota DOT com> 1.8.2-1
- Updated to 1.8.2

* Fri Dec 15 2017 David Vásquez <davidva AT tutanota DOT com> 1.8.1-1
- Updated to 1.8.1

* Sun Oct 22 2017 David Vásquez <davidva AT tutanota DOT com> 1.7.5-1
- Updated to 1.7.5

* Mon Oct 02 2017 David Vásquez <davidva AT tutanota DOT com> 1.6.14-1
- Updated to 1.6.14

* Sun Aug 13 2017 David Vásquez <davidva AT tutanota DOT com> 1.3.15-1
- Updated, added sources and new changes in the structure

* Tue Jan  3 2017 mosquito <sensor.wen@gmail.com> - 1.3.13-1.git93c4f90
- Release 1.3.13
* Thu Dec  1 2016 mosquito <sensor.wen@gmail.com> - 1.3.9-1.gitcb9fdc4
- Release 1.3.9
* Sat Oct 15 2016 mosquito <sensor.wen@gmail.com> - 1.3.7-1.gite3688a8
- Release 1.3.7
* Wed Jul 13 2016 mosquito <sensor.wen@gmail.com> - 1.2.7-1.git13e1818
- Release 1.2.7
* Wed Jun 29 2016 mosquito <sensor.wen@gmail.com> - 1.2.3-3.git553341d
- Dont edit the global config file in postscript
* Sun Jun 19 2016 mosquito <sensor.wen@gmail.com> - 1.2.3-2.git553341d
- Rewrite post script for rhel7
* Fri Jun 17 2016 mosquito <sensor.wen@gmail.com> - 1.2.3-1.git553341d
- Release 1.2.3
- Set priority 90
* Fri Jun 17 2016 mosquito <sensor.wen@gmail.com> - 0.37.8-1.gitedb73fb
- Revert to 0.37.8
- Use multiversion config
* Fri Jun 10 2016 mosquito <sensor.wen@gmail.com> - 1.2.2-1.gitb2bea57
- Release 1.2.2
* Fri Jun  3 2016 mosquito <sensor.wen@gmail.com> - 1.2.1-1.git97dd71d
- Release 1.2.1
* Thu May 26 2016 mosquito <sensor.wen@gmail.com> - 1.2.0-1.gitc127274
- Release 1.2.0
* Mon Apr 25 2016 mosquito <sensor.wen@gmail.com> - 0.37.7-1.gitc04d43c
- Release 0.37.7
- Add node headers
* Wed Apr 13 2016 mosquito <sensor.wen@gmail.com> - 0.37.5-1.git55b8e9a
- Release 0.37.5
* Sat Mar 12 2016 mosquito <sensor.wen@gmail.com> - 0.36.11-1.gitead94b7
- Release 0.36.11
* Sat Mar  5 2016 mosquito <sensor.wen@gmail.com> - 0.36.10-1.git3397845
- Release 0.36.10
* Sat Feb 20 2016 mosquito <sensor.wen@gmail.com> - 0.36.8-1.git4b18317
- Release 0.36.8
* Sun Feb 14 2016 mosquito <sensor.wen@gmail.com> - 0.36.7-1.git9d8e23c
- Initial package
