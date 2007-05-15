%define real_name CGI-GuruMeditation

Summary:	Guru Meditation for CGIs
Name:		perl-%{real_name}
Version:	1.10
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RS/RSE/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}

%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/CGI/*
%{_mandir}/*/*
