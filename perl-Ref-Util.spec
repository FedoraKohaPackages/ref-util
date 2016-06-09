Name:           perl-Ref-Util
Version:        0.020
Release:        2%{?dist}
Summary:        Utility functions for checking references
License:        MIT
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/Ref-Util/
Source0:        http://www.cpan.org/authors/id/X/XS/XSAWYERX/Ref-Util-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  perl(Exporter) >= 5.57
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::More)
Requires:       perl(Exporter) >= 5.57
Requires:       perl(Test::More)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Provides:       perl(Ref::Util)
%description
Ref::Util introduces several functions to help identify references in a
faster and smarter way. In short:

%prep
%setup -q -n Ref-Util-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc Changes LICENSE README
%{perl_vendorarch}/auto/*
%{perl_vendorarch}/Ref*
%{_mandir}/man3/*

%changelog
* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.020-1
- Make the Provide explicit
* Thu Jun 09 2016 Nicholas van Oudtshoorn <vanoudt@gmail.com> 0.020-1
- Specfile autogenerated by cpanspec 1.78.
