from Pessoa import Pessoa

class PessoaFisica(Pessoa):
    def __init__(self, nome, numero_conta, data_abertura_conta, status, data_nascimento, cpf, rg):
        super().__init__(nome, numero_conta, data_abertura_conta, status)
        self.__data_nascimento=data_nascimento
        self.__cpf=cpf
        self.__rg=rg
        
        @property
        def data_nascimento(self):
            return self.__data_nascimento
        @data_nascimento.setter
        def data_nascimento(self, value):
            self.__data_nascimento=value
            
        @property
        def cpf(self):
            return self.__cpf
        @cpf.setter
        def cpf(self, value):
            if len(value)==11:
                self.__cpf=value
            else:
                raise ValueError('CPF deve ter 11 caracteres.')
            
        @property
        def rg(self):
            return self.__rg
        @rg.setter
        def rg(self, value):
            self.__rg=value
        
        def imprimir_dados(self):
            super().imprimir_dados()
            print(f'Data de nascimento:{self.data_nascimento}')
            print(f'CPF:{self.cpf}')
            print(f'RG:{self.rg}')