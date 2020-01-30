%define staticdevelname %mklibname bison -d -s

%define bootstrap 0
%{?_without_bootstrap: %global bootstrap 0}
%{?_with_bootstrap: %global bootstrap 1}

Summary:	A GNU general-purpose parser generator
Name:		bison
Version:	3.5.1
Release:	1
License:	GPLv3+
Group:		Development/Tools
URL:		http://www.gnu.org/software/bison/bison.html
Source0:	ftp://ftp.gnu.org/pub/gnu/bison/bison-%{version}.tar.xz
Patch0:		bison-1.32-extfix.patch
Requires:	m4 >= 1.4
BuildRequires:	gettext-devel
BuildRequires:	help2man
%if !%{bootstrap}
%ifnarch %mips %arm
BuildRequires:	java-devel-openjdk
%endif
%endif
BuildRequires:	m4 >= 1.4
#for tests
BuildRequires:	flex

%description
Bison is a general purpose parser generator which converts a grammar
description for an LALR context-free grammar into a C program to parse
that grammar.  Bison can be used to develop a wide range of language
parsers, from ones used in simple desk calculators to complex programming
languages.  Bison is upwardly compatible with Yacc, so any correctly
written Yacc grammar should work with Bison without any changes.  If
you know Yacc, you shouldn't have any trouble using Bison (but you do need
to be very proficient in C programming to be able to use Bison).  Many
programs use Bison as part of their build process. Bison is only needed
on systems that are used for development.

If your system will be used for C development, you should install Bison
since it is used to build many C programs.

%package -n	%{staticdevelname}
Summary:	Static development library for using Bison-generated parsers
Group:		Development/C
Requires:	bison = %{version}
Provides:	bison-devel-static = %{version}

%description -n	%{staticdevelname}
This package contains the static -ly library sometimes used by programs using
Bison-generated parsers. If you are developing programs using Bison, you might
want to link with this library. This library is not required by all
Bison-generated parsers, but may be employed by simple programs to supply
minimal support for the generated parsers.

%prep
%autosetup -p1

#fix build with autoreconf
sed -i -e 's,AM_GNU_GETTEXT_VERSION,AM_GNU_GETTEXT_REQUIRE_VERSION,' configure.ac

%build
autoreconf -fi
%configure
%make_build

%check
%__make check

%install
%make_install

mv %{buildroot}%{_bindir}/yacc %{buildroot}%{_bindir}/yacc.bison

%find_lang %{name} --all-name

%post
%{_sbindir}/update-alternatives --install %{_bindir}/yacc yacc %{_bindir}/yacc.bison 10

%preun
if [ $1 -eq 0 ]; then
  %{_sbindir}/update-alternatives --remove yacc %{_bindir}/yacc.bison
fi

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_bindir}/*
%dir %{_datadir}/bison
%{_datadir}/bison/*
%{_datadir}/aclocal/*
%{_infodir}/bison.info*
%{_mandir}/man1/*
%{_docdir}/bison/examples

%files -n %{staticdevelname}
%{_libdir}/liby.a


%changelog
* Mon Jan 20 2020 kekepower <kekepower> 3.5.1-1.mga8
+ Revision: 1481743
- Update to version 3.5.1
+ wally <wally>
- replace deprecated %%configure2_5x

* Fri Dec 13 2019 kekepower <kekepower> 3.5-1.mga8
+ Revision: 1466152
- Update to version 3.5

* Fri Sep 13 2019 daviddavid <daviddavid> 3.4.2-1.mga8
+ Revision: 1440139
- new version: 3.4.2

* Sun Jun 30 2019 daviddavid <daviddavid> 3.4.1-1.mga8
+ Revision: 1416499
- new version: 3.4.1

* Sun Feb 03 2019 luigiwalser <luigiwalser> 3.3.2-1.mga7
+ Revision: 1362929
- 3.3.2

* Sat Feb 02 2019 tmb <tmb> 3.3.1-1.mga7
+ Revision: 1362332
- update to 3.3.1

* Sat Jan 26 2019 kekepower <kekepower> 3.3-1.mga7
+ Revision: 1361167
- Update to version 3.3

* Mon Dec 24 2018 kekepower <kekepower> 3.2.4-1.mga7
+ Revision: 1344858
- Update to version 3.2.4

* Wed Dec 19 2018 kekepower <kekepower> 3.2.3-1.mga7
+ Revision: 1342826
- Update to version 3.2.3

* Thu Nov 22 2018 kekepower <kekepower> 3.2.2-1.mga7
+ Revision: 1333402
- Try again without disabling tests
- Disable tests number 331, 341 and 460 for now
- Update to version 3.2.2

* Fri Nov 09 2018 daviddavid <daviddavid> 3.2.1-1.mga7
+ Revision: 1329124
- new version: 3.2.1

* Wed Oct 31 2018 daviddavid <daviddavid> 3.2-1.mga7
+ Revision: 1326860
- new version: 3.2

* Fri Sep 21 2018 umeabot <umeabot> 3.1-3.mga7
+ Revision: 1295447
- Mageia 7 Mass Rebuild

* Mon Sep 03 2018 tv <tv> 3.1-2.mga7
+ Revision: 1256425
- rely on filetriggers for info system (mga#23482)
- rely on filetriggers for info system (mga#23482)

* Tue Aug 28 2018 daviddavid <daviddavid> 3.1-1.mga7
+ Revision: 1255357
- new version: 3.1

* Thu May 31 2018 kekepower <kekepower> 3.0.5-1.mga7
+ Revision: 1233199
- Update to version 3.0.5

* Sun Sep 24 2017 cjw <cjw> 3.0.4-4.mga7
+ Revision: 1158687
- add buildrequires: gettext-devel
- add upstream fix for test failures with gcc 7

* Sat Feb 13 2016 umeabot <umeabot> 3.0.4-3.mga6
+ Revision: 959591
- Mageia 6 Mass Rebuild

* Thu Oct 15 2015 shlomif <shlomif> 3.0.4-2.mga6
+ Revision: 891768
- Include missing files under docdir.

* Tue Jan 27 2015 luigiwalser <luigiwalser> 3.0.4-1.mga5
+ Revision: 812468
- 3.0.4

* Thu Jan 15 2015 luigiwalser <luigiwalser> 3.0.3-1.mga5
+ Revision: 810774
- 3.0.3

* Wed Oct 15 2014 umeabot <umeabot> 3.0.2-3.mga5
+ Revision: 739035
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 3.0.2-2.mga5
+ Revision: 678160
- Mageia 5 Mass Rebuild

* Thu Dec 05 2013 luigiwalser <luigiwalser> 3.0.2-1.mga4
+ Revision: 555410
- 3.0.2

* Sat Oct 19 2013 umeabot <umeabot> 3.0-2.mga4
+ Revision: 533508
- Mageia 4 Mass Rebuild

* Sat Aug 31 2013 wally <wally> 3.0-1.mga4
+ Revision: 473700
- BR flex for tests
+ fwang <fwang>
- new version 3.0

* Fri May 24 2013 luigiwalser <luigiwalser> 2.7.1-1.mga4
+ Revision: 426594
- 2.7.1

* Fri Jan 11 2013 umeabot <umeabot> 2.7-2.mga3
+ Revision: 346908
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sat Dec 15 2012 luigiwalser <luigiwalser> 2.7-1.mga3
+ Revision: 331235
- 2.7

* Thu Nov 08 2012 fwang <fwang> 2.6.5-1.mga3
+ Revision: 316291
- new version 2.6.5
- cleanup spec and rpm group

* Wed Oct 24 2012 fwang <fwang> 2.6.4-1.mga3
+ Revision: 309592
- new version 2.6.4

* Tue Oct 23 2012 fwang <fwang> 2.6.3-1.mga3
+ Revision: 309399
- new version 2.6.3

* Fri Aug 03 2012 fwang <fwang> 2.6.2-1.mga3
+ Revision: 278293
- new version 2.6.2

* Wed Aug 01 2012 fwang <fwang> 2.6.1-1.mga3
+ Revision: 277151
- new version 2.6.1

* Fri Jul 20 2012 fwang <fwang> 2.6-1.mga3
+ Revision: 272741
- new version 2.6

* Wed Jun 06 2012 fwang <fwang> 2.5.1-1.mga3
+ Revision: 256088
- new version 2.5.1

* Fri Jun 17 2011 tv <tv> 2.5-1.mga2
+ Revision: 109238
- new release

* Sun Jan 09 2011 blino <blino> 2.4.3-2.mga1
+ Revision: 2170
- rebuild  with java

* Sat Jan 08 2011 blino <blino> 2.4.3-1.mga1
+ Revision: 404
- bootstrap bison
- add bootstrap flag
- remove obsolete stuff
- imported package bison

