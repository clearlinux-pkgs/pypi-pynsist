#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pynsist
Version  : 2.8
Release  : 8
URL      : https://files.pythonhosted.org/packages/99/e0/b1b797633a71fadb5e37b44b69a707bf1f3108f1922d25bbb82d320af0cd/pynsist-2.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/99/e0/b1b797633a71fadb5e37b44b69a707bf1f3108f1922d25bbb82d320af0cd/pynsist-2.8.tar.gz
Summary  : Build NSIS installers for Python applications.
Group    : Development/Tools
License  : MIT
Requires: pypi-pynsist-bin = %{version}-%{release}
Requires: pypi-pynsist-license = %{version}-%{release}
Requires: pypi-pynsist-python = %{version}-%{release}
Requires: pypi-pynsist-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(poetry_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
Pynsist is a tool to build Windows installers for your Python applications. The
installers bundle Python itself, so you can distribute your application to
people who don't have Python installed.

%package bin
Summary: bin components for the pypi-pynsist package.
Group: Binaries
Requires: pypi-pynsist-license = %{version}-%{release}

%description bin
bin components for the pypi-pynsist package.


%package license
Summary: license components for the pypi-pynsist package.
Group: Default

%description license
license components for the pypi-pynsist package.


%package python
Summary: python components for the pypi-pynsist package.
Group: Default
Requires: pypi-pynsist-python3 = %{version}-%{release}

%description python
python components for the pypi-pynsist package.


%package python3
Summary: python3 components for the pypi-pynsist package.
Group: Default
Requires: python3-core
Provides: pypi(pynsist)
Requires: pypi(distlib)
Requires: pypi(jinja2)
Requires: pypi(requests)
Requires: pypi(requests_download)
Requires: pypi(yarg)

%description python3
python3 components for the pypi-pynsist package.


%prep
%setup -q -n pynsist-2.8
cd %{_builddir}/pynsist-2.8
pushd ..
cp -a pynsist-2.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656398940
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pynsist
cp %{_builddir}/pynsist-2.8/LICENSE %{buildroot}/usr/share/package-licenses/pypi-pynsist/744d155856cad539df9e13c3ed4a29f3539d3433
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pynsist

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pynsist/744d155856cad539df9e13c3ed4a29f3539d3433

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
