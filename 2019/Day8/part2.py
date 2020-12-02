import sys

def main():
    height = 6
    width = 25
    layer_size = height * width

    file = open(input("Filename: "), 'r')
    pixels = file.readline()
    layers = [pixels[i:i + layer_size] for i in range(0, len(pixels), layer_size)]

    image = ["2" for i in range(layer_size)]

    for layer in layers:
        for i in range(layer_size):
            if image[i] == "2":
                image[i] = layer[i]
    
    for i in range(height):
        # print(i*width, (i+1)*width)
        row = image[i*width:(i+1)*width]
        row = ''.join(row)
        print(row.replace('0', 'XX').replace('1', '  '))
        print(row.replace('0', 'XX').replace('1', '  '))

main()