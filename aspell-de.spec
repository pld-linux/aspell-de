Summary:	German dictionary for aspell
Summary(de.UTF-8):	Ein deutsches Wörterbuch für aspell
Summary(pl.UTF-8):	Niemiecki słownik dla aspella
Name:		aspell-de
Version:	20161207
%define	subv	7-0
Release:	3
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	https://ftp.gnu.org/gnu/aspell/dict/de/aspell6-de-%{version}-%{subv}.tar.bz2
# Source0-md5:	2648a128c6da53b07133a7747fb9417f
URL:		http://aspell.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
German dictionary (i.e. word list) for aspell.

%description -l de.UTF-8
Ein deutsches Wörterbuch zur Rechtschreibkontrolle nach den neuen
Rechtschreibregeln mit aspell.

%description -l pl.UTF-8
Niemiecki słownik (lista słów) dla aspella.

%prep
%setup -q -n aspell6-de-%{version}-%{subv}

gunzip doc/RSR.gz

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
%doc Copyright doc/{Credits,README}
%lang(de) %doc doc/RSR
%{_prefix}/lib/aspell/de-common.rws
%{_prefix}/lib/aspell/de.multi
%{_prefix}/lib/aspell/de_AT-only.rws
%{_prefix}/lib/aspell/de_AT.multi
%{_prefix}/lib/aspell/de_CH-only.rws
%{_prefix}/lib/aspell/de_CH.multi
%{_prefix}/lib/aspell/de_DE-only.rws
%{_prefix}/lib/aspell/de_DE.multi
%{_prefix}/lib/aspell/deutsch.alias
%{_prefix}/lib/aspell/german.alias
%{_datadir}/aspell/de.dat
%{_datadir}/aspell/de_affix.dat
%{_datadir}/aspell/de_phonet.dat
