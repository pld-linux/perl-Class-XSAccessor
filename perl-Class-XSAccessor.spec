#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	XSAccessor
Summary:	Class::XSAccessor - Generate fast XS accessors without runtime compilation
Summary(pl.UTF-8):	Class::XSAccessor - Generuj szybkie funkcje dostępu XS bez kompilacji w czasie uruchomienia
Name:		perl-Class-XSAccessor
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/S/SM/SMUELLER/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	6f5b8af9f3647548e510eb8587708cbb
URL:		http://search.cpan.org/dist/Class-XSAccessor/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(AutoXS::Header) >= 1.00
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
Class::XSAccessor - Generuj szybkie funkcje dostępu XS bez kompilacji
w czasie uruchomienia.

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
%dir %{perl_vendorarch}/auto/Class/XSAccessor
%{perl_vendorarch}/auto/Class/XSAccessor/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Class/XSAccessor/*.so
%{_mandir}/man3/*
