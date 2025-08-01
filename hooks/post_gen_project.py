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


def init_submodules():
    """Initialize git submodules for MCP servers."""
    print("\nInitializing MCP server submodules...")
    
    # Add memgraph-ai-toolkit submodule
    memgraph_path = '.devcontainer/mcp/memgraph-ai-toolkit'
    if not os.path.exists(memgraph_path):
        print("Adding memgraph-ai-toolkit submodule...")
        subprocess.call(['git', 'submodule', 'add', 'https://github.com/memgraph/ai-toolkit.git', memgraph_path])
        subprocess.call(['git', 'submodule', 'update', '--init', '--recursive'])
        print("Memgraph AI Toolkit submodule added!")
    else:
        print("Memgraph AI Toolkit submodule already exists.")
    
    # Commit the submodule addition
    subprocess.call(['git', 'add', '.gitmodules', memgraph_path])
    subprocess.call(['git', 'commit', '-m', 'Add memgraph-ai-toolkit submodule'])


def main():
    """Main entry point for post generation hook."""
    print("\n🎉 Project '{{ cookiecutter.project_name }}' created successfully!")
    print("\nPost-generation tasks:")
    
    # Initialize git repository
    init_git()
    
    # Initialize submodules
    init_submodules()
    
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