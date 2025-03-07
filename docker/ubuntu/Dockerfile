ARG BASE_IMAGE=ubuntu:25.04

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

FROM $BASE_IMAGE AS runtime

# ARTIFACT_DIR is the dir that contains $ARTIFACT_FILE
ARG ARTIFACT_DIR=build/deps-artifacts
# ARTIFACT_FILE is the deb filename
ARG ARTIFACT_FILE=alumet_0.8-1_amd64_ubuntu_25.04.deb

COPY $ARTIFACT_DIR/$ARTIFACT_FILE /tmp/
RUN apt update -y && apt install -y libcap2-bin openssl
RUN dpkg -i /tmp/$ARTIFACT_FILE && rm -f /tmp/$ARTIFACT_FILE

# alumet-agent is packaged in /usr/lib in deb package but can be called directly here
RUN rm /usr/bin/alumet-agent && mv /usr/lib/alumet-agent /usr/bin/alumet-agent

# set up user and permissions
RUN groupadd -r alumet && \
    useradd -r -g alumet alumet && \
    mkdir /app && \
    chown alumet:alumet /usr/bin/alumet-agent /etc/alumet/alumet-config.toml /app

USER alumet
WORKDIR /app

ENTRYPOINT ["/usr/bin/alumet-agent"]
CMD ["--config", "/etc/alumet/alumet-config.toml", "--plugins", "csv,perf,procfs,socket-control", "--output-file", "/app/alumet-output.csv"]
