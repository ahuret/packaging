Name:           ALUMET
Version:        0.5.0
Release:        1%{?dist}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}_v%{version}.tar.gz
BuildArch:      x86_64


# Disable this line if you wish to support all platforms.
# In most situations, you will likely only target tier1 arches for user facing components.
 
%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices. 
 
%prep
%autosetup -n %{name}

 
%build
%{cargo_build}
 
%install
pwd
ls -al
cd app-agent
%{cargo_install}
pwd
ls -al

 
%files
# %license LICENSE
%{_bindir}/alumet-agent
 
 
%clean
ù{cargo}