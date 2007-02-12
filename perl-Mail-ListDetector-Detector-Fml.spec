#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Mail
%define	pnam	ListDetector-Detector-Fml
Summary:	Mail::ListDetector::Detector::Fml - FML message detector
Summary(pl.UTF-8):   Mail::ListDetector::Detector::Fml - wykrywanie wiadomości FML
Name:		perl-Mail-ListDetector-Detector-Fml
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	483f4459e6a4837907b68a3815733764
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Mail-ListDetector >= 0.18
BuildRequires:	perl-Test-Simple >= 0.32
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail::ListDetector::Detector::Fml is an implementation of a mailing
list detector, for FML. See http://www.fml.org/ for details about FML.

When used, this module installs itself to Mail::ListDetector. FML
maling list message is RFC2369 compliant, so can be matched with
RFC2369 detector, but this module allows you to parse more FML
specific information about the mailing list.

%description -l pl.UTF-8
Mail::ListDetector::Detector::Fml to implementacja wykrywania list
dyskusyjnych dla FML. Szczegóły na temat FML można znaleźć pod adresem
<http://www.fml.org/>.

W przypadku użycia moduł ten instaluje się wewnątrz klasy
Mail::ListDetector. Wiadomości list dyskusyjnych FML są zgodne z
RFC2369, więc mogą być dopasowywane wykrywaczem RFC2369, ale ten moduł
umożliwia analizowanie większej liczby informacji o liście
specyficznych dla FML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Mail/ListDetector/Detector/*.pm
%{_mandir}/man3/*
