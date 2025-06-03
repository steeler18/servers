# syntax=docker/dockerfile:1
FROM mcr.microsoft.com/devcontainers/universal:2

# Install uv (includes uvx)
RUN curl -Ls https://astral.sh/uv/install.sh | sh

# [Optional] Add uv to PATH if needed (default install is ~/.cargo/bin)
ENV PATH="/root/.cargo/bin:${PATH}"

# ...existing code...
