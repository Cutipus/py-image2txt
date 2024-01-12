"""Translate image to ASCII"""
from PIL import Image
from sys import argv, stderr

def round_color(color: int):
    if not 0 <= color < 256:
        raise ValueError("Color value must be between 0 and 255")

    if color < 63:
        return 0
    elif color < 190:
        return 127
    else:
        return 255

def pixel_to_str(pixel: tuple[int, int, int, int]):
    rounded_pixel = tuple(map(round_color, pixel))

    match rounded_pixel:
        case 0, 0, 0, _:
            return ' '
        case 0, 0, 127, _:
            return '1'
        case 0, 0, 255, _:
            return ')'
        case 0, 127, 0, _:
            return '!'
        case 0, 127, 127, _:
            return '3'
        case 0, 127, 255, _:
            return '>'
        case 0, 255, 0, _:
            return '|'
        case 0, 255, 127, _:
            return 'x'
        case 0, 255, 255, _:
            return '\\'
        case 127, 0, 0, _:
            return '@'
        case 127, 0, 127, _:
            return '5'
        case 127, 0, 255, _:
            return '$'
        case 127, 127, 0, _:
            return  '['
        case 127, 127, 127, _:
            return  '\u2593'
        case 127, 127, 255, _:
            return  '='
        case 127, 255, 0, _:
            return '#'
        case 127, 255, 127, _:
            return 'L'
        case 127, 255, 255, _:
            return 'J'
        case 255, 0, 0, _:
            return '('
        case 255, 0, 127, _:
            return 'p'
        case 255, 0, 255, _:
            return '&'
        case 255, 127, 0, _:
            return '-'
        case 255, 127, 127, _:
            return 'i'
        case 255, 127, 255, _:
            return 'I'
        case 255, 255, 0, _:
            return '/'
        case 255, 255, 127, _:
            return 'X'
        case 255, 255, 255, _:
            return '@'
        case err:
            print(f"What is {err}?")
            raise ValueError


def main(filename):
    try:
        img = Image.open(filename)
    except (FileNotFoundError, IndexError):
        print("Invalid file.", file=stderr)
        exit()

    pixels = img.load()

    text: str = ""
    for x in range(0, img.size[1],1):
        for y in range(0, img.size[0] ,1):
            text += pixel_to_str(pixels[y,x])
        text += "\n"

    print(text)

if __name__ == '__main__':
    main(argv[1])
