Name: dwz
Version: 0.12
Release: 11
Summary: A DWARF optimization and duplicate removal tool
License: GPLv2+ and GPLv3+
URL: https://sourceware.org/dwz/
Source0: %{name}-%{version}.tar.bz2
BuildRequires:gcc elfutils-libelf-devel

%description
The package contains a program that attempts to optimize DWARF debugging
information contained in ELF shared libraries and ELF executables for size,
by replacing DWARF information representation with equivalent smaller
representation where possible and by reducing the amount of duplication
using techniques from DWARF standard appendix E - creating
DW_TAG_partial_unit compilation units (CUs) for duplicated information and
using DW_TAG_imported_unit to import it into each CU that needs it.

%package_help

%prep
%autosetup -n %{name}-%{version}

%build
%make_build

%install
%make_install

%pre

%preun

%post

%postun

%files
%defattr(-,root,root,-)
%license COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz

%files help
%{_mandir}/man1/dwz*

%changelog
* Fri Sep 27 2019 chengquan<chengquan3@huawei.com> - 0.12-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add help package

* Thu Aug 15 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.12-10
- Package init

