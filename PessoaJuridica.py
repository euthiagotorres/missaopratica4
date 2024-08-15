from Pessoa import Pessoa

class PessoaJuridica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, status, data_abertura_Empresa, cnpj):
        super().__init__(nome, numero_conta, data_abertura_conta, status)
        
        self.__data_abertura_Empresa=data_abertura_Empresa
        self.__cnpj=cnpj
        
    @property
    def data_abertura_Empresa(self):
        return self.__data_abertura_Empresa
    @data_abertura_Empresa.setter
    def data_abertura_Empresa(self, value):
        self.__data_abertura_Empresa=value
            
    @property
    def cnpj(self):
        return self.__cnpj
    @cnpj.setter
    def cnpj(self, value):
        if len(value)==18:
            self.__cnpj=value
        else:
            raise ValueError('CNPJ deve conter 18 caracteres.')
            
    def imprimir_dados(self):
        super().imprimir_dados()
        print(f'Data da abertura da empresa:{self.data_abertura_Empresa}')
        print(f'CNPJ:{self.cnpj}')
