# Prerequisites

Before using devenv, ensure you have the following tools installed.

## Required Tools

### 1. Python 3.12+

devenv generates Python 3.12+ projects by default.

=== "macOS (Homebrew)"

    ```bash
    brew install python@3.12
    ```

=== "Ubuntu/Debian"

    ```bash
    sudo apt update
    sudo apt install python3.12 python3.12-venv
    ```

=== "Windows"

    Download from [python.org](https://www.python.org/downloads/)

### 2. Cookiecutter

The template engine that generates your project.

```bash
pip install cookiecutter
# or
pipx install cookiecutter
```

### 3. uv (Recommended)

Fast, reliable Python package manager used in generated projects.

=== "macOS/Linux"

    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows"

    ```powershell
    powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
    ```

=== "pipx"

    ```bash
    pipx install uv
    ```

### 4. Docker (Optional but Recommended)

Required for Dev Containers and containerized development.

=== "macOS"

    ```bash
    brew install --cask docker
    ```

=== "Linux"

    Follow [Docker's official installation guide](https://docs.docker.com/engine/install/)

=== "Windows"

    Download [Docker Desktop](https://www.docker.com/products/docker-desktop/)

### 5. just (Optional)

A command runner used in generated projects. Not required but recommended.

=== "macOS"

    ```bash
    brew install just
    ```

=== "Linux"

    ```bash
    curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
    ```

=== "Windows"

    ```powershell
    winget install Casey.Just
    ```

## Optional Tools

### VS Code

For the best Dev Container experience:

- [Visual Studio Code](https://code.visualstudio.com/)
- [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)

### Git

For version control (you probably already have this):

```bash
git --version
```

## Verify Installation

Run these commands to verify everything is installed:

```bash
# Python
python3 --version  # Should be 3.12+

# Cookiecutter
cookiecutter --version

# uv
uv --version

# Docker (optional)
docker --version

# just (optional)
just --version
```

## Troubleshooting

### Python not found

Ensure Python is in your PATH:

```bash
which python3
# or on Windows
where python
```

### Cookiecutter fails to install

Try using pipx for isolated installation:

```bash
pip install pipx
pipx install cookiecutter
```

### Docker permission denied

Add your user to the docker group (Linux):

```bash
sudo usermod -aG docker $USER
# Log out and back in
```

## Next Steps

Once prerequisites are installed, proceed to:

[:octicons-arrow-right-24: Quickstart](quickstart.md)
