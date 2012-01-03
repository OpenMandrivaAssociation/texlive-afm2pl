# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-afm2pl
Version:	20111103
Release:	3
Summary:	TeXLive afm2pl package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afm2pl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afm2pl.doc.tar.xz
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
%{_texmfdir}/fonts/enc/dvips/afm2pl/afm2pl-ot1.enc
%{_texmfdir}/fonts/enc/dvips/afm2pl/afm2pl-ot1ital.enc
%{_texmfdir}/fonts/enc/dvips/afm2pl/afm2pl-ot1tt.enc
%{_texmfdir}/fonts/enc/dvips/afm2pl/afm2pl-texnanlc.enc
%{_texmfdir}/fonts/enc/dvips/afm2pl/afm2pl-texnanuc.enc
%{_texmfdir}/fonts/lig/afm2pl/accents.lig
%{_texmfdir}/fonts/lig/afm2pl/bound.lig
%{_texmfdir}/fonts/lig/afm2pl/default.lig
%{_texmfdir}/fonts/lig/afm2pl/defpost.lig
%{_texmfdir}/fonts/lig/afm2pl/defpre.lig
%{_texmfdir}/fonts/lig/afm2pl/forge.lig
%{_texmfdir}/fonts/lig/afm2pl/ligtex.lig
%{_texmfdir}/tex/fontinst/afm2pl/README
%{_texmfdir}/tex/fontinst/afm2pl/ly1.etx
%{_texmfdir}/tex/fontinst/afm2pl/ly1c.etx
%{_texmfdir}/tex/fontinst/afm2pl/makesc8y.tex
%doc %{_mandir}/man1/afm2pl.1*
%doc %{_texmfdir}/doc/man/man1/afm2pl.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
