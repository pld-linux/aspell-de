Summary:	German dictionary for aspell
Summary(de):	Ein deutsches W�rterbuch f�r aspell
Summary(pl):	Niemiecki s�ownik dla aspella
Name:		aspell-de
Version:	0.1
%define	subv	3
Release:	1
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	http://aspell.sourceforge.net/%{name}-%{version}-%{subv}.tar.bz2
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell
BuildRequires:	pspell-devel
Requires:	aspell
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
German dictionary (i.e. word list) for aspell.

%description -l de
Ein deutsches W�rterbuch zur Rechtschreibkontrolle nach den neuen
Rechtschreibregeln mit aspell.
    
%description -l pl
Niemiecki s�ownik (lista s��w) dla aspella.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/{BUGS,TODO}
%lang(de) %doc doc/{README.*,RSR}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
%{_datadir}/pspell/*