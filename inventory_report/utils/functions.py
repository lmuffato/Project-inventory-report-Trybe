# push comentary.
class Functions:

    def data_de_fabricacao(today, path, older):
        item = iter(path)
        while item:
            try:
                result = next(item)
                if (older > result['data_de_fabricacao']):
                    older = result['data_de_fabricacao']
            except StopIteration:
                break
        return older

    def data_de_validade(today, path, validate):
        item = iter(path)
        while item:
            try:
                result = next(item)
                element = result['data_de_validade']
                if (validate > element) and today < element:
                    validate = result['data_de_validade']
            except StopIteration:
                break
        return validate
