%global debug_package %{nil}

Name:           alumet
Version:        %{version}
Release:        %{release}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}.tar.gz
BuildArch:      x86_64

Requires: glibc >= 2.2.5
Requires: gcc >= 3.0
Requires: gnu-hash
Requires: rpmlib(CompressedFileNames) <= 3.0.4-1
Requires: rpmlib(FileDigests) <= 4.6.0-1
Requires: rpmlib(PayloadFilesHavePrefix) <= 4.0-1
Requires: rpmlib(PayloadIsXz) <= 5.2-1

%package alumet-local-agent
Summary:        alumet-local-agent package
%description alumet-local-agent
This package contains the alumet app agent.

%package alumet-relay-server
Summary:        alumet-relay-server package
%description alumet-relay-server
This package contains the alumet alumet-relay-server.

%package alumet-relay-client
Summary:        alumet-relay-client package
%description alumet-relay-client
This package contains the alumet alumet-relay-client.
 
%description
Customizable and efficient tool for measuring the energy consumption and performance metrics of software on HPC, Cloud and Edge devices. 
 
%prep
%autosetup -n %{name}

 
%build
mkdir -p %{_builddir}/bin/
cp alumet.sh %{_builddir}/alumet-local-agent
cp alumet.sh %{_builddir}/alumet-relay-server
cp alumet.sh %{_builddir}/alumet-relay-client
cd alumet/app-agent
CARGO_TARGET_DIR=%{_builddir}/bin/ cargo build --release --bin alumet-local-agent --features="local_x86"
CARGO_TARGET_DIR=%{_builddir}/bin/ cargo build --release --bin alumet-relay-server --features="relay_server"
CARGO_TARGET_DIR=%{_builddir}/bin/ cargo build --release --bin alumet-relay-client --features="relay_client"


%install
mkdir -p %{buildroot}%{_exec_prefix}/lib/
mkdir -p %{buildroot}%{_exec_prefix}/bin/
install -D -m 0555 "%{_builddir}/bin/release/alumet-local-agent" "%{buildroot}%{_exec_prefix}/lib/alumet-local-agent_bin"
install -D -m 0555 "%{_builddir}/bin/release/alumet-relay-server" "%{buildroot}%{_exec_prefix}/lib/alumet-relay-server_bin"
install -D -m 0555 "%{_builddir}/bin/release/alumet-relay-client" "%{buildroot}%{_exec_prefix}/lib/alumet-relay-client_bin"
install -D -m 0755 "%{_builddir}/alumet-local-agent" "%{buildroot}%{_exec_prefix}/bin/"
install -D -m 0755 "%{_builddir}/alumet-relay-server" "%{buildroot}%{_exec_prefix}/bin/"
install -D -m 0755 "%{_builddir}/alumet-relay-client" "%{buildroot}%{_exec_prefix}/bin/"
mkdir -p %{buildroot}%{_sharedstatedir}/alumet
chmod 777 %{buildroot}%{_sharedstatedir}/alumet

%files alumet-local-agent
%{_bindir}/alumet-local-agent
%{_exec_prefix}/lib/alumet-local-agent_bin
%dir %{_sharedstatedir}/alumet/

%files alumet-relay-server
%{_bindir}/alumet-relay-server
%{_exec_prefix}/lib/alumet-relay-server_bin
%dir %{_sharedstatedir}/alumet/

%files alumet-relay-client
%{_bindir}/alumet-relay-client
%{_exec_prefix}/lib/alumet-relay-client_bin
%dir %{_sharedstatedir}/alumet/

 
%changelog 
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
