Name: dwz
Version: 0.14
Release: 5
Summary: A DWARF optimization and duplicate removal tool
License: GPLv2+ and GPLv3+
URL: https://sourceware.org/dwz/
Source0:https://sourceware.org/ftp/dwz/releases/%{name}-%{version}.tar.xz
BuildRequires:gcc gcc-c++ gdb elfutils-libelf-devel dejagnu

Patch1: testsuite-Handle-readelf-following-links-by-default.patch
Patch2: backport-Redirect-stder-in-gdb-add-index.sh-test.patch

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
%autosetup -n %{name} -p1

%build
make %{?_smp_mflags} CFLAGS='%{optflags}' LDFLAGS='%{build_ldflags}' \
  prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir}
#%%make_build

%install
#%rm -rf %{buildroot}
make DESTDIR=%{buildroot} prefix=%{_prefix} mandir=%{_mandir} bindir=%{_bindir} \
  install
#%%make_install

%pre

%preun

%post

%postun
%check
make check

%files
%defattr(-,root,root,-)
%license COPYING COPYING3 COPYING.RUNTIME
%{_bindir}/dwz

%files help
%{_mandir}/man1/dwz*

%changelog
* Tue Jan 10 2023 dongyuzhen <dongyuzhen@h-partners.com> - 0.14-5
- fix the testcase fail

* Tue Oct 25 2022 yanglongkang <yanglongkang@h-partners.com> - 0.14-4
- rebuild for next release

* Tue Jan 25 2022 renhongxun <renhongxun@h-partner.com> - 0.14-3
- fix testsuite with community patch

* Mon Oct 25 2021 caodongxia <caodongxia@huawei.com> - 0.14-2
- Add buildRequire gcc-c++ and gdb

* Sat Jul 24 2021 shixuantong <shixuantong@huawei.com> - 0.14-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:update version to 0.14

* Mon Jul 27 2020 wenzhanli<wenzhanli2@huawei.com> - 0.13-1
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:version update 0.13

* Fri Sep 27 2019 chengquan<chengquan3@huawei.com> - 0.12-11
- Type:bugfix
- ID:NA
- SUG:NA
- DESC:add help package

* Thu Aug 15 2019 openEuler Buildteam <buildteam@openeuler.org> - 0.12-10
- Package init

