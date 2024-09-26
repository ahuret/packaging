Name:           alumet
Version:        %{version}
Release:        %{release}
Summary:        A tool for measuring the energy consumption and performance metrics
License:        EUPL
Url:            https://github.com/alumet-dev/alumet
Source:         %{name}.tar.gz
BuildArch:      x86_64

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
mkdir -p %{buildroot}%{_bindir}/alumet/
install -D -m 0755 "%{_builddir}/alumet-local-agent" "%{buildroot}%{_bindir}/"
install -D -m 0755 "%{_builddir}/alumet-relay-server" "%{buildroot}%{_bindir}/"
install -D -m 0755 "%{_builddir}/alumet-relay-client" "%{buildroot}%{_bindir}/"
install -D -m 0755 "%{_builddir}/bin/release/alumet-local-agent" "%{buildroot}%{_bindir}/alumet/alumet-local-agent"
install -D -m 0755 "%{_builddir}/bin/release/alumet-relay-client" "%{buildroot}%{_bindir}/alumet/alumet-relay-client"
install -D -m 0755 "%{_builddir}/bin/release/alumet-relay-server" "%{buildroot}%{_bindir}/alumet/alumet-relay-server"
mkdir -p %{buildroot}%{_sysconfdir}/alumet
chmod 777 %{buildroot}%{_sysconfdir}/alumet



%files alumet-local-agent
%{_bindir}/alumet/alumet-local-agent
%{_bindir}/alumet-local-agent
%dir %{_sysconfdir}/alumet/

%files alumet-relay-server
%{_bindir}/alumet/alumet-relay-server
%{_bindir}/alumet-relay-server
%dir %{_sysconfdir}/alumet/

%files alumet-relay-client
%{_bindir}/alumet/alumet-relay-client
%{_bindir}/alumet-relay-client
%dir %{_sysconfdir}/alumet/

 
%changelog 
* Wed Sep 18 2024 Cyprien cyprien.pelisse-verdoux@eviden.com - 0.0.1
- Initial package
