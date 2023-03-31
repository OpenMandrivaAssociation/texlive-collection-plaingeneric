Name:		texlive-collection-plaingeneric
Version:	65016
Release:	2
Summary:	Plain (La)TeX packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/collection-plaingeneric
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-plaingeneric.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Add-on packages and macros that work with plain TeX, often
LaTeX, and occasionally other formats.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
