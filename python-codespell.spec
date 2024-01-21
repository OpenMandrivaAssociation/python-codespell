%define oname codespell
Name:           python-codespell
Version:        2.2.6
Release:        1
Summary:        Find and fix common misspellings in text files
Group:          Development/Tools
License:        GPLv2
URL:            https://github.com/lucasdemarchi/codespell
Source0:        https://github.com/lucasdemarchi/codespell/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildArch:      noarch
#BuildRequires:  help2man
BuildRequires:  python
BuildRequires:  python-setuptools

%description
Finds and fixes common misspellings in text files. It is designed
primarily for checking misspelled words in source code, but it can be
used with other files as well.

%prep
%autosetup -n %{oname}-%{version} -p1

%build
%py_build

# Generate manpage
#help2man ./bin/%{oname} --no-discard-stderr \
#  --include %{oname}.1.include --no-info --output %{oname}.1
#sed -i '/\.SS \"Usage/,+2d' %{oname}.1

%install
%py_install

# Install manpage
#install -D -m644 %{oname}.1 %{buildroot}%{_mandir}/man1/%{name}.1

%files
%doc README.rst
%{_bindir}/%{oname}
#{_mandir}/man1/python-codespell.1.*
%{python_sitelib}/%{oname}-%{version}-py%{python_version}.egg-info/
%{python_sitelib}/%{oname}_lib/


