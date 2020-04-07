#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : microversion_parse
Version  : 1.0.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/1c/bb/ffeb8ac7acfe77425220352f1338e164ceb1177fdb69f7bcbc6750ca878d/microversion_parse-1.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/1c/bb/ffeb8ac7acfe77425220352f1338e164ceb1177fdb69f7bcbc6750ca878d/microversion_parse-1.0.1.tar.gz
Summary  : OpenStack microversion header parser
Group    : Development/Tools
License  : Apache-2.0
Requires: microversion_parse-license = %{version}-%{release}
Requires: microversion_parse-python = %{version}-%{release}
Requires: microversion_parse-python3 = %{version}-%{release}
Requires: WebOb
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
microversion_parse
==================
A small set of functions to manage OpenStack `microversion`_ headers that can
be used in middleware, application handlers and decorators to effectively
manage microversions.

%package license
Summary: license components for the microversion_parse package.
Group: Default

%description license
license components for the microversion_parse package.


%package python
Summary: python components for the microversion_parse package.
Group: Default
Requires: microversion_parse-python3 = %{version}-%{release}

%description python
python components for the microversion_parse package.


%package python3
Summary: python3 components for the microversion_parse package.
Group: Default
Requires: python3-core
Provides: pypi(microversion_parse)
Requires: pypi(webob)

%description python3
python3 components for the microversion_parse package.


%prep
%setup -q -n microversion_parse-1.0.1
cd %{_builddir}/microversion_parse-1.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1586271974
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/microversion_parse
cp %{_builddir}/microversion_parse-1.0.1/LICENSE %{buildroot}/usr/share/package-licenses/microversion_parse/92170cdc034b2ff819323ff670d3b7266c8bffcd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/microversion_parse/92170cdc034b2ff819323ff670d3b7266c8bffcd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
