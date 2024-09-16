from PIL import ImageFilter, Image
import time


def median_filter_diy(data, filter_size: int):
    indexer = filter_size // 2

    for x in range(data.size[0]):
        for y in range(data.size[1]):
            temp = []

            for k in range(filter_size):
                if x + k - indexer < 0 or x + k - indexer > data.size[0] - 1:
                    for c in range(filter_size):
                        temp.append((0, 0, 0))
                else:
                    if y + k - indexer < 0 or y + indexer > data.size[1] - 1:
                        temp.append((0, 0, 0))
                    else:
                        for z in range(filter_size):
                            temp.append(data.getpixel((x + k - indexer, y + z - indexer)))
            pixel = [0, 0, 0]
            for i in range(3):
                temp.sort(key=lambda x: x[i])
                pixel[i] = temp[len(temp) // 2][i]
            data.putpixel((x, y), tuple(pixel))
    return data


if __name__ == '__main__':
    im = Image.open('./balloons_noisy.png')

    sum_time_diy = 0
    for i in range(100):
        im2 = im.copy()
        start = time.process_time()
        median_filter_diy(im2, 3)
        sum_time_diy += (time.process_time() - start)

    sum_time_pil = 0
    for i in range(100):
        im2 = im.copy()
        start = time.process_time()
        im2.filter(ImageFilter.MedianFilter(3))
        sum_time_pil += (time.process_time() - start)

    print(f'{sum_time_diy=}, {sum_time_pil=}')

    removed_noise = median_filter_diy(im.copy(), 3)
    removed_noise.show('diy')

    im.copy().filter(ImageFilter.MedianFilter(3)).show('pil')
