Summary:	German dictionary for aspell
Summary(de):	Ein deutsches Wörterbuch für aspell
Summary(pl):	Niemiecki s³ownik dla aspella
Name:		aspell-de
Version:	20030222
%define	subv	1
Release:	3
Epoch:		1
License:	GPL v2
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/de/aspell6-de-%{version}-%{subv}.tar.bz2
# Source0-md5:	5950c5c8a36fc93d4d7616591bace6a6
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
German dictionary (i.e. word list) for aspell.

%description -l de
Ein deutsches Wörterbuch zur Rechtschreibkontrolle nach den neuen
Rechtschreibregeln mit aspell.

%description -l pl
Niemiecki s³ownik (lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-de-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README doc/notes.txt
%{_libdir}/aspell/*
%{_datadir}/aspell/*
