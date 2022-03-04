#
# spec file for package electron
#
# Copyright (c) 2022 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://goo.gl/zqFJft
#

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
Version: 17.1.0
Release: 1%{?dist}
Summary: Framework for build cross-platform desktop applications
Group:   Applications/Editors
License: MIT
URL:     https://github.com/electron/electron
Source:  https://github.com/electron/electron/releases/download/v%{version}/electron-v%{version}-%{archele}.zip
Source1: https://atom.io/download/atom-shell/v%{version}/node-v%{version}.tar.gz

Requires(post): chkconfig
Requires(postun): chkconfig

%description
The Electron framework lets you write cross-platform desktop applications
using JavaScript, HTML and CSS. It is based on Node.js and Chromium.

Visit http://electron.atom.io/ to learn more.

%prep
%setup -c -a 1

%build

%install

install -d %{buildroot}%{electrondir}
cp -rf * %{buildroot}%{electrondir}

install -d %{buildroot}%{_bindir}
ln -sfv %{electrondir}/%{name} %{buildroot}%{_bindir}/%{name}-%{version}

# Install node headers
install -d %{buildroot}%{electrondir}/node
cp -r node_headers/include/node/* %{buildroot}%{electrondir}/node

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

* Thu Mar 03 2022 - David Va <davidva AT tuta DOT io> 17.1.0-1
- Updated to 17.1.0

* Sun Oct 24 2021 - David Va <davidva AT tuta DOT io> 15.2.0-1
- Updated to 15.2.0

* Thu Sep 16 2021 - David Va <davidva AT tuta DOT io> 14.0.1-1
- Updated to 14.0.1

* Fri Sep 03 2021 - David Va <davidva AT tuta DOT io> 14.0.0-1
- Updated to 14.0.0

* Mon Aug 23 2021 - David Va <davidva AT tuta DOT io> 13.2.2-1
- Updated to 13.2.2

* Mon Aug 02 2021 - David Va <davidva AT tuta DOT io> 13.1.7-1
- Updated to 13.1.7

* Thu Jul 08 2021 - David Va <davidva AT tuta DOT io> 13.1.6-1
- Updated to 13.1.6

* Mon Jun 28 2021 - David Va <davidva AT tuta DOT io> 13.1.4-1
- Updated to 13.1.4

* Thu Jun 03 2021 - David Va <davidva AT tuta DOT io> 13.1.0-1
- Updated to 13.1.0

* Sat Apr 17 2021 - David Va <davidva AT tuta DOT io> 12.0.2-1
- Updated to 12.0.2

* Sat Mar 20 2021 - David Va <davidva AT tuta DOT io> 12.0.1-1
- Updated to 12.0.1

* Mon Feb 15 2021 - David Va <davidva AT tuta DOT io> 11.2.3-1
- Updated to 11.2.3

* Sat Oct 24 2020 - David Va <davidva AT tuta DOT io> 10.1.5-1
- Updated to 10.1.5

* Mon Oct 12 2020 - David Va <davidva AT tuta DOT io> 10.1.3-1
- Updated to 10.1.3

* Fri Jul 03 2020 - David Va <davidva AT tuta DOT io> 9.0.5-1
- Updated to 9.0.5

* Mon Jun 08 2020 - David Va <davidva AT tuta DOT io> 9.0.3-1
- Updated to 9.0.3

* Tue Jun 02 2020 - David Va <davidva AT tuta DOT io> 9.0.1-1
- Updated to 9.0.1

* Mon May 18 2020 - David Va <davidva AT tuta DOT io> 9.0.0-1
- Updated to 9.0.0

* Sat May 02 2020 - David Va <davidva AT tuta DOT io> 8.2.5-1
- Updated to 8.2.5

* Mon Apr 20 2020 - David Va <davidva AT tuta DOT io> 8.2.3-1
- Updated to 8.2.3

* Wed Apr 15 2020 - David Va <davidva AT tuta DOT io> 8.2.2-1
- Updated to 8.2.2

* Tue Apr 07 2020 - David Va <davidva AT tuta DOT io> 8.2.1-1
- Updated to 8.2.1

* Wed Mar 11 2020 - David Va <davidva AT tuta DOT io> 8.1.1-1
- Updated to 8.1.1

* Mon Feb 03 2020 - David Va <davidva AT tuta DOT io> 8.0.0-1
- Updated to 8.0.0

* Sun Jan 19 2020 - David Va <davidva AT tuta DOT io> 7.1.9-1
- Updated to 7.1.9

* Fri Dec 13 2019 - David Va <davidva AT tuta DOT io> 7.1.4-1
- Updated to 7.1.4

* Fri Dec 06 2019 - David Va <davidva AT tuta DOT io> 7.1.3-1
- Updated to 7.1.3

* Mon Nov 25 2019 - David Va <davidva AT tuta DOT io> 7.1.2-1
- Updated to 7.1.2

* Mon Oct 14 2019 - David Va <davidva AT tuta DOT io> 6.0.12-1
- Updated to 6.0.12

* Fri Oct 04 2019 - David Va <davidva AT tuta DOT io> 6.0.11-1
- Updated to 6.0.11

* Fri Sep 13 2019 - David Va <davidva AT tuta DOT io> 6.0.9-1
- Updated to 6.0.9

* Tue Sep 03 2019 - David Va <davidva AT tuta DOT io> 6.0.7-1
- Updated to 6.0.7

* Thu Aug 29 2019 - David Va <davidva AT tuta DOT io> 6.0.5-1
- Updated to 6.0.5

* Thu Aug 22 2019 - David Va <davidva AT tuta DOT io> 6.0.3-1
- Updated to 6.0.3

* Tue Aug 13 2019 - David Va <davidva AT tuta DOT io> 6.0.2-1
- Updated to 6.0.2

* Thu Aug 08 2019 - David Va <davidva AT tuta DOT io> 6.0.1-1
- Updated to 6.0.1

* Thu Jul 18 2019 - David Va <davidva AT tuta DOT io> 5.0.7-1
- Updated to 5.0.7

* Sun Jun 30 2019 - David Va <davidva AT tuta DOT io> 5.0.6-1
- Updated to 5.0.6

* Tue Jun 25 2019 - David Va <davidva AT tuta DOT io> 5.0.5-1
- Updated to 5.0.5

* Tue Jun 18 2019 - David Va <davidva AT tuta DOT io> 5.0.4-1
- Updated to 5.0.4

* Tue Jun 11 2019 - David Va <davidva AT tuta DOT io> 5.0.3-1
- Updated to 5.0.3

* Sat May 25 2019 - David Va <davidva AT tuta DOT io> 5.0.2-1
- Updated to 5.0.2

* Fri May 17 2019 - David Va <davidva AT tuta DOT io> 5.0.1-1
- Updated to 5.0.1

* Thu Apr 25 2019 - David Va <davidva AT tuta DOT io> 5.0.0-1
- Updated to 5.0.0

* Sat Apr 06 2019 - David Va <davidva AT tuta DOT io> 4.1.4-1
- Updated to 4.1.4

* Fri Mar 01 2019 - David Va <davidva AT tuta DOT io> 4.0.6-1
- Updated to 4.0.6

* Tue Feb 19 2019 - David Va <davidva AT tuta DOT io> 4.0.5-1
- Updated to 4.0.5

* Wed Feb 06 2019 - David Va <davidva AT tuta DOT io> 4.0.4-1
- Updated to 4.0.4

* Tue Jan 29 2019 - David Va <davidva AT tuta DOT io> 4.0.3-1
- Updated to 4.0.3

* Thu Jan 24 2019 - David Va <davidva AT tuta DOT io> 4.0.2-1
- Updated to 4.0.2

* Fri Jan 04 2019 - David Va <davidva AT tuta DOT io> 4.0.1-1
- Updated to 4.0.1

* Sat Dec 22 2018 - David Va <davidva AT tuta DOT io> 4.0.0-1
- Updated to 4.0.0

* Sat Dec 15 2018 - David Va <davidva AT tuta DOT io> 3.0.12-1
- Updated to 3.0.12

* Tue Dec 11 2018 - David Va <davidva AT tuta DOT io> 3.0.11-1
- Updated to 3.0.11

* Mon Nov 19 2018 - David Va <davidva AT tuta DOT io> 3.0.10-1
- Updated to 3.0.10

* Wed Nov 14 2018 - David Va <davidva AT tuta DOT io> 3.0.9-1
- Updated to 3.0.9

* Thu Nov 08 2018 - David Va <davidva AT tuta DOT io> 3.0.8-1
- Updated to 3.0.8

* Sun Nov 04 2018 - David Va <davidva AT tuta DOT io> 3.0.7-1
- Updated to 3.0.7

* Mon Oct 29 2018 - David Va <davidva AT tuta DOT io> 3.0.6-1
- Updated to 3.0.6

* Mon Oct 22 2018 - David Va <davidva AT tuta DOT io> 3.0.5-1
- Updated to 3.0.5

* Sun Oct 14 2018 - David Va <davidva AT tuta DOT io> 3.0.4-1
- Updated to 3.0.4

* Wed Oct 10 2018 - David Va <davidva AT tuta DOT io> 3.0.3-1
- Updated to 3.0.3

* Mon Oct 01 2018 - David Va <davidva AT tuta DOT io> 3.0.2-1
- Updated to 3.0.2

* Thu Sep 20 2018 - David Va <davidva AT tuta DOT io> 3.0.0-1
- Updated to 3.0.0

* Wed Sep 12 2018 - David Va <davidva AT tuta DOT io> 2.0.9-1
- Updated to 2.0.9

* Thu Sep 06 2018 - David Va <davidva AT tuta DOT io> 2.0.8-1
- Updated to 2.0.8

* Thu Aug 09 2018 - David Va <davidva AT tuta DOT io> 2.0.7-1
- Updated to 2.0.7

* Thu Aug 02 2018 - David Va <davidva AT tuta DOT io> 2.0.6-1
- Updated to 2.0.6

* Wed Jul 25 2018 David Vásquez <davidva AT tutanota DOT com> 2.0.5-1
- Updated to 2.0.5

* Sun Jul 08 2018 David Vásquez <davidva AT tutanota DOT com> 2.0.4-1
- Updated to 2.0.4

* Tue Jun 26 2018 David Vásquez <davidva AT tutanota DOT com> 2.0.3-1
- Updated to 2.0.3

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
