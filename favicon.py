from PIL import Image

def generate_favicon(input_filename):
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (192, 192), (256, 256)]
    favicon = Image.open(input_filename)
    favicon.save('favicon.ico', sizes=sizes)

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 2:
        print('Usage: python favicon.py pfp.png')
        sys.exit(1)
    generate_favicon(sys.argv[1])
