import sys
import os
from inventory_report.inventory.inventory import Inventory

INVALID_ARG = 22


def check_input_file(path):
    file_exists = os.path.exists(path)
    if(not file_exists):
        sys.stderr.write('\nArquivo não existe\n\n')
        sys.exit(INVALID_ARG)


def check_report_type(type):
    if(type not in ['simples', 'completo']):
        sys.stderr.write(
            '\nTipo de relatório inválido. Entrada válidas'
            ' -> {"1": "simples", "2": "completo"} \n\n'
        )
        sys.exit(INVALID_ARG)


def main():
    args = sys.argv
    if(len(args) < 3):
        sys.stderr.write('Verifique os argumentos\n')
        # error = sys.stderr.write('Verifique os argumentos\n')
        # sys.exit(error)
    else:
        current_path, file_path, report_type = args
        check_input_file(file_path)
        check_report_type(report_type)

        report_str = Inventory.import_data(file_path, report_type)
        sys.stdout.write(report_str)

# main()
