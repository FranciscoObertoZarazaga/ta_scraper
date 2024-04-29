
class Indicator:
    def __init__(self, title):
        self.title = title
        self.params = list()

    def setParams(self, params):
        for param in params:
            param = param.text.replace(': pandas.core.series.Series', '')
            excluir = ['high', 'low', 'close', 'open', 'volume']
            if 'bool' not in param and param not in excluir:
                self.params.append(param)
        if len(self.params) == 0:
            self.params.append('No recibe parámetros.')

    def __str__(self):
        msg = f'{self.title}\n'
        for param in self.params:
            msg += f'{param}\n'
        return msg
