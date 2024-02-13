#!/usr/bin/env bash

hooks=(
    "applypatch-msg"
    "commit-msg"
    "fsmonitor-watchman"
    "post-update"
    "pre-applypatch"
    "post-commit"
    # "pre-commit"
    "pre-merge-commit"
    "pre-push"
    "pre-rebase"
    "pre-receive"
    "prepare-commit-msg"
    "push-to-checkout"
    "sendemail-validate"
    "update"
)

cd "$(dirname "$0")"

for hook in "${hooks[@]}"; do
    if ! [ -f ".githooks/$hook" ]; then continue; fi
    if [ -f ".git/hooks/$hook" ]; then
        mv ".git/hooks/$hook" ".git/hooks/$hook.bak"
    fi
    ln -sf ".githooks/$hook" ".git/hooks/$hook"
    # chmod +x ".githooks/$hook"
done

# Check if pre-commit command exists
if ! command -v pre-commit &> /dev/null; then
    read -p "Install pre-commit? 'pip install pre-commit'? (y/n): " install_precommit
    if [ "$install_precommit" == "y" ]; then
        pip install pre-commit
    fi
fi
if ! command -v pre-commit &> /dev/null; then
    pre-commit install
fi
