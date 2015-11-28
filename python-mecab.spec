Summary:	MeCab module for Python
Summary(pl.UTF-8):	Moduł MeCab dla Pythona
Name:		python-mecab
Version:	0.996
Release:	2
License:	GPL v2 or LGPL v2.1 or BSD
Group:		Development/Languages/Python
#Source0Download: http://code.google.com/p/mecab/downloads/list
Source0:	http://mecab.googlecode.com/files/mecab-python-%{version}.tar.gz
# Source0-md5:	167da6c5f3865262852853efbd240c0e
URL:		http://code.google.com/p/mecab/
BuildRequires:	libstdc++-devel
BuildRequires:	mecab-devel >= 0.996
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	mecab >= 0.996
Requires:	python-libs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MeCab module for Python.

%description -l pl.UTF-8
Moduł MeCab dla Pythona.

%prep
%setup -q -n mecab-python-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BSD COPYING README bindings.html
%{py_sitedir}/MeCab.py[co]
%attr(755,root,root) %{py_sitedir}/_MeCab.so
%if "%{py_ver}" > "2.4"
%{py_sitedir}/mecab_python-%{version}-py*.egg-info
%endif
