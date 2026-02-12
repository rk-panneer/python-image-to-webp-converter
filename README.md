# 🖼️ Python Image to WebP Converter

A **production-ready Python CLI tool** to batch convert images into **WebP format** with configurable quality, recursive scanning, overwrite control, and dry-run support.

Designed for **web performance optimization, startups, and automation pipelines**.

---

## 🚀 Features

- ✅ Batch convert images to WebP
- 📂 Recursive directory scanning (enabled by default)
- 🎯 Configurable quality (0–100)
- 🔁 Optional overwrite support
- 🧪 Dry-run mode (safe preview)
- 🧠 Automatic image mode handling (RGBA → RGB)
- ⚡ Optimized & lossless WebP options
- 📜 Structured logging (standard & verbose)
- 🖥️ Clean CLI interface

---

## 📦 Supported Input Formats

- `.jpg`
- `.jpeg`
- `.png`
- `.bmp`
- `.tiff`

---

## Prerequisites

- Python 3.6 or higher
- Pillow - Python Imaging Library (`pip install Pillow`)

---

## Installation

1. Clone the repository (or download the script):
   ```bash
   git clone https://github.com/rk-panneer/python-image-to-webp-converter.git
   cd python-image-to-webp-converter
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

Run the script from your terminal. The basic syntax is:

```bash
python python_image_converter.py [directory] [options]
```

### Basic Conversion

Convert all images in the current directory (recursively) with default quality (85):

```bash
python python_image_converter.py
```

### Advanced Examples

#### Convert a specific directory:
```bash
python python_image_converter.py path/to/images
```

#### Set WebP quality:
```bash
python python_image_converter.py --quality 90
```

#### Disable recursive scanning:
```bash
python python_image_converter.py --no-recursive
```

#### Overwrite existing WebP files:
```bash
python python_image_converter.py --force
```

#### Dry run (preview without writing files):
```bash
python python_image_converter.py --dry-run
```

#### Lossless WebP compression:
```bash
python python_image_converter.py --lossless
```

#### Enable verbose logging:
```bash
python python_image_converter.py --verbose
```

---

### 🛠️ Options

| Option | Description |
|--------|-------------|
| `directory` | Directory to scan (default: `.`) |
| `--quality` | Set compression quality (0-100). Default: `85` |
| `--lossless` | Enable lossless compression |
| `--no-recursive` | Disable searching in subdirectories |
| `--force` | Overwrite existing WebP files |
| `--dry-run` | Preview conversion without writing files |
| `--verbose` | Enable debug logging |

---

## Sample Output

```bash
INFO: 🚀 Starting conversion in: .
INFO: 📸 Quality: 85 | Recursive: True
INFO: Force overwrite: False | Dry run: False
INFO: --------------------------------------------------
INFO: ✅ Converted: example.png → example.webp
INFO: ✅ Converted: banner.jpg → banner.webp
INFO: --------------------------------------------------
INFO: 🎉 Process Complete!
INFO: ✅ Converted: 2
INFO: ⏩ Skipped: 0
INFO: ❌ Errors: 0
```

![alt text](<screenshots/original-converted-images-sample.png>)
---

## How It Works

1. The script scans the specified directory (recursively by default) for supported image files (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.tiff`).
2. Each image is converted to WebP format using the **Pillow** library.
3. Converted files are saved in the **same directory** as the source image, with the `.webp` extension.
4. The script handles color mode normalization (e.g., converting RGBA to RGB) to ensure compatibility.
5. It provide a summary of converted, skipped, and failed files upon completion.

---

### 🧠 Use Cases

- Web asset optimization
- Static site generators
- CDN pipelines
- Startup media processing
- CI/CD image optimization

### 🧪 Production Design Notes

- **Safe file handling**: Skips existing files unless `--force` is used.
- **Exit codes**: Returns `1` if any errors occur, useful for CI/CD pipelines.
- **Memory efficient**: Uses context managers to handle image files properly.
- **Structured logging**: Clean feedback for automated environments.

### 👨‍💻 Author

**R. Panneer** - 
Senior Backend / Full-Stack Engineer - 
Python • PHP • Laravel • Systems • AI Integrations

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
