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

HEADER_SIZE = 54
PIXEL_SIZE = 3


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
    """Generates expected grayscale BMP from lena.bmp"""

    path = os.path.join(INPUT_DIR, "lena.bmp")

    with open(path, "rb") as f:
        data = f.read()

    header = data[:HEADER_SIZE]
    pixels = data[HEADER_SIZE:]

    result = bytearray()

    # Process pixels in groups of 3 (BGR)
    for i in range(0, len(pixels), PIXEL_SIZE):
        if i + 2 >= len(pixels):
            break

        blue  = pixels[i]
        green = pixels[i + 1]
        red   = pixels[i + 2]

        gray = (blue + green + red) // 3

        result.extend([gray, gray, gray])

    return {
        "lena.bmp": header + bytes(result)
    }


@pytest.mark.parametrize(
    "fname",
    ["lena.bmp"]
)
def test_header_preserved(expected_contents, fname):
    """Valida que el header del BMP no sea modificado"""
    
    in_path = os.path.join(INPUT_DIR, fname)
    out_path = os.path.join(OUT_DIR, fname)

    assert os.path.isfile(out_path), f"Archivo no generado: {out_path}"

    with open(in_path, "rb") as f:
        original = f.read(HEADER_SIZE)

    with open(out_path, "rb") as f:
        result = f.read(HEADER_SIZE)

    if result == original:
        write_log(f"PASS: HEADER {fname}")
    else:
        write_log(f"FAIL: HEADER {fname} | Header was modified")

    assert result == original, (
        f"\nHeader mismatch in {fname}\n"
    )


@pytest.mark.parametrize(
    "fname",
    ["lena.bmp"]
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
        write_log(f"FAIL: {fname} | Expected vs Got differ")

    assert result == expected, (
        f"\nMismatch in {fname}:\n"
    )