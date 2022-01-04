from stock_utils import StockUtils


class SimpleReport(StockUtils):
    @classmethod
    def generate(stock):
        oldest_date = SimpleReport.get_oldest_manufacture_date(
          stock, 'data_de_fabricacao'
        )
        closest_due_date = SimpleReport.get_closest_due_date(
          stock, 'data_de_validade'
        )
        biggest_inventory = SimpleReport.get_biggest_inventory(
          stock, 'nome_da_empresa'
        )
        return f"""Data de fabricação mais antiga: {oldest_date}
    Data de validade mais próxima: {closest_due_date}
    Empresa com maior quantidade de produtos estocados: {biggest_inventory}
    """
