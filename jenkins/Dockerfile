FROM jenkins/jenkins:lts-jdk21

USER root

# Cliente de Docker (solo el binario): Jenkins usa el daemon del host a través del socket montado.
COPY --from=docker:cli /usr/local/bin/docker /usr/local/bin/docker

# Plan B: Git confía en la carpeta montada en /repo-local (dueño distinto en Windows).
RUN git config --system --add safe.directory '*'

USER jenkins

# Plugins declarados en plugins.txt (instalados en la imagen, sin asistente).
COPY --chown=jenkins:jenkins plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN jenkins-plugin-cli --plugin-file /usr/share/jenkins/ref/plugins.txt
