%include	/usr/lib/rpm/macros.php
%define		_class		HTML
%define		_subclass	TreeMenu
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - provides an api to create a HTML tree
Summary(pl):	%{_pearname} - dostarcza API do tworzenia drzew HTML
Name:		php-pear-%{_pearname}
Version:	1.2.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	29702b4e7fa6a3b716c1cf2deda063f0
URL:		http://pear.php.net/package/HTML_TreeMenu/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
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
available at http://www.phpguru.org/treemenu.php .

In PEAR status of this package is: %{_status}.

%description -l pl
To oparte na PHP API tworzy struktur� drzewa przy u�yciu zestawu
ma�ych klas PHP. Drzewo to mo�e by� przekonwertowane do JavaScriptu
przy u�yciu metody printMenu(). Drzewo powinno by� dynamiczne w: IE 4
lub nowszym oraz NN6/Mozilli; zachowuje stan (zwini�cie/rozwini�cie
rozga��zie�) w IE 5 lub nowszym, ale by�o to testowane tylko w IE 6.
Inne przegl�darki wy�wietlaj� drzewo w pe�ni rozwini�te. Ka�dy li��
mo�e mie� opcjonalny odno�nik i ikonk�. Przyk�ad takiego dzia�ania
jest dost�pny pod adresem http://www.phpguru.org/treemenu.php .

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/{images,imagesAlt{,2}}

install %{_pearname}-%{version}/*.{php,js} $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/
install %{_pearname}-%{version}/images/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/images
install %{_pearname}-%{version}/imagesAlt/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/imagesAlt
install %{_pearname}-%{version}/imagesAlt2/* $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/imagesAlt2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{php_pear_dir}/%{_class}/images
%dir %{php_pear_dir}/%{_class}/imagesAlt
%dir %{php_pear_dir}/%{_class}/imagesAlt2
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/*.js
%{php_pear_dir}/%{_class}/images/*
%{php_pear_dir}/%{_class}/imagesAlt/*
%{php_pear_dir}/%{_class}/imagesAlt2/*
