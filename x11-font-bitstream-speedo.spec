Name: x11-font-bitstream-speedo
Version: 1.0.2
Release: 17
Summary: Xorg X11 font bitstream-speedo
Group: Development/X11
URL: https://xorg.freedesktop.org
Source0: https://xorg.freedesktop.org/releases/individual/font/font-bitstream-speedo-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: pkgconfig(fontutil) >= 1.0.1
BuildRequires: pkgconfig(xorg-macros) >= 1.1.5
Requires(post,postun): mkfontscale

%description
Xorg X11 font bitstream-speedo.

%prep
%autosetup -p1 -n font-bitstream-speedo-%{version}

%build
%configure --with-fontdir=%{_datadir}/fonts/Speedo

%make_build

%install
%make_install
rm -f %{buildroot}%{_datadir}/fonts/Speedo/fonts.dir
rm -f %{buildroot}%{_datadir}/fonts/Speedo/fonts.scale

%post
mkfontscale %{_datadir}/fonts/Speedo
mkfontdir %{_datadir}/fonts/Speedo

%postun
mkfontscale %{_datadir}/fonts/Speedo
mkfontdir %{_datadir}/fonts/Speedo

%files
%doc COPYING
%dir %{_datadir}/fonts/Speedo 
%{_datadir}/fonts/Speedo/font0*.spd
