# QR Generator

A simple Python script that generates a QR code image from any text or URL.

## Features

- Generates high-error-correction QR codes (still scannable even if partially damaged or obscured)
- Auto-sizes to fit your input data (no manual version tuning)
- Saves output as a PNG image
- Works interactively or via command-line arguments

## Requirements

- Python 3.7+
- [`qrcode`](https://pypi.org/project/qrcode/) with the PIL extra

## Installation

```bash
pip install qrcode[pil]
```

## Usage

### Interactive mode

```bash
python qr_generator.py
```

You'll be prompted for:
1. The URL or text to encode
2. A file name to save the QR code as

### Command-line mode

```bash
python qr_generator.py -d "https://github.com" -o github_qr
```

### Options

| Flag | Description | Default |
|------|-------------|---------|
| `-d`, `--data` | Text or URL to encode | prompts if omitted |
| `-o`, `--output` | Output file name (no extension) | prompts if omitted |
| `--box-size` | Pixel size of each QR box | 12 |
| `--border` | Border thickness in boxes | 4 |

The script saves the result as `<file_name>.png` in the current directory.