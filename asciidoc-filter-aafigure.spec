# TODO: use system fonts (Red Hat Liberation?)
Summary:	aafigure filter for AsciiDoc
Summary(pl.UTF-8):	Filtr aafigure do narzędzia AsciiDoc
Name:		asciidoc-filter-aafigure
Version:	1.1
Release:	1
License:	GPL v2
Group:		Applications/Graphics
#Source0Download: http://code.google.com/p/asciidoc-aafigure-filter/downloads/list
Source0:	http://asciidoc-aafigure-filter.googlecode.com/files/aafigure-filter-%{version}.zip
# Source0-md5:	fc4554dbb973b6b7a2ae8d50de096bbd
URL:		http://code.google.com/p/asciidoc-aafigure-filter/
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	asciidoc >= 8.6.3
Requires:	python-aafigure >= 0.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aafigure is an application for ASCII line art to image conversion.
Using the AsciiDoc aafigure filter, ASCII line art can be embedded
into AsciiDoc documents and processed into either PNG bitmap or SVG
vector graphics.

%description -l pl.UTF-8
aafigure to program do przekształcania rysunków ASCII art na obrazki.
Przy użyciu filtra aafigure do narzędzia AsciiDoc można osadzać
rysunki ASCII art wewnątrz dokumentów AsciiDoc, a nastepnie
przetwarzać je do bitmap PNG lub grafik wektorowych SVG.

%prep
%setup -q -c

sed -i -e '1s,#! /usr/bin/env python,#!/usr/bin/python,' aafig2img.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/asciidoc/filters/aafigure

install aafig2img.py $RPM_BUILD_ROOT/etc/asciidoc/filters/aafigure
cp -p aafigure-filter.conf $RPM_BUILD_ROOT/etc/asciidoc/filters/aafigure
# TODO: symlink system fonts?
cp -p Liberation{Mono,Sans}-Regular.ttf $RPM_BUILD_ROOT/etc/asciidoc/filters/aafigure

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc asciidoc-aafigure-readme.{txt,html} images
%dir /etc/asciidoc/filters/aafigure
%attr(755,root,root) /etc/asciidoc/filters/aafigure/aafig2img.py
/etc/asciidoc/filters/aafigure/aafigure-filter.conf
/etc/asciidoc/filters/aafigure/LiberationMono-Regular.ttf
/etc/asciidoc/filters/aafigure/LiberationSans-Regular.ttf
