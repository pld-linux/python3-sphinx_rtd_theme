#
# Conditional build:
%bcond_without	tests	# unit tests

%define 	module	sphinx_rtd_theme
Summary:	ReadTheDocs.org theme for Sphinx
Summary(pl.UTF-8):	Motyw ReadTheDocs.org dla Sphinksa
Name:		python3-%{module}
Version:	3.0.2
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_rtd_theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_rtd_theme/%{module}-%{version}.tar.gz
# Source0-md5:	b26e7ff8c3a90817bbc20fb76c530e00
URL:		https://github.com/snide/sphinx_rtd_theme/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-pytest
BuildRequires:	python3-readthedocs-sphinx-ext
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a mobile-friendly Sphinx theme made for readthedocs.org.

%description -l pl.UTF-8
Ten pakiet zawiera przyjazny dla urządzeń przenośnych motyw Sphinksa
wykonany przez readthedocs.org.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}-py*.egg-info
