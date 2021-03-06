Name: x11-font-bitstream-speedo
Version: 1.0.2
Release: 16
Summary: Xorg X11 font bitstream-speedo
Group: Development/X11
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/font/font-bitstream-speedo-%{version}.tar.bz2
License: MIT
BuildArch: noarch
BuildRequires: fontconfig
BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1
Conflicts: xorg-x11 <= 6.9.0
Requires(post): mkfontdir
Requires(postun): mkfontdir
Requires(post): mkfontscale
Requires(postun): mkfontscale

%description
Xorg X11 font bitstream-speedo

%prep
%setup -q -n font-bitstream-speedo-%{version}

%build
%configure --with-fontdir=%_datadir/fonts/Speedo

%make

%install
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/Speedo/fonts.dir
rm -f %{buildroot}%_datadir/fonts/Speedo/fonts.scale

%post
mkfontscale %_datadir/fonts/Speedo
mkfontdir %_datadir/fonts/Speedo

%postun
mkfontscale %_datadir/fonts/Speedo
mkfontdir %_datadir/fonts/Speedo

%files
%doc COPYING
%dir %_datadir/fonts/Speedo 
%_datadir/fonts/Speedo/font0*.spd
