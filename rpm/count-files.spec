Name:           count-files
Version:        1.0
Release:        1%{?dist}
Summary:        Bash script for counting files

License:        MIT
URL:            https://github.com/hrebinnik-maks/spaos
Source0:        %{name}-%{version}.tar.gz
BuildArch:      noarch

Requires:       bash
Requires:       coreutils
Requires:       findutils
Requires:       gawk

%description
A Bash script for counting files in a specified directory,
including recursive search and file size calculation.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 count_files.sh %{buildroot}%{_bindir}/count_files

%pre
echo "Preparing to install count-files..."

%post
echo "count-files installed successfully!"
echo "Run 'sudo count_files' to use the script."

%files
%{_bindir}/count_files

%changelog
* Thu Nov 12 2026 Maksym Hrebinnyk - 1.0-1
- Initial release

