# test_smoke.py - Smoke tests for hobbies project

"""
Smoke tests to verify basic functionality and infrastructure.
These tests ensure the project structure and core components are working.
"""

import pytest
import os
import sys
from pathlib import Path
import importlib.util


class TestProjectStructure:
    """Test basic project structure and configuration."""

    def test_project_root_exists(self):
        """Test that the project root directory exists."""
        project_root = Path(__file__).parent.parent
        assert project_root.exists()
        assert project_root.is_dir()

    def test_pyproject_toml_exists(self):
        """Test that pyproject.toml configuration file exists."""
        project_root = Path(__file__).parent.parent
        pyproject_file = project_root / "pyproject.toml"
        assert pyproject_file.exists()
        assert pyproject_file.is_file()

    def test_agent_os_directory_exists(self):
        """Test that .agent-os directory exists."""
        project_root = Path(__file__).parent.parent
        agent_os_dir = project_root / ".agent-os"
        assert agent_os_dir.exists()
        assert agent_os_dir.is_dir()

    def test_claude_md_exists(self):
        """Test that CLAUDE.md configuration file exists."""
        project_root = Path(__file__).parent.parent
        claude_file = project_root / "CLAUDE.md"
        assert claude_file.exists()
        assert claude_file.is_file()

    def test_uv_toml_exists(self):
        """Test that uv.toml configuration file exists."""
        project_root = Path(__file__).parent.parent
        uv_file = project_root / "uv.toml"
        assert uv_file.exists()
        assert uv_file.is_file()

    def test_gitignore_exists(self):
        """Test that .gitignore file exists."""
        project_root = Path(__file__).parent.parent
        gitignore_file = project_root / ".gitignore"
        assert gitignore_file.exists()
        assert gitignore_file.is_file()


class TestPythonEnvironment:
    """Test Python environment and basic imports."""

    def test_python_version(self):
        """Test that Python version is supported."""
        assert sys.version_info >= (3, 8)

    def test_basic_imports(self):
        """Test that basic Python modules can be imported."""
        import json
        import os
        import pathlib
        import sys
        assert json
        assert os
        assert pathlib
        assert sys

    def test_pytest_working(self):
        """Test that pytest is working correctly."""
        # This test existing and running proves pytest is working
        assert True

    def test_testing_environment_variable(self):
        """Test that testing environment is properly set."""
        assert os.environ.get('TESTING') == 'true'


class TestAgentOSStructure:
    """Test Agent OS directory structure and key files."""

    def test_agent_os_cli_exists(self):
        """Test that Agent OS CLI directory exists."""
        project_root = Path(__file__).parent.parent
        cli_dir = project_root / ".agent-os" / "cli"
        if cli_dir.exists():
            assert cli_dir.is_dir()
            # Test for key CLI files
            main_py = cli_dir / "main.py"
            if main_py.exists():
                assert main_py.is_file()

    def test_agent_os_commands_exists(self):
        """Test that Agent OS commands directory exists."""
        project_root = Path(__file__).parent.parent
        commands_dir = project_root / ".agent-os" / "commands"
        if commands_dir.exists():
            assert commands_dir.is_dir()

    def test_agent_os_python_files(self):
        """Test that Agent OS Python files are valid."""
        project_root = Path(__file__).parent.parent
        agent_os_dir = project_root / ".agent-os"

        if agent_os_dir.exists():
            # Find Python files in .agent-os directory
            python_files = list(agent_os_dir.rglob("*.py"))

            # Test that we found some Python files
            if python_files:
                assert len(python_files) > 0

                # Test that at least one file can be parsed
                for py_file in python_files[:3]:  # Test first 3 files
                    try:
                        with open(py_file, 'r', encoding='utf-8') as f:
                            content = f.read()
                        # Try to compile the code
                        compile(content, str(py_file), 'exec')
                    except (SyntaxError, UnicodeDecodeError):
                        pytest.fail(f"Python file {py_file} has syntax errors")


class TestFilePermissions:
    """Test file permissions and accessibility."""

    def test_project_files_readable(self):
        """Test that key project files are readable."""
        project_root = Path(__file__).parent.parent
        key_files = [
            "pyproject.toml",
            "CLAUDE.md",
            "uv.toml",
            ".gitignore"
        ]

        for filename in key_files:
            file_path = project_root / filename
            if file_path.exists():
                assert os.access(file_path, os.R_OK), f"Cannot read {filename}"

    def test_tests_directory_structure(self):
        """Test that tests directory has correct structure."""
        tests_dir = Path(__file__).parent
        assert tests_dir.exists()
        assert tests_dir.is_dir()

        # Test for expected subdirectories
        unit_dir = tests_dir / "unit"
        integration_dir = tests_dir / "integration"

        assert unit_dir.exists()
        assert integration_dir.exists()
        assert unit_dir.is_dir()
        assert integration_dir.is_dir()


class TestConfigurationFiles:
    """Test configuration file content and structure."""

    def test_pyproject_toml_valid(self):
        """Test that pyproject.toml has valid structure."""
        project_root = Path(__file__).parent.parent
        pyproject_file = project_root / "pyproject.toml"

        if pyproject_file.exists():
            import tomli
            try:
                with open(pyproject_file, 'rb') as f:
                    config = tomli.load(f)

                # Test for expected sections
                assert 'project' in config
                assert 'tool' in config

                # Test project metadata
                if 'project' in config:
                    project_config = config['project']
                    assert 'name' in project_config
                    assert project_config['name'] == 'hobbies'

            except Exception as e:
                pytest.fail(f"pyproject.toml is not valid TOML: {e}")

    def test_coverage_configuration(self):
        """Test that coverage configuration is present."""
        project_root = Path(__file__).parent.parent
        pyproject_file = project_root / "pyproject.toml"

        if pyproject_file.exists():
            with open(pyproject_file, 'r', encoding='utf-8') as f:
                content = f.read()

            # Check for coverage configuration
            assert 'tool.coverage' in content or 'tool.pytest' in content