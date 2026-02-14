import sys
import os
from PIL import Image, ImageOps


def main():
    # 1) Check number of command-line arguments
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    # 2) Validate extensions (case-insensitive)
    allowed = {".jpg", ".jpeg", ".png"}

    in_ext = os.path.splitext(input_path)[1].lower()
    out_ext = os.path.splitext(output_path)[1].lower()

    if in_ext not in allowed:
        sys.exit("Invalid input")
    if out_ext not in allowed:
        sys.exit("Invalid output")
    if in_ext != out_ext:
        sys.exit("Input and output have different extensions")

    # 3) Open input image (handle missing file)
    try:
        photo = Image.open(input_path)
    except FileNotFoundError:
        sys.exit("Input does not exist")

    # 4) Open shirt, fit photo to shirt size, overlay, save
    shirt = Image.open("shirt.png")
    size = shirt.size

    photo = ImageOps.fit(photo, size)  # default method/bleed/centering
    photo.paste(shirt, (0, 0), shirt)  # use shirt as mask for transparency
    photo.save(output_path)


if __name__ == "__main__":
    main()
