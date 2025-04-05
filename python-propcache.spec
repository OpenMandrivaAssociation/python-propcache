%global debug_package %{nil}
%define module propcache

Name:		python-propcache
Version:	0.3.1
Release:	1
Summary:	Accelerated property cache
URL:		https://pypi.org/project/propcache/
License:	Apache-2.0
Group:		Development/Python
Source0:	https://files.pythonhosted.org/packages/source/p/propcache/%{module}-%{version}.tar.gz
BuildSystem:	python

BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(expandvars)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)



%description
Accelerated property cache

%prep
%autosetup -p1 -n %{module}-%{version}

%build
%py_build

%install
%py_install

%files
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}.dist-info
%license LICENSE
%doc CHANGES.rst README.rst
