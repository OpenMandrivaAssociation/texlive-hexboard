Name:		texlive-hexboard
Version:	62102
Release:	2
Summary:	For drawing Hex boards and games
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/hexboard
License:	cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexboard.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexboard.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hexboard.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
hexboard is a package for LaTeX that should also work with
LuaTeX and XeTeX, that provides functionality for drawing Hex
boards and games. The aim is a clean, clear design with
flexibility for drawing different sorts of Hex diagrams.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/hexboard
%{_texmfdistdir}/tex/latex/hexboard
%doc %{_texmfdistdir}/doc/latex/hexboard

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
