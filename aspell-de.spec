Summary:	German dictionary for aspell
Summary(de):	Ein deutsches Wörterbuch für aspell
Summary(pl):	Niemiecki s³ownik dla aspella
Name:		aspell-de
Version:	0.50
%define	subv	2
Release:	3
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/de/%{name}-%{version}-%{subv}.tar.bz2
# Source0-md5:	204a9737ff0110fb8c7d284bd7200f7d
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.50.0
Requires:	aspell >= 3:0.50.0
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README doc/{BUGS,TODO}
%lang(de) %doc doc/{README.*,RSR}
%{_libdir}/aspell/*
%{_datadir}/aspell/*
