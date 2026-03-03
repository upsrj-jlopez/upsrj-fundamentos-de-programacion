import os
import pytest
from datetime import datetime

SRC_DIR   = os.path.join("..", "src")
BUILD_DIR = os.path.join("..", "build")
INPUT_DIR = os.path.join("..", "inputs")

LOG_DIR   = os.path.join(BUILD_DIR, "log")
LOG_FILE  = os.path.join(LOG_DIR, "test_main.log")

FILENAME = "main"
BIN_PATH = os.path.join(BUILD_DIR, "bin", FILENAME)

def c_capitalize(text: str) -> str:
    text = text.lower()
    result = []
    capitalize = True
    for ch in text:
        if ch in [' ', '\n', '\t']:
            capitalize = True
            result.append(ch)
        else:
            if capitalize and 'a' <= ch <= 'z':
                result.append(chr(ord(ch) - (ord('a') - ord('A'))))
            else:
                result.append(ch)
            capitalize = False
    return "".join(result)

def write_log(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

@pytest.fixture(scope="session")
def expected_contents():
    """Genera los contenidos esperados a partir de lorem.txt"""
    path = os.path.join(INPUT_DIR, "lorem.txt")
    with open(path, "r", encoding="utf-8") as f:
        base_text = f.read()

    return {
        "upper.txt": base_text.upper(),
        "lower.txt": base_text.lower(),
        "capitalize.txt": c_capitalize(base_text),
    }

@pytest.mark.parametrize(
    "fname",
    ["upper.txt", "lower.txt", "capitalize.txt"]
)
def test_generated_files(expected_contents, fname):
    """Compara los archivos generados en C con los esperados en Python"""
    out_path = os.path.join(INPUT_DIR, fname)
    assert os.path.isfile(out_path), f"Archivo no generado: {out_path}"

    with open(out_path, "r", encoding="utf-8") as f:
        result = f.read()

    expected = expected_contents[fname]

    if result == expected:
        write_log(f"PASS: {fname}")
    else:
        write_log(f"FAIL: {fname} | Expected vs Got differ")

    assert result == expected, (
        f"\nMismatch in {fname}:\n"
        f"Expected:\n{expected[:200]}...\n"
        f"Got:\n{result[:200]}..."
    )