# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.166.1/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version: 3, 3.9, 3.8, 3.7, 3.6
ARG VARIANT="3"
FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}
# An ARG declared before a FROM is outside of a build stage,
# so it can't be used in any instruction after a FROM. To use the
# value of an ARG that was defined before the FROM, you need to add the ARG
# again after the FROM
ARG VARIANT
ARG PYTHON_MICRO_VERSION="12"

# Install common software
RUN apt update && apt install -y software-properties-common zip less groff

# Install AWS CLI
RUN curl -s "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && \
	unzip -qq awscliv2.zip && \
	./aws/install && \
	rm -rf aws*

# Install Terraform
RUN curl -fsSL https://apt.releases.hashicorp.com/gpg | apt-key add - && \
	apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main" && \
	apt update && apt install -y terraform

# Install PyEnv
RUN git clone https://github.com/pyenv/pyenv.git /opt/pyenv && \
	cd /opt/pyenv && src/configure && make -C src

ENV PATH "/opt/pyenv/bin/:$PATH"
ENV PYENV_ROOT "/opt/pyenv"

RUN pyenv install ${VARIANT}.${PYTHON_MICRO_VERSION} && \
	pyenv global ${VARIANT}.${PYTHON_MICRO_VERSION} && \
 	chmod -R 777 /opt/pyenv

# Install Poetry
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | \
	POETRY_HOME=/opt/poetry python - && \
	chmod -R 755 /opt/poetry

RUN pip install cleanpy

ENV PATH "/opt/poetry/bin:$PATH"

ENV VIRTUAL_ENV_DISABLE_PROMPT 1

COPY .devcontainer/.bashrc /home/vscode/.bashrc
RUN chown 1000:1000 /home/vscode/.bashrc

RUN poetry config virtualenvs.in-project true
	