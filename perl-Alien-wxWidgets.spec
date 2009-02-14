%define module  Alien-wxWidgets
%define name    perl-%{module}
%define version 0.42
%define release %mkrel 2

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Building, finding and using wxWidgets binaries
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Alien/%{module}-%{version}.tar.gz
Buildrequires:  perl(Module::Build)
Buildrequires:  perl(Module::Pluggable)
Buildrequires:  lib64wxgtku2.8-devel
Buildrequires:  wxGTK-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
In short Alien::wxWidgets can be used to detect and get configuration settings
from an installed wxWidgets.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor < /dev/null
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README.txt
%{perl_vendorarch}/Alien
%{perl_vendorarch}/auto/Alien
%{_mandir}/*/*

