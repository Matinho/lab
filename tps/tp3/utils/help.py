import argparse


def get_options():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-f', '--f', dest="file", required=True,help='Ingresar archivo')
    parser.add_argument('-p', '--p', dest="port", default=8080,type=int, help='Ingresar puerto')
        
    options = {
        'file': parser.parse_args().file,
        'port': parser.parse_args().port,
	
      
    }

    return options
