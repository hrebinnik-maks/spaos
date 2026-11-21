Name:           count-files
Version:        1.0
Release:        2%{?dist}
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
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 count_files.1 %{buildroot}%{_mandir}/man1/count_files.1

%pre
echo "Preparing to install count-files..."

%post
echo "count-files installed successfully!"
echo "Run 'sudo count_files' to use the script."

%files
%{_bindir}/count_files
%{_mandir}/man1/count_files.1*

%changelog
* Fri Nov 13 2026 Maksym Hrebinnyk <grebinnikmaksim8@gmail.com> - 1.0-2
- Add man page to package

* Thu Nov 12 2026 Maksym Hrebinnyk <grebinnikmaksim8@gmail.com> - 1.0-1
- Initial release

