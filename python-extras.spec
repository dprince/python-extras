Name:           python-extras
Version:        0.0.2
Release:        1%{?dist}
Summary:        Extra code that should be part of the standard library but isn't.

Group:      Development/Languages
License:    MIT
URL:            https://github.com/testing-cabal/extras
Source0:        http://pypi.python.org/packages/source/s/extras/extras-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python-devel
BuildRequires:  python-setuptools

%description
Extra code that should be part of the standard library but isn't.

%prep
%setup -q -n extras-%{version}

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst LICENSE
%{python_sitelib}/extras
%{python_sitelib}/extras-%{version}-py?.?.egg-info

%changelog
* Sun Jan 13 2013 Dan Prince - 0.0.2-1
- Initial package.
