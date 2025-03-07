ARG BUILDER_IMAGE=redhat/ubi8:8.10
ARG BASE_IMAGE=redhat/ubi8-micro:8.10

# TODO
# LABEL org.opencontainers.image.created="The date and time on which the image was built (string, RFC 3339 date-time)." /
# 	org.opencontainers.image.authors="Contact details of the people or organization responsible for the image (freeform string)." /
# 	org.opencontainers.image.url="URL to find more information on the image (string)." /
# 	org.opencontainers.image.documentation="URL to get documentation on the image (string)." /
# 	org.opencontainers.image.source="URL to the source code for building the image (string)." /
# 	org.opencontainers.image.version="Version of the packaged software (string)." /
# 	org.opencontainers.image.revision="Source control revision identifier for the image (string)." /
# 	org.opencontainers.image.vendor="Name of the distributing entity, organization, or individual (string)." /
# 	org.opencontainers.image.licenses="License(s) under which contained software is distributed (string, SPDX License List)." /
# 	org.opencontainers.image.ref.name="Name of the reference for a target (string)." /
# 	org.opencontainers.image.title="Human-readable title of the image (string)." /
# 	org.opencontainers.image.description="Human-readable description of the software packaged in the image (string)."

FROM $BUILDER_IMAGE AS builder

# ARTIFACT_DIR is the dir that contains $ARTIFACT_FILE
ARG ARTIFACT_DIR=build/deps-artifacts
# ARTIFACT_FILE is the rpm filename
ARG ARTIFACT_FILE=alumet-agent-0.8.0-1.ubi.8.3.x86_64.rpm

COPY ${ARTIFACT_DIR}/${ARTIFACT_FILE} /tmp/
RUN rpm -i /tmp/$ARTIFACT_FILE && rm -f /tmp/$ARTIFACT_FILE

FROM $BASE_IMAGE AS runtime

# alumet-agent is packaged in /usr/lib in RPM package but can be called directly here
COPY --from=builder /usr/lib/alumet-agent /usr/bin/alumet-agent
COPY --from=builder /etc/alumet/alumet-config.toml /etc/alumet/alumet-config.toml

# shadow-utils for groupadd and useradd - util-linux for lscpu
RUN microdnf install -y shadow-utils util-linux && \
    microdnf clean all

# set up user and permissions
RUN groupadd -r alumet && \
    useradd -r -g alumet alumet && \
    mkdir /app && \
    chown alumet:alumet /usr/bin/alumet-agent /etc/alumet/alumet-config.toml /app

# NOTE: Workaround for ubi-8.3 that need to have libcap updated... Can be removed for ubi-8.10
# needed capability for rapl plugin - TODO make it optional
RUN microdnf update libcap && \
    setcap cap_perfmon=ep /usr/bin/alumet-agent

USER alumet
WORKDIR /app

ENTRYPOINT ["/usr/bin/alumet-agent"]
CMD ["--config", "/etc/alumet/alumet-config.toml", "--plugins", "csv,perf,procfs,socket-control", "--output-file", "/app/alumet-output.csv"]
