#!/usr/bin/env bash
# Configure repository git hooks
git config core.hooksPath .githooks
chmod +x .githooks/*
echo "✔ Git hooks successfully configured to use .githooks/"
