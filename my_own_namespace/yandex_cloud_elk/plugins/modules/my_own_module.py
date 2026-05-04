#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2025, Your Name
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module
short_description: Creates a text file on a remote host
version_added: "1.0.0"
description:
  - This module creates a text file on a remote host with specified content.
options:
  path:
    description:
      - Path to the file to be created on the remote host.
    required: true
    type: str
  content:
    description:
      - Content to write to the file.
    required: true
    type: str
author:
  - Your Name (@yourGitHubHandle)
'''

EXAMPLES = r'''
- name: Create a file with content
  my_own_module:
    path: /tmp/test_file.txt
    content: "Hello, Ansible!"
'''

RETURN = r'''
path:
  description: Path to the created/modified file
  type: str
  returned: always
  sample: "/tmp/test_file.txt"
content:
  description: Content written to the file
  type: str
  returned: always
  sample: "Hello, Ansible!"
changed:
  description: Whether the file was created or modified
  type: bool
  returned: always
'''

import os

from ansible.module_utils.basic import AnsibleModule

def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )

    result = dict(
        changed=False,
        path='',
        content=''
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    path = module.params['path']
    content = module.params['content']
    result['path'] = path
    result['content'] = content

    # Check if file exists and content matches
    file_exists = os.path.exists(path)
    file_content_matches = False

    if file_exists:
        with open(path, 'r') as f:
            existing_content = f.read()
            if existing_content == content:
                file_content_matches = True

    if module.check_mode:
        if not file_exists or not file_content_matches:
            result['changed'] = True
        module.exit_json(**result)

    # Write or update the file
    if not file_exists or not file_content_matches:
        try:
            with open(path, 'w') as f:
                f.write(content)
            result['changed'] = True
            module.exit_json(**result)
        except Exception as e:
            module.fail_json(msg=f"Error writing to file {path}: {str(e)}", **result)
    else:
        module.exit_json(**result)

def main():
    run_module()

if __name__ == '__main__':
    main()
