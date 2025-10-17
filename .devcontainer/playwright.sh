#!/bin/bash
# This script is executed when the devcontainer is created.
set -e

# Install
# https://blog.jongallant.com/2021/08/playwright-codegen-devcontainer/
export DEBIAN_FRONTEND=noninteractive
sudo apt-get update && \
echo "\n" | sudo npx -q playwright install-deps && \
npx -q playwright install --force --with-deps webkit && \
# sudo npm i -D @playwright/test && \
# sudo npx -q playwright install && \
# sudo npx -q playwright install --force --with-deps --only-shell && \
# sudo npx -q playwright install --force --with-deps && \
# sudo npx -q playwright install --force --with-deps webkit && \
# sudo npx -q playwright install --force --with-deps chromium && \
# sudo npx -q playwright install --force --with-deps chrome && \
# sudo npx -q playwright install --force --with-deps firefox && \
sudo rm -rf /var/lib/apt/lists/*
