import flask, argparse

parser = argparse.ArgumentParser()
parser.add_argument('prueba', type=str, help='Introduce el DNI del estudiante')
args = parser.parse_args()
if args.prueba == 'B4907846':
    print('Correcto')
