import os
import sys
import argparse
import logging
from PIL import Image

SUPPORTED_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.bmp', '.tiff')

def setup_logger(verbose: bool):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(level=level, format="%(levelname)s: %(message)s")

def convert_images_to_webp(root_dir: str, quality: int, recursive: bool, force: bool, dry_run: bool, lossless: bool):
    converted = skipped = failed = 0

    logging.info(f"🚀 Starting conversion in: {root_dir}")
    logging.info(f"📸 Quality: {quality} | Recursive: {recursive}")
    logging.info(f"Force overwrite: {force} | Dry run: {dry_run}")
    logging.info("-" * 50)

    for dirpath, _, filenames in os.walk(root_dir):
        if not recursive and dirpath != root_dir:
            continue

        for filename in filenames:
            if not filename.lower().endswith(SUPPORTED_EXTENSIONS):
                continue

            src_path = os.path.join(dirpath, filename)
            dst_path = os.path.splitext(src_path)[0] + ".webp"

            if os.path.exists(dst_path) and not force:
                skipped += 1
                logging.debug(f"⏩ Skipped (exists): {dst_path}")
                continue

            try:
                if dry_run:
                    logging.info(f"[DRY-RUN] Would convert: {src_path}")
                    converted += 1
                    continue

                with Image.open(src_path) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")

                    img.save(dst_path, "WEBP", quality=quality, lossless=lossless, optimize=True)

                logging.info(f"✅ Converted: {filename} → {os.path.basename(dst_path)}")
                converted += 1

            except Exception as exc:
                failed += 1
                logging.error(f"❌ Failed: {filename} ({exc})")

    logging.info("-" * 50)
    logging.info(f"🎉 Process Complete!")
    logging.info(f"✅ Converted: {converted}")
    logging.info(f"⏩ Skipped: {skipped}")
    logging.info(f"❌ Errors: {failed}")

    return failed


def main():
    parser = argparse.ArgumentParser(
        description="Batch convert images to WebP format"
    )
    parser.add_argument(
        "directory",
        nargs="?",
        default=".",
        help="Directory to scan (default: current directory)"
    )
    parser.add_argument(
        "--quality",
        type=int,
        default=85,
        help="WebP quality (0-100)"
    )
    parser.add_argument(
        "--no-recursive",
        action="store_true",
        help="Disable recursive directory scanning"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing WebP files"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview conversion without writing files"
    )
    parser.add_argument(
        "--lossless",
        action="store_true",
        help="Use lossless WebP compression"
    )
    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable debug logging"
    )

    args = parser.parse_args()
    setup_logger(args.verbose)

    try:
        import PIL  # noqa
    except ImportError:
        logging.error("Pillow is not installed. Run: pip install Pillow")
        sys.exit(1)

    if not os.path.isdir(args.directory):
        logging.error(f"Directory not found: {args.directory}")
        sys.exit(1)

    failures = convert_images_to_webp(
        root_dir=args.directory,
        quality=args.quality,
        recursive=not args.no_recursive,
        force=args.force,
        dry_run=args.dry_run,
        lossless=args.lossless
    )

    sys.exit(1 if failures else 0)


if __name__ == "__main__":
    main()
