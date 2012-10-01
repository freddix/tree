Summary:	A utility which displays a tree view of the contents of directories
Name:		tree
Version:	1.6.0
Release:	1
License:	GPL
Group:		Applications/File
Source0:	http://mama.indstate.edu/users/ice/tree/src/%{name}-%{version}.tgz
# Source0-md5:	04e967a3f4108d50cde3b4b0e89e970a
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

