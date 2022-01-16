import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    # $ inventory_report <caminho_do_arquivo_input> <tipo_de_relatório>
    # print('@@@@@@@@@@@@@2@@@@')
    if(len(sys.argv) != 3):
        print('Verifique os argumentos', file=sys.stderr)

    fileType = sys.argv[1].split('.')[-1]

    if(fileType == 'json'):
        relatorio = InventoryRefactor(JsonImporter)
        relatorioFinal = relatorio.import_data(sys.argv[1], sys.argv[2])
        # print(relatorioFinal + '------------------')
        sys.stdout.write(relatorioFinal)
    elif(fileType == 'csv'):
        relatorio = InventoryRefactor(CsvImporter)
        relatorioFinal = relatorio.import_data(sys.argv[1], sys.argv[2])
        # print(relatorioFinal + '------------------')
        sys.stdout.write(relatorioFinal)
    elif(fileType == 'xml'):
        relatorio = InventoryRefactor(XmlImporter)
        relatorioFinal = relatorio.import_data(sys.argv[1], sys.argv[2])
        # print(relatorioFinal + '------------------')
        sys.stdout.write(relatorioFinal)

    pass
