#!/usr/bin/env python3
"""
Unit tests for lowercase function.

This test suite:
- Compiles the project using Make with -DUNIT_TEST flag
- Executes the generated binary
- Validates functional behavior of lowercase conversion
- Generates execution log file
- Uses pytest fixtures and parametrization

Author: Jesús Salvador López Ortega
Course: Fundamentos de Programación
"""

import os
import subprocess
import pytest
from datetime import datetime

SRC_DIR   = os.path.join("..", "src")
BUILD_DIR = os.path.join("..", "build")
BIN_DIR   = os.path.join(BUILD_DIR, "bin")
LOG_DIR   = os.path.join(BUILD_DIR, "log")
LOG_FILE  = os.path.join(LOG_DIR, "test_main.log")

FILENAME = "main"
BIN_PATH = os.path.join(BIN_DIR, FILENAME)


def write_log(message):
    """
    Append a timestamped message to the test log file.

    :param message: Message string to log.
    """
    os.makedirs(LOG_DIR, exist_ok=True)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


def run_cmd(cmd, cwd=None, input_data=None, timeout=5):
    """
    Execute a shell command and capture its result.

    :param cmd: Command list to execute.
    :param cwd: Working directory.
    :param input_data: Optional stdin input.
    :param timeout: Execution timeout in seconds.
    :return: Tuple (returncode, stdout, stderr).
    """
    result = subprocess.run(
        cmd,
        cwd=cwd,
        input=input_data,
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    return result.returncode, result.stdout, result.stderr


@pytest.fixture(scope="session")
def build_project():
    """
    Compile the project once per test session.

    Uses Make with -DUNIT_TEST flag to exclude
    the student main function and enable test harness.

    :return: Path to compiled binary.
    """

    # Reset log file at beginning of session
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)

    write_log("===== TEST SESSION STARTED =====")
    
    cmd = [
        "make",
        "clean",
        "all",
        'CFLAGS=-Wall -O2 -Wno-unused-result -DUNIT_TEST'
    ]

    write_log("Compiling project with UNIT_TEST flag")
    
    code, out, err = run_cmd(cmd, cwd=SRC_DIR)

    write_log(f"Compilation return code: {code}")
    write_log(f"Compiler stdout:\n{out}")
    write_log(f"Compiler stderr:\n{err}")
    
    assert code == 0, (
        "Compilation failed.\n"
        f"Compiler output:\n{err}"
    )

    assert os.path.isfile(BIN_PATH), (
        f"Binary not found at expected location: {BIN_PATH}"
    )

    write_log("Compilation successful")
    write_log("===== EXECUTING TEST CASES =====")
    
    return BIN_PATH


@pytest.mark.parametrize(
    "input_text, expected_output",
    [
        ("HELLO", "hello"),
        ("Hello123", "hello123"),
        ("already", "already"),
        ("PiZzA", "pizza"),
        ("12345", "12345"),
        ("", ""),
    ],
)
def test_lowercase(build_project, input_text, expected_output):
    """
    Validate lowercase conversion behavior.

    The test:
    - Sends input string to program stdin
    - Captures stdout
    - Compares exact output with expected result

    :param build_project: Fixture providing binary path.
    :param input_text: Input string.
    :param expected_output: Expected transformed string.
    """
    
    write_log(f"Running test case: input='{input_text}'")
    
    code, out, err = run_cmd(
        build_project,
        input_data=input_text + "\n",
    )

    write_log(f"Execution return code: {code}")
    write_log(f"Program stdout: '{out.strip()}'")
    write_log(f"Program stderr: '{err.strip()}'")
    
    assert code == 0, (
        "Program execution failed.\n"
        f"stderr:\n{err}"
    )

    result = out.strip()

    if result == expected_output:
        write_log("Result: PASS\n")
    else:
        write_log(
            f"Result: FAIL | Expected: '{expected_output}' | Got: '{result}'\n"
        )
        
    assert result == expected_output, (
        "\nMismatch detected:\n"
        f"Input:    {input_text}\n"
        f"Expected: {expected_output}\n"
        f"Got:      {result}"
    )