# revision 23089
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-afm2pl
Version:	20111103
Release:	1
Summary:	TeXLive afm2pl package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afm2pl.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/afm2pl.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Requires:	texlive-afm2pl.bin
Provides:	tetex-afm = %{version}
Provides:	texlive-afm = %{version}
Provides:	texlive-texmf-afm = %{version}
Obsoletes:	tetex-afm <= 3.0
Conflicts:	tetex-afm <= 3.0
Obsoletes:	texlive-afm <= 2007
Conflicts:	texlive-afm <= 2007
Obsoletes:	texlive-texmf-afm <= 2007
Conflicts:	texlive-texmf-afm <= 2007
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive afm2pl package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
