%define upstream_name    Alien-wxWidgets
%define upstream_version 0.65

%define debug_package %{nil}

Name:           perl-%{upstream_name}
Version:        %perl_convert_version %{upstream_version}
Release:	1

Summary:        Building, finding and using wxWidgets binaries

License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{upstream_name}
Source0:        http://www.cpan.org/modules/by-module/Alien/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:         Alien-wxWidgets-0.43-fix-wrong-libname.patch

Buildrequires:  perl(Module::Build)
Buildrequires:  perl(Module::Pluggable)
Buildrequires:  wxgtku2.8-devel
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



