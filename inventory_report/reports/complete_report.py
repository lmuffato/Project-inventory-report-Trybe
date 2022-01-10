from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, file):
        empresas = {}
        for obj in file:
            if obj['nome_da_empresa'] not in empresas:
                empresas[obj['nome_da_empresa']] = 1
            else:
                empresas[obj['nome_da_empresa']] += 1
        lista_itens = empresas.items()
        # for obj in file:
        #     empresas.append(obj['nome_da_empresa'])
        # x = collections.Counter(empresas)
        # print(x)
        cpny_list = "Produtos estocados por empresa: \n"
        for company, quantity in lista_itens:
            cpny_list += f"- {company}: {quantity}\n"

        return (
            f"{SimpleReport.generate(file)}\n"
            f"{cpny_list}"
        )


