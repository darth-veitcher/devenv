#!/usr/bin/env python
"""Post generation hook for cookiecutter template."""
import os
import subprocess
import sys


def init_git():
    """Initialize git repository if not already initialized."""
    if not os.path.exists('.git'):
        print("Initializing git repository...")
        subprocess.call(['git', 'init'])
        subprocess.call(['git', 'add', '.'])
        subprocess.call(['git', 'commit', '-m', 'Initial commit from cookiecutter template'])
        print("Git repository initialized!")
    else:
        print("Git repository already exists, skipping initialization.")


def main():
    """Main entry point for post generation hook."""
    print("\n🎉 Project '{{ cookiecutter.project_name }}' created successfully!")
    print("\nPost-generation tasks:")
    
    # Initialize git repository
    init_git()
    
    # Print next steps
    print("\n📋 Next steps:")
    print("1. cd {{ cookiecutter.project_slug }}")
    print("2. Open in VS Code: code .")
    print("3. Reopen in Dev Container when prompted")
    print("4. Start coding! 🚀")
    
    if "{{ cookiecutter.use_claude_ai }}" == "yes":
        print("\n🤖 Claude AI is configured and ready to assist you!")
    
    print("\nFor more information, see the README.md file.")


if __name__ == "__main__":
    main()