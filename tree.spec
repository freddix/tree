Summary:	A utility which displays a tree view of the contents of directories
Name:		tree
Version:	1.7.0
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://mama.indstate.edu/users/ice/tree/src/%{name}-%{version}.tgz
# Source0-md5:	abe3e03e469c542d8e157cdd93f4d8a6
URL:		http://mama.indstate.edu/users/ice/tree/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The tree utility recursively displays the contents of directories in a
tree-like format. Tree is basically a UNIX port of the tree DOS
utility.

%prep
%setup -q

%build
rm -f tree-1.4
%{__make} \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/tree
%{_mandir}/man1/*

