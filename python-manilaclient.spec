#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-manilaclient
Version  : 1.11.0
Release  : 15
URL      : http://tarballs.openstack.org/python-manilaclient/python-manilaclient-1.11.0.tar.gz
Source0  : http://tarballs.openstack.org/python-manilaclient/python-manilaclient-1.11.0.tar.gz
Summary  : Client library for OpenStack Manila API.
Group    : Development/Tools
License  : Apache-2.0
Requires: python-manilaclient-bin
Requires: python-manilaclient-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Python bindings to the OpenStack Manila API
===========================================

%package bin
Summary: bin components for the python-manilaclient package.
Group: Binaries

%description bin
bin components for the python-manilaclient package.


%package python
Summary: python components for the python-manilaclient package.
Group: Default

%description python
python components for the python-manilaclient package.


%prep
%setup -q -n python-manilaclient-1.11.0

%build
export LANG=C
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/manila

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
