import os
import pytest
import subprocess
from datetime import datetime


SRC_DIR   = os.path.join("..", "src")
BUILD_DIR = os.path.join("..", "build")
INPUT_DIR = os.path.join("..", "inputs")

LOG_DIR   = os.path.join(BUILD_DIR, "log")
LOG_FILE  = os.path.join(LOG_DIR, "test_main.log")

OUT_DIR   = os.path.join(BUILD_DIR, "out")

FILENAME = "main"
BIN_PATH = os.path.join(BUILD_DIR, "bin", FILENAME)

EXPECTED_HEX = (
    "20202020202a20202020200a"
    "202020202a2a2a202020200a"
    "2020202a2a2a2a2a2020200a"
    "20202a2a2a2a2a2a2a20200a"
    "202a2a2a2a2a2a2a2a2a200a"
    "2a2a2a2a2a2a2a2a2a2a2a0a"
)

def write_log(message):
    os.makedirs(LOG_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")


@pytest.fixture(scope="session", autouse=True)
def build_and_run():
    """Ejecuta make clean all run antes de los tests"""
    try:
        # Ejecutamos make en el directorio de build
        subprocess.run(
            ["make", "clean", "all", "run"],
            cwd=SRC_DIR,
            check=True,
            capture_output=True,
            text=True
        )
        write_log("Make PASS: clean all run")
    except subprocess.CalledProcessError as e:
        write_log(f"Make FAIL: {e.stderr}")
        pytest.fail(f"Make failed:\n{e.stderr}")


@pytest.fixture(scope="session")
def expected_contents():
    """Generates expected pyramid.txt"""

    expected_bytes = bytes.fromhex(EXPECTED_HEX)

    return {
        "pyramid.txt": expected_bytes
    }


@pytest.mark.parametrize(
    "fname",
    ["pyramid.txt"]
)
def test_generated_files(expected_contents, fname):
    """Compara los archivos generados en C con los esperados en Python"""
    out_path = os.path.join(OUT_DIR, fname)
    assert os.path.isfile(out_path), f"Archivo no generado: {out_path}"

    with open(out_path, "rb") as f:
        result = f.read()

    expected = expected_contents[fname]

    if result == expected:
        write_log(f"PASS: {fname}")
    else:
        write_log(
            f"FAIL: {fname} | Expected vs Got differ\n"
            f"--- Expected (str) ---\n{expected.decode('utf-8')}\n"
            f"--- Got (str) ---\n{result.decode('utf-8')}\n"
        )

    assert result == expected, (
        f"\nMismatch in {fname}:\n"
        f"--- Expected (str) ---\n{expected.decode('utf-8')}\n"
        f"--- Got (str) ---\n{result.decode('utf-8')}\n"
    )