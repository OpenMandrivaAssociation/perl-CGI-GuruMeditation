%define upstream_name    CGI-GuruMeditation
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Guru Meditation for CGIs
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is a small module accompanying the CGI module, providing the display of an
error screen (somewhat resembling the classical red-on-black blinking Guru
Meditation from the good-old AmigaOS before version 2.04) in case of abnormal
termination of a CGI.

The module simply installs a $SIG{__DIE__} handler which sends a HTTP response
showing a HTML/CSS based screen which optionally includes the Perl run-time
error message, an excerpt from the CGI source code and the Perl run-time
environment variables. This provides both optically more pleasant and
functionally more elaborate error messages for CGIs.

This module supports both the regular CGI and the Apache/mod_perl CGI
environment.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/CGI/*
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 680689
- mass rebuild

* Tue Jul 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 402132
- rebuild using %%perl_convert_version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.10-3mdv2009.0
+ Revision: 241167
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue May 15 2007 Oden Eriksson <oeriksson@mandriva.com> 1.10-1mdv2008.0
+ Revision: 26912
- Import perl-CGI-GuruMeditation



* Tue May 15 2007 Oden Eriksson <oeriksson@mandriva.com> 1.10-1mdv2007.1
- initial Mandriva package
