%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	TreeMenu
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_class}_%{_subclass} - Provides an api to create a HTML tree
Summary(pl):	%{_class}_%{_subclass} - Dostarcza API do tworzenia drzew HTML
Name:		php-pear-%{_pearname}
Version:	1.0.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
BuildRequires:	rpm-php-pearprov
URL:		http://pear.php.net/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP Based api creates a tree structure using a couple of small PHP
classes. This can then be converted to javascript using the
printMenu() method. The tree should be dynamic in IE 4 or higher and
NN6/Mozilla, and in IE 5 or higher it maintains state (the
collapsed/expanded status of the branches). Has only been tested under
IE6 however. Other browser display the tree fully expanded. Each node
can have an optional link and icon. An example of this in action is
available at http://www.phpguru.org/treemenu.php

%description -l pl

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
cd %{_pearname}-%{version}

install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{images,imagesAlt}

install *.{php,js}		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install images/*		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/images
install imagesAlt/*		$RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/imagesAlt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{php_pear_dir}/%{_class}/{images,imagesAlt}
%doc %{_pearname}-%{version}/docs/*
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/*.js
%{php_pear_dir}/%{_class}/images/*
%{php_pear_dir}/%{_class}/imagesAlt/*
