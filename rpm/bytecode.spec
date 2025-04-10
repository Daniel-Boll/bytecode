%global pypi_name bytecode

%define __python python3

Name:           python3-%{pypi_name}
Version:        %{version_placeholder}
Release:        0
Summary:        Python module to generate and modify bytecode

License:        MIT
URL:            https://github.com/MatthieuDartiailh/bytecode
Source0:        %{pypi_name}-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel

Requires:       python3 >= 3.8

%description
Bytecode is a Python module providing tools to generate, modify, and analyze
Python bytecode. It allows programmatic manipulation of code objects,
useful for metaprogramming, code generation, optimization, and analysis tasks.

%prep
%autosetup -n %{pypi_name}-%{version}

%build
%{__python} -m pip install "setuptools_scm[toml]>=3.4.3"
%{__python} -m build --wheel --no-isolation

%install
%{__python} -m pip install --no-index --root=%{buildroot} --prefix=%{_prefix} --verbose dist/*.whl

%files
%license COPYING
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-*.dist-info/

%changelog
* Tue Apr 09 2024 Daniel Boll <danielboll.dev@proton.me> - %{version}-%{release}
- Initial RPM packaging for bytecode.
