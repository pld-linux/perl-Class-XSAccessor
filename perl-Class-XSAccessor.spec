#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	XSAccessor
Summary:	Class::XSAccessor - Generate fast XS accessors without runtime compilation
Summary(pl.UTF-8):	Class::XSAccessor - generowanie szybkich funkcji dostępu XS bez kompilacji w czasie uruchomienia
Name:		perl-Class-XSAccessor
Version:	1.19
Release:	4
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Class/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5c5dea74f00ad37c5119dd22b28a5563
URL:		http://search.cpan.org/dist/Class-XSAccessor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-AutoXS-Header >= 1.00
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Class::XSAccessor implements fast read, write and read/write accessors
in XS. Additionally, it can provide predicates such as has_foo() for
testing whether the attribute foo is defined in the object. It only
works with objects that are implemented as ordinary hashes.
Class::XSAccessor::Array implements the same interface for objects
that use arrays for their internal representation.

%description -l pl.UTF-8
Class::XSAccessor implementuje szybkie funkcje dostępu do odczytu,
zapisu lub odczytu/zapisu w XS. Dodatkowo potrafi zapewnić predykaty
takie jak has_foo() do sprawdzania, czy atrybut foo jest zdefiniowany
w obiekcie. Działa tylko z obiektami zaimplentowanymi jako zwykłe
hasze. Class::XSAccessor::Array implementuje ten sam interfejs dla
obiektów wykorzystujących tablice jako wewnętrzną reprezentację.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Class/*.pm
%dir %{perl_vendorarch}/Class/XSAccessor
%{perl_vendorarch}/Class/XSAccessor/*.pm
%dir %{perl_vendorarch}/auto/Class/XSAccessor
%attr(755,root,root) %{perl_vendorarch}/auto/Class/XSAccessor/XSAccessor.so
%{_mandir}/man3/Class::XSAccessor.3pm*
%{_mandir}/man3/Class::XSAccessor::*.3pm*
