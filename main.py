import io
import time
def compress(uncompressed):
    # Build the dictionary. We initialize it with size of 256
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    # Iterate over each character c in uncompressed
    uncompressed=uncompressed+"."
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            # Update w to the new character
            w = c

    return result

def decompress(compressed):
    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    result = io.StringIO()
    # Pop first element and convert to char
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)
        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return result.getvalue()

def main():
    start_time = time.time()  # Record the start time
    with open("D:\\Facultate\\Python\\text\\text1.txt") as myfile:
        info = "".join(myfile.readlines())
        print("Data from text file: ", info)
        print("\n")

    print("Compressing Data-> ")
    compressed = compress(info)
    print("Compressed output: ", compressed)
    print("\n")

    # Writing compressed data to a text file
    with open("D:\\Facultate\\Python\\text\\compressed_text1.txt", "w") as compressed_file:
        compressed_file.write(",".join(map(str, compressed)))  # Writing comma-separated compressed data

    print("Decompressing Data-> ")
    decompressed = decompress(compressed)
    print("Decompressed output: ", decompressed)
    print("\n")

    print("COMPARE:")
    if info == decompressed:
        print("Successfully Done")
    else:
        print("Not done!")

    end_time = time.time()  # Record the end time
    execution_time = end_time - start_time
    print("Total execution time: {:.5f} seconds".format(execution_time))

if __name__ == "__main__":
    main()
