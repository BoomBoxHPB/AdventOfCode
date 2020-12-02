import sys

def main():
    height = 6
    width = 25
    layer_size = height * width

    file = open(input("Filename: "), 'r')
    pixels = file.readline()
    layers = [pixels[i:i + layer_size] for i in range(0, len(pixels), layer_size)]

    # print(layers)
    # print(len(layers[0]))
    fewest_zeros = [None, layer_size + 1]
    for layer in layers:
        zero_count = layer.count("0")
        if zero_count < fewest_zeros[1]:
            fewest_zeros = [layer, zero_count]
    
    one_count = fewest_zeros[0].count("1")
    two_count = fewest_zeros[0].count("2")

    print(one_count * two_count)

main()