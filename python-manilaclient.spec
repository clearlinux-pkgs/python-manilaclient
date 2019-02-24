#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x1A541148054E9E38 (infra-root@openstack.org)
#
Name     : python-manilaclient
Version  : 1.26.0
Release  : 28
URL      : http://tarballs.openstack.org/python-manilaclient/python-manilaclient-1.26.0.tar.gz
Source0  : http://tarballs.openstack.org/python-manilaclient/python-manilaclient-1.26.0.tar.gz
Source99 : http://tarballs.openstack.org/python-manilaclient/python-manilaclient-1.26.0.tar.gz.asc
Summary  : Client library for OpenStack Manila API
Group    : Development/Tools
License  : Apache-2.0
Requires: python-manilaclient-bin = %{version}-%{release}
Requires: python-manilaclient-license = %{version}-%{release}
Requires: python-manilaclient-python = %{version}-%{release}
Requires: python-manilaclient-python3 = %{version}-%{release}
Requires: Babel
Requires: debtcollector
Requires: docutils
Requires: ipaddress
Requires: oslo.config
Requires: oslo.log
Requires: oslo.serialization
Requires: oslo.utils
Requires: pbr
Requires: python-keystoneclient
Requires: requests
Requires: simplejson
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : pbr

%description
========================
Team and repository tags
========================
.. image:: https://governance.openstack.org/tc/badges/python-manilaclient.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

%package bin
Summary: bin components for the python-manilaclient package.
Group: Binaries
Requires: python-manilaclient-license = %{version}-%{release}

%description bin
bin components for the python-manilaclient package.


%package license
Summary: license components for the python-manilaclient package.
Group: Default

%description license
license components for the python-manilaclient package.


%package python
Summary: python components for the python-manilaclient package.
Group: Default
Requires: python-manilaclient-python3 = %{version}-%{release}

%description python
python components for the python-manilaclient package.


%package python3
Summary: python3 components for the python-manilaclient package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-manilaclient package.


%prep
%setup -q -n python-manilaclient-1.26.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551035717
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-manilaclient
cp LICENSE %{buildroot}/usr/share/package-licenses/python-manilaclient/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/manila

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/python-manilaclient/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
