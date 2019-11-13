import argparse


def get_options():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-f', '--file', dest="file", required=True, help='Ingrese nombre del archivo a leer.')
    parser.add_argument('-n', '--num_bytes', dest="num_bytes", required=True, type=int,
                        help='Ingrese cantidad de bytes a leer.')
    parser.add_argument('-p', '--processes', dest="children", default=2, type=int,
                        help='Ingrese cantidad de bytes a leer.')

    options = {
        'file': parser.parse_args().file,
        'num_bytes': parser.parse_args().num_bytes,
        'children': parser.parse_args().children
    }

    return options
