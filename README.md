# image2txt - a silly image-to-ASCII converter written in Python

To use, simply execute `python img2txt example.png`.

## Dependencies
- Python 3.12+
- Pillow (`pip install pillow`)

## Tips
- To save the ASCII result, simply redirect it to a file using your terminal `python img2txt example.png > file.txt`
- The program converts pixels to characters one-to-one, so realistically anything over 120x120px might be too big!
