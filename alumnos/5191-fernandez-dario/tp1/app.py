#!/usr/bin/python
from utils.help import get_options
from multiprocessing import Process, Queue


def create_children():
    children = []

    for i in range(options['children']):
        child = Process(target=count_words, args=(out_queue,))
        children.append(child)
        child.start()
    return children


def count_words(out_queue):
    sum_words = 0
    while True:
        content = in_queue.get()

        if content == '':
            break
        len_content = len(content.split())

        sum_words = sum_words + len_content

        out_queue.put(sum_words)
        if in_queue.empty():
            show_words()


def read_file(in_queue):
    import os
    fd = os.open(options['file'], os.O_RDONLY)
    delims = [' ', '\t', '\n', ',']
    next_word = ''
    parcial_word = []
    while True:
        content = os.read(fd, options['num_bytes'])
        if content == '':
            break
        if not content[-1] in delims:
            partial_line = content.split()

            len_parcial_word = len(partial_line[-1])
            parcial_word.append(partial_line[-1])

            diff = options['num_bytes'] - len_parcial_word
            if diff != 0:
                parcial_word = []
                word = next_word + content[0:diff]

                next_word = content[diff: options['num_bytes']]
                in_queue.put(word)
            else:
                word_concat = "".join(parcial_word)
                next_word = next_word + word_concat

    os.close(fd)


def show_words():
    total_words = 0
    while out_queue.qsize() > 0:
        total_words = out_queue.get()

    print 'La cantidad de palabras encontradas fueron: ', total_words


if __name__ == "__main__":
    options = get_options()

    in_queue = Queue()
    out_queue = Queue()

    children = create_children()

    read_file(in_queue)

    for child in children:
        child.join()
