Name:           count-files
Version:        2.0
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
mkdir -p %{buildroot}%{_mandir}/man1
install -m 644 count_files.1 %{buildroot}%{_mandir}/man1/count_files.1
mkdir -p %{buildroot}%{_sysconfdir}
install -m 644 count-files.conf %{buildroot}%{_sysconfdir}/count-files.conf

%pre
echo "Preparing to install count-files..."

%post
echo "count-files installed successfully!"
echo "Run 'sudo count_files' to use the script."

%files
%{_bindir}/count_files
%{_mandir}/man1/count_files.1*
%config(noreplace) %{_sysconfdir}/count-files.conf

%changelog
* Mon Nov 16 2026 Maksym Hrebinnyk <grebinnikmaksim8@gmail.com> - 2.0-1
- Add configuration file support
- Release version 2.0

* Fri Nov 13 2026 Maksym Hrebinnyk <grebinnikmaksim8@gmail.com> - 1.0-2
- Add man page to package

* Thu Nov 12 2026 Maksym Hrebinnyk <grebinnikmaksim8@gmail.com> - 1.0-1
- Initial release

