%global tl_name hexboard
%global tl_revision 62102

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	For drawing Hex boards and games
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/hexboard
License:	cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hexboard.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hexboard.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hexboard.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
hexboard is a package for LaTeX that should also work with LuaTeX and
XeTeX, that provides functionality for drawing Hex boards and games. The
aim is a clean, clear design with flexibility for drawing different
sorts of Hex diagrams.

