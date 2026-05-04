#!/bin/bash
cd ~/my_own_collection/ansible
source venv/bin/activate
source hacking/env-setup 2>/dev/null || echo "Using pip-installed Ansible"
echo "=== Ansible Development Environment ==="
ansible --version | head -3
echo ""
echo "To deactivate: deactivate"
