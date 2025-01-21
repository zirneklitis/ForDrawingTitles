%define catalogue %{_sysconfdir}/X11/fontpath.d
%global priority  63
%global fontname  ForDrawingTitles

Name:             %{fontname}-fonts
Summary:          The font “For Drawing Titles” mimics the poster titles drawn by hand.
Version:          1.0.0
Release:          K02%{?dist}
Packager:         Kārlis Kalviškis
License:          SIL OFL
Group:            User Interface/X
URL:              http://priede.bf.lu.lv/ftp/Linux/Fedora/
Source0:          %{fontname}-%{version}.tar.xz
Source1:          %{fontname}.conf
BuildArch:        noarch
BuildRequires:    fontpackages-devel >= 1.13, xorg-x11-font-utils
BuildRequires:    fontforge
BuildRequires:    make
BuildRequires:    mkfontscale

%description

But this font is not very hand-made – the outlines are clean. The font
has four different weights – light, regular, bold and black. The weight
changes the visual appearance but not the width or height of symbols.
So the text written using the black weight takes the same space as
written using light weight.

As the font name suggests, it's suitable for large font size not for
small ones.



%prep
%setup -n  %{fontname}-%{version}

%build
make %{?_smp_mflags} 
mv  %{fontname}-ttf-%{version}/* .


%install
# fonts .ttf
install -m 0755 -d %{buildroot}%{_fontdir}
install -m 0644 -p *.ttf %{buildroot}%{_fontdir}
# catalogue
install -m 0755 -d %{buildroot}%{catalogue}
ln -s %{_fontdir} %{buildroot}%{catalogue}/%{fontname}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

%global fconf  %{priority}-%{fontname}.conf
install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/%{fconf}
ln -s %{_fontconfig_templatedir}/%{fconf} \
        %{buildroot}%{_fontconfig_confdir}/%{fconf}

# fonts.{dir,scale}
mkfontscale %{buildroot}%{_fontdir}
mkfontdir %{buildroot}%{_fontdir}

mkdir -p ${RPM_BUILD_ROOT}%{_docdir}/%{fontname}
cp AUTHORS ChangeLog COPYING README TODO ${RPM_BUILD_ROOT}%{_docdir}/%{fontname}

%files
%defattr(-,root,root)
%{_datadir}
# % dir % {_fontdir}
%{catalogue}/%{fontname}
%{_fontconfig_confdir}


%changelog

* Mon Jan 20 2025 Kārlis Kalviškis <karlo@lu.lv> - 1.0.0-K02
- Inital packaging
