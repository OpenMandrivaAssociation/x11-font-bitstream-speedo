Name: x11-font-bitstream-speedo
Version: 1.0.0
Release: %mkrel 4
Summary: Xorg X11 font bitstream-speedo
Group: Development/X11
URL: http://xorg.freedesktop.org
Source: http://xorg.freedesktop.org/releases/individual/font/font-bitstream-speedo-%{version}.tar.bz2
License: CHECK
BuildRoot: %{_tmppath}/%{name}-root
BuildArch: noarch

BuildRequires: x11-font-util >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

Conflicts: xorg-x11 <= 6.9.0
PreReq: mkfontdir
PreReq: mkfontscale

%description
Xorg X11 font bitstream-speedo

%prep
%setup -q -n font-bitstream-speedo-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir} --with-fontdir=%_datadir/fonts/Speedo

%make

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%_datadir/fonts/Speedo/fonts.dir
rm -f %{buildroot}%_datadir/fonts/Speedo/fonts.scale

%post
mkfontscale %_datadir/fonts/Speedo
mkfontdir %_datadir/fonts/Speedo

%postun
mkfontscale %_datadir/fonts/Speedo
mkfontdir %_datadir/fonts/Speedo

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %_datadir/fonts/Speedo 
%_datadir/fonts/Speedo/font0*.spd


