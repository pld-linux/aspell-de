Summary:	German dictionary for aspell
Summary(de):	Ein deutsches Wörterbuch für aspell
Summary(pl):	Niemiecki s³ownik dla aspella
Name:		aspell-de
Version:	0.1
%define	subv	3
Release:	1
License:	GPL v2
Group:		Applications/Text
Source0:	http://aspell.sourceforge.net/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell
Requires:	aspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
German dictionary (i.e. word list) for aspell.

%description -l de
Ein deutsches Wörterbuch zur Rechtschreibkontrolle nach den neuen
Rechtschreibregeln mit aspell.
    
%description -l pl
Niemiecki s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n %{name}-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f doc/{README,README.de}
gzip -9nf README doc/{BUGS,README.*,RSR,TODO}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz doc/{BUGS,TODO}.gz
%lang(de) %doc doc/{README.*,RSR}.gz
%{_libdir}/aspell/*
%{_datadir}/aspell/*
%{_datadir}/pspell/*
