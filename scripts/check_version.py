#!/usr/bin/env python3
"""
Helper script to check and update the version number in pyproject.toml.
Run this before publishing a new version to PyPI.
"""

import re
import sys
import os
from pathlib import Path

def get_current_version(init_file):
    """Extract version string from __init__.py"""
    with open(init_file, 'r') as f:
        content = f.read()
    
    # Find version with regex
    match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)['\"]", content)
    if match:
        return match.group(1)
    else:
        print(f"ERROR: Could not find version in {init_file}")
        return None

def get_toml_version(toml_file):
    """Extract version from pyproject.toml"""
    if not os.path.exists(toml_file):
        print(f"ERROR: {toml_file} does not exist")
        return None
    
    with open(toml_file, 'r') as f:
        content = f.read()
    
    # Find version with regex
    match = re.search(r"version\s*=\s*['\"]([^'\"]+)['\"]", content)
    if match:
        return match.group(1)
    else:
        print(f"ERROR: Could not find version in {toml_file}")
        return None

def update_pyproject_toml(toml_file, version):
    """Update version in pyproject.toml"""
    if not os.path.exists(toml_file):
        print(f"ERROR: {toml_file} does not exist")
        return False
    
    with open(toml_file, 'r') as f:
        content = f.read()
    
    # Update version
    new_content = re.sub(
        r"(version\s*=\s*['\"])[^'\"]+(['\"])", 
        r"\g<1>" + version + r"\g<2>", 
        content
    )
    
    with open(toml_file, 'w') as f:
        f.write(new_content)
    
    return True

def prompt_new_version(current_version):
    """Prompt for a new version number"""
    parts = current_version.split('.')
    if len(parts) == 3:
        # Suggest a patch version bump
        patch = int(parts[2]) + 1
        suggestion = f"{parts[0]}.{parts[1]}.{patch}"
    else:
        suggestion = f"{current_version}.1"
    
    print(f"Current version: {current_version}")
    print(f"Suggested new version: {suggestion}")
    
    user_input = input(f"Enter new version [press Enter to use {suggestion}]: ")
    return user_input.strip() if user_input.strip() else suggestion

def main():
    # Get project root directory
    project_root = Path(__file__).parent.parent
    
    # Check for pyproject.toml
    toml_file = project_root / "pyproject.toml"
    if not toml_file.exists():
        print(f"ERROR: Could not find {toml_file}")
        sys.exit(1)
    
    current_version = get_toml_version(toml_file)
    if not current_version:
        sys.exit(1)
    
    # Check for version in __init__.py
    init_file = project_root / "mqtt_docker_controller" / "__init__.py"
    if init_file.exists():
        init_version = get_current_version(init_file)
        if init_version and init_version != current_version:
            print(f"WARNING: Version mismatch between pyproject.toml ({current_version}) and __init__.py ({init_version})")
    
    # Prompt for version update
    new_version = prompt_new_version(current_version)
    
    if new_version != current_version:
        print(f"Updating version from {current_version} to {new_version}...")
        update_pyproject_toml(toml_file, new_version)
        print(f"Updated version in {toml_file}")
        
        # Also update __init__.py if it exists
        if init_file.exists() and '__version__' in open(init_file).read():
            with open(init_file, 'r') as f:
                content = f.read()
            
            new_content = re.sub(
                r"(__version__\s*=\s*['\"])[^'\"]+(['\"])", 
                r"\g<1>" + new_version + r"\g<2>", 
                content
            )
            
            with open(init_file, 'w') as f:
                f.write(new_content)
            
            print(f"Updated version in {init_file}")
    else:
        print(f"Keeping current version: {current_version}")
    
    print("Version check complete.")
    return 0

if __name__ == "__main__":
    sys.exit(main())