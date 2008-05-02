%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	TreeMenu
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides an api to create a HTML tree
Summary(pl.UTF-8):	%{_pearname} - dostarcza API do tworzenia drzew HTML
Name:		php-pear-%{_pearname}
Version:	1.2.1
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6f2693c215555b637a7b643548e81dfb
URL:		http://pear.php.net/package/HTML_TreeMenu/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP based API creates a tree structure using a couple of small PHP
classes. This can then be converted to javascript using the
printMenu() method. The tree should be dynamic in IE 4 or higher and
NN6/Mozilla, and in IE 5 or higher it maintains state (the
collapsed/expanded status of the branches). Has only been tested under
IE6 however. Other browsers display the tree fully expanded. Each node
can have an optional link and icon. An example of this in action is
available at <http://www.phpguru.org/treemenu.php>.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
To oparte na PHP API tworzy strukturę drzewa przy użyciu zestawu
małych klas PHP. Drzewo to może być przekonwertowane do JavaScriptu
przy użyciu metody printMenu(). Drzewo powinno być dynamiczne w: IE 4
lub nowszym oraz NN6/Mozilli; zachowuje stan (zwinięcie/rozwinięcie
rozgałęzień) w IE 5 lub nowszym, ale było to testowane tylko w IE 6.
Inne przeglądarki wyświetlają drzewo w pełni rozwinięte. Każdy liść
może mieć opcjonalny odnośnik i ikonkę. Przykład takiego działania
jest dostępny pod adresem <http://www.phpguru.org/treemenu.php>.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

install -d docs/%{_pearname}
mv ./%{php_pear_dir}/%{_class}/docs/* docs/%{_pearname}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/%{_class}/*.php

%{php_pear_dir}/data/%{_pearname}
