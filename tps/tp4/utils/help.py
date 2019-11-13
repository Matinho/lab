import argparse


def get_options():
    parser = argparse.ArgumentParser(description='Process some integers.')

    parser.add_argument('-u', '--url', dest="url", required=True, nargs="*",help='Ingresar url')
   
        
    options = {
        'url': parser.parse_args().url,
	
      
    }

    return options
