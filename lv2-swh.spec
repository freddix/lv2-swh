Summary:	SWH LV2 plugins
Name:		lv2-swh
Version:	1.0.15
Release:	1
License:	GPL v3
Group:		X11/Applications/Sound
# git://github.com/swh/lv2.git
Source0:	%{name}-%{version}.tar.xz
# Source0-md5:	e7fd6f63cc9f62362866c1c34b24627b
BuildRequires:	fftw3-single-devel
BuildRequires:	libxslt-progs
BuildRequires:	lv2-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LV2 port of SWH plugins.

%prep
%setup -q

%build
export CFLAGS="%{rpmcflags}"
export LDFLAGS="%{rpmldflags}"
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install-system	\
	PREFIX=%{_prefix}	\
	INSTALL_DIR="$RPM_BUILD_ROOT%{_libdir}/lv2"

_DIR=$(pwd)
cd $RPM_BUILD_ROOT%{_libdir}/lv2

echo "%defattr(644,root,root,755)" > $_DIR/files.plugins
for dir in *; do
    echo "%dir %{_libdir}/lv2/$dir" >> $_DIR/files.plugins
    echo "%attr(755,root,root) %{_libdir}/lv2/$dir/plugin-Linux.so" >> $_DIR/files.plugins
    echo "%{_libdir}/lv2/$dir/manifest.ttl" >> $_DIR/files.plugins
    echo "%{_libdir}/lv2/$dir/plugin.ttl" >> $_DIR/files.plugins
done

%clean
rm -rf $RPM_BUILD_ROOT

%files -f files.plugins
%doc README

