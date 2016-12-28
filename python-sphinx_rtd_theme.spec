#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	sphinx_rtd_theme
Summary:	ReadTheDocs.org theme for Sphinx, 2013 version
Summary(pl.UTF-8):	Motyw ReadTheDocs.org dla Sphinksa, wersja z 2013 roku
Name:		python-%{module}
Version:	0.1.9
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/sphinx_rtd_theme
Source0:	https://pypi.python.org/packages/source/s/sphinx_rtd_theme/%{module}-%{version}.tar.gz
# Source0-md5:	86a25c8d47147c872e42dc84cc66f97b
URL:		https://github.com/snide/sphinx_rtd_theme/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a mobile-friendly Sphinx theme made for readthedocs.org.

%description -l pl.UTF-8
Ten pakiet zawiera przyjazny dla urządzeń przenośnych motyw Sphinksa
wykonany przez readthedocs.org.

%package -n python3-%{module}
Summary:	ReadTheDocs.org theme for Sphinx, 2013 version
Summary(pl.UTF-8):	Motyw ReadTheDocs.org dla Sphinksa, wersja z 2013 roku
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
This is a mobile-friendly Sphinx theme made for readthedocs.org.

%description -n python3-%{module} -l pl.UTF-8
Ten pakiet zawiera przyjazny dla urządzeń przenośnych motyw Sphinksa
wykonany przez readthedocs.org.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
%endif
