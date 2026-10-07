#!/usr/bin/env bash
# ==============================================================================
# Setup Git Hooks for huz4f.com
# Configures core.hooksPath and grants execution permissions to all hooks
# ==============================================================================

set -e

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

git config core.hooksPath .githooks
chmod +x .githooks/*

echo "✔ Git hooks successfully configured to use .githooks/"
echo "  • pre-commit: verifies site before committing"
echo "  • pre-push:   verifies site before pushing to remote"
