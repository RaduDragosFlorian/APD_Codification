import io
import time
import multiprocessing


def compress(uncompressed):
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    w = ""
    result = []
    uncompressed = uncompressed + "."
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    return result


def decompress(compressed):
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    result = io.StringIO()
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
        dictionary[dict_size] = w + entry[0]
        dict_size += 1
        w = entry
    return result.getvalue()


def process_file(file_number):
    start_time = time.time()
    input_file = f"D:\\Facultate\\Python\\text\\text{file_number}.txt"
    output_file = f"D:\\Facultate\\Python\\text\\compressed_text{file_number}.txt"

    with open(input_file) as myfile:
        info = "".join(myfile.readlines())

    compressed = compress(info)

    with open(output_file, "w") as compressed_file:
        compressed_file.write(",".join(map(str, compressed)))

    decompressed = decompress(compressed)

    if info == decompressed:
        print(f"Successfully Done for text{file_number}.txt")
    else:
        print(f"Not done for text{file_number}.txt!")

    end_time = time.time()
    execution_time = end_time - start_time
    print("Total execution time for text{file_number}.txt: {:.5f} seconds".format(execution_time, file_number=file_number))


def main():
    num_processes = 6
    pool = multiprocessing.Pool(processes=num_processes)
    for i in range(1, num_processes + 1):
        pool.apply_async(process_file, args=(i,))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()
