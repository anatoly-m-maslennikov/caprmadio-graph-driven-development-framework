FROM node:22.20.0-bookworm-slim AS codex
ARG CODEX_VERSION=0.156.1
RUN npm install --global @openai/codex@${CODEX_VERSION}

FROM python:3.14.7-slim@sha256:51dafde81dbdb6ebde285137a295cf18a47ca95234fe388a343719cb97305b3d
ARG RUNTIME_UID=1000
ARG RUNTIME_GID=1000
RUN apt-get update && apt-get install -y --no-install-recommends git ca-certificates \
    && rm -rf /var/lib/apt/lists/* \
    && (getent group ${RUNTIME_GID} || groupadd -g ${RUNTIME_GID} caprmedio) \
    && useradd -u ${RUNTIME_UID} -g ${RUNTIME_GID} -m -d /home/caprmedio caprmedio
RUN python -m pip install --no-cache-dir uv==0.12.18
COPY --from=codex /usr/local/bin/node /usr/local/bin/node
COPY --from=codex /usr/local/lib/node_modules /usr/local/lib/node_modules
RUN ln -s /usr/local/lib/node_modules/@openai/codex/bin/codex.js /usr/local/bin/codex
WORKDIR /workspace
COPY pyproject.toml uv.lock ./
ENV UV_PROJECT_ENVIRONMENT=/opt/venv UV_CACHE_DIR=/tmp/uv-cache
RUN uv sync --locked --no-dev --group rmed-workflow-mcp --group workflow-orchestrator \
    --group validate-atoms --group validate-atoms-dev
COPY 102_FRAMEWORK_ENGINE ./102_FRAMEWORK_ENGINE
RUN mkdir -p /home/caprmedio/.codex /workspace/.caprmedio_install \
    /workspace/.caprmedio_tmp /workspace/tmp /workspace/.caprmedio_caprmedio \
    && chown -R ${RUNTIME_UID}:${RUNTIME_GID} /home/caprmedio
ENV PATH=/opt/venv/bin:/usr/local/bin:/usr/bin:/bin PYTHONDONTWRITEBYTECODE=1
USER caprmedio
ENTRYPOINT ["python", "102_FRAMEWORK_ENGINE/201_PROGRAMMATIC/203_APPS/WORKFLOW_ORCHESTRATOR/docker/entrypoint.py"]
