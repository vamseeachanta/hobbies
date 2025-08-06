#!/usr/bin/env python3
"""
Self-contained /create-spec slash command entry point.
Works immediately after git clone with no external dependencies.
"""

import sys
import os
from datetime import datetime
from pathlib import Path

def create_spec_directory(spec_name):
    """Create specification directory structure."""
    today = datetime.now().strftime("%Y-%m-%d")
    spec_folder_name = f"{today}-{spec_name}"
    
    specs_dir = Path(".agent-os/specs")
    specs_dir.mkdir(parents=True, exist_ok=True)
    
    spec_path = specs_dir / spec_folder_name
    spec_path.mkdir(exist_ok=True)
    
    return spec_path

def main():
    """Main create-spec command."""
    if len(sys.argv) < 2:
        print("Usage: python create-spec.py <spec-name>")
        print("Example: python create-spec.py user-authentication")
        return 1
    
    spec_name = sys.argv[1]
    
    try:
        print(f"Creating specification: {spec_name}")
        
        # Create directory structure
        spec_path = create_spec_directory(spec_name)
        print(f"📁 Created: {spec_path}")
        
        # Create basic spec.md
        spec_content = f"""# Spec Requirements Document

> Spec: {spec_name}
> Created: {datetime.now().strftime("%Y-%m-%d")}
> Status: Planning

## Overview

[Brief description of what this spec accomplishes]

## User Stories

### [Story Title]

As a [user type], I want to [action], so that [benefit].

## Spec Scope

1. **[Feature Name]** - [One sentence description]

## Expected Deliverable

1. [Testable outcome]
"""
        
        with open(spec_path / "spec.md", "w") as f:
            f.write(spec_content)
        
        print(f"✅ Specification '{spec_name}' created successfully!")
        print(f"📍 Location: {spec_path}")
        print(f"📄 Main file: {spec_path}/spec.md")
        
        return 0
        
    except Exception as e:
        print(f"❌ Error creating specification: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
