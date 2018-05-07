Name:       plr-hawq
Summary:    PL/R module for HAWQ
Version:    08.03.00.14.%{hawq_version}
Release:    %{hawq_build_number}.%{os_version_distro}
License:    GPL
Group:      Applications/Databases
Prefix:     /usr/local
Requires:   plr-hawq_%{hawq_version_str}

AutoReqProv:    no

%description
This is the virtual rpm package of plr-hawq.

%prep

%install

%clean

%post

%postun

%files
