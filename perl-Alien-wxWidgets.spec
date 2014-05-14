%define upstream_name    Alien-wxWidgets
%define upstream_version 0.64

%define debug_package %{nil}

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:	1

Summary:        Building, finding and using wxWidgets binaries
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Alien/Alien-wxWidgets-0.64.tar.gz
Patch0:         Alien-wxWidgets-0.43-fix-wrong-libname.patch

BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Module::Pluggable)
BuildRequires:  wxgtku2.8-devel
BuildRequires:  perl(JSON::PP)

%description
In short Alien::wxWidgets can be used to detect and get configuration settings
from an installed wxWidgets.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
# fix bug 45256
%patch0 -p0 -b .libname

%build
%{__perl} Build.PL installdirs=vendor < /dev/null
./Build

%install
./Build install destdir=%{buildroot}

%check
./Build test

%files 
%doc Changes README.txt
%{perl_vendorarch}/Alien
%{_mandir}/*/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.520.0-2
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.520.0-1
+ Revision: 674706
- new version

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 0.510.0-2mdv2011.0
+ Revision: 555419
- rebuild

* Wed Mar 31 2010 Jérôme Quelin <jquelin@mandriva.org> 0.510.0-1mdv2010.1
+ Revision: 530257
- update to 0.51

* Mon Jan 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.1
+ Revision: 489512
- update to 0.50

* Sun Jan 10 2010 Jérôme Quelin <jquelin@mandriva.org> 0.490.0-1mdv2010.1
+ Revision: 488600
- update to 0.49

* Mon Dec 28 2009 Jérôme Quelin <jquelin@mandriva.org> 0.480.0-1mdv2010.1
+ Revision: 483033
- update to 0.48

* Sun Dec 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.470.0-1mdv2010.1
+ Revision: 474072
- update to 0.47

* Mon Nov 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.460.0-1mdv2010.1
+ Revision: 463365
- update to 0.46

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.450.0-1mdv2010.1
+ Revision: 461256
- update to 0.45

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.440.0-1mdv2010.0
+ Revision: 414986
- update to 0.44

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.430.0-1mdv2010.0
+ Revision: 399436
- using %%perl_convert_version
- fixed license field
- fix bug 45256

* Mon May 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.43-1mdv2010.0
+ Revision: 374412
- update to new version 0.43

* Sat May 09 2009 Jérôme Quelin <jquelin@mandriva.org> 0.42-4mdv2010.0
+ Revision: 373697
- forcing rebuild

* Sun Feb 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.42-3mdv2009.1
+ Revision: 340467
- removing non-unicode requirement

* Sat Feb 14 2009 Olivier Thauvin <nanardon@mandriva.org> 0.42-2mdv2009.1
+ Revision: 340293
- fix buildrequires

  + Jérôme Quelin <jquelin@mandriva.org>
    - fix bug #47728: part one

* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.42-1mdv2009.1
+ Revision: 301424
- update to new version 0.42

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.41-1mdv2009.1
+ Revision: 297810
- update to new version 0.41

* Fri Oct 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.40-1mdv2009.1
+ Revision: 294619
- update to new version 0.40

* Tue Sep 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.39-1mdv2009.0
+ Revision: 283022
- update to new version 0.39

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.38-1mdv2009.0
+ Revision: 277940
- update to new version 0.38

* Mon Jun 30 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.37-1mdv2009.0
+ Revision: 230266
- update to new version 0.37

* Tue May 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.36-1mdv2009.0
+ Revision: 209315
- update to new version 0.36

* Tue May 06 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.35-1mdv2009.0
+ Revision: 201835
- update to new version 0.35

* Tue Apr 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.34-1mdv2009.0
+ Revision: 193735
- update to new version 0.34

* Sun Feb 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-2mdv2008.1
+ Revision: 164818
- despite containing only .pm files, this is not a noarch package
- rebuild

* Mon Jan 21 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.33-1mdv2008.1
+ Revision: 155666
- update to new version 0.33

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2008.1
+ Revision: 105466
- import perl-Alien-wxWidgets


* Fri Nov 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.32-1mdv2008.1
- first mdv release 

