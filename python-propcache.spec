%global debug_package %{nil}
%define module propcache

Name:		python-propcache
Summary:	Accelerated property cache
Version:	0.5.2
Release:	1
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/aio-libs/propcache
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(expandvars)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
Accelerated property cache

%build -p
export LDFLAGS="%{ldflags} -lpython%{pyver}"

%files
%doc CHANGES.rst README.rst
%license LICENSE
%{python3_sitearch}/%{module}
%{python3_sitearch}/%{module}-%{version}.dist-info
