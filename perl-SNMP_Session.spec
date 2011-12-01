Name:           perl-SNMP_Session
Version:        1.12
Release:        4%{?dist}
Summary:        SNMP support for Perl 5

Group:          Development/Libraries
License:        Artistic 2.0
URL:            http://www.switch.ch/misc/leinen/snmp/perl/
Source0:        http://www.switch.ch/misc/leinen/snmp/perl/dist/SNMP_Session-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(ExtUtils::MakeMaker)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Pure Perl SNMP v1 and SNMP v2 support for Perl 5.

The SNMP operations currently supported are "get", "get-next", "get-bulk"
and "set", as well as trap generation and reception. 


%prep
%setup -q -n SNMP_Session-%{version}
%{__perl} -pi -e 's{^#!/usr/local/bin/perl\b}{#!%{__perl}}' test/*
chmod -c 644 test/*


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Artistic README README.SNMP_util index.html test/
%{perl_vendorlib}/*


%changelog
* Mon Dec  7 2009 Stepan Kasal <skasal@redhat.com> - 1.12-4
- rebuild against perl 5.10.1

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Apr 22 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.12-1
- update to 1.12 (license change to Artistic 2.0)

* Thu Mar 06 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-4.1
- Rebuild for new perl

* Tue Oct 16 2007 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-3.1
- add BR: perl(ExtUtils::MakeMaker)

* Thu Sep  7 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-3
- Rebuild for FC6.

* Thu Mar  9 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-2
- Rebuild for FC5 (perl 5.8.8).

* Thu Dec 29 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-1
- Update to 1.08.

* Tue Sep 13 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-2
- Removed superfluous perl BR.

* Wed Aug 10 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.07-1
- Update to Fedora Extras template.

* Wed Nov 24 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.07-0.fdr.1
- Update to 1.07.

* Sun Oct  3 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.06-0.fdr.1
- Update to 1.06.

* Wed Aug 25 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.05-0.fdr.2
- The homepage changed placed in 2004-08-23.
- The author repackaged the files using the same tar.gz version (1.05).

* Wed Jul 21 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.05-0.fdr.1
- Update to 1.05.

* Tue May 18 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.03-0.fdr.1
- First build.
