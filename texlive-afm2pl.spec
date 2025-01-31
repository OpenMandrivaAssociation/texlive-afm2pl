Name:		texlive-afm2pl
Version:	71515
Release:	1
Summary:	TeXLive afm2pl package
Group:		Publishing
URL:		https://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afm2pl.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afm2pl.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-afm2pl.bin
%rename tetex-afm
%rename texlive-texmf-afm

%description
TeXLive afm2pl package.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/enc/dvips/afm2pl/afm2pl-ot1.enc
%{_texmfdistdir}/fonts/enc/dvips/afm2pl/afm2pl-ot1ital.enc
%{_texmfdistdir}/fonts/enc/dvips/afm2pl/afm2pl-ot1tt.enc
%{_texmfdistdir}/fonts/enc/dvips/afm2pl/afm2pl-texnanlc.enc
%{_texmfdistdir}/fonts/enc/dvips/afm2pl/afm2pl-texnanuc.enc
%{_texmfdistdir}/fonts/lig/afm2pl/accents.lig
%{_texmfdistdir}/fonts/lig/afm2pl/bound.lig
%{_texmfdistdir}/fonts/lig/afm2pl/default.lig
%{_texmfdistdir}/fonts/lig/afm2pl/defpost.lig
%{_texmfdistdir}/fonts/lig/afm2pl/defpre.lig
%{_texmfdistdir}/fonts/lig/afm2pl/forge.lig
%{_texmfdistdir}/fonts/lig/afm2pl/ligtex.lig
%{_texmfdistdir}/tex/fontinst/afm2pl/README
%{_texmfdistdir}/tex/fontinst/afm2pl/ly1.etx
%{_texmfdistdir}/tex/fontinst/afm2pl/ly1c.etx
%{_texmfdistdir}/tex/fontinst/afm2pl/makesc8y.tex
%doc %{_mandir}/man1/afm2pl.1*
%doc %{_texmfdistdir}/doc/man/man1/afm2pl.man1.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
