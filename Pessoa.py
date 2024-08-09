class Pessoa:
    def __init__(self,  nome, numero_conta, data_abertura_conta, status):
        self.__nome=nome
        self.__numero_conta=numero_conta
        self.__data_abertura=data_abertura_conta
        self.__status=status
        
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, value):
        self.__nome=value
        
    @property
    def numero_conta(self):
        return self.__numero_conta
    
    @numero_conta.setter
    def numero_conta(self, value):
        self.__numero_conta=value
        
    @property
    def data_abertura(self):
        return self.__data_abertura
    
    @data_abertura.setter
    def data_abertura(self, value):
        self.__data_abertura=value
        
        
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, value):
        self.__status=value
        
        
        
    def imprimir_dados(self):
        print(f'Nome:{self.nome}')
        print(f'Número da conta:{self.numero_conta}')
        print(f'Data de abertura da conta:{self.data_abertura}')
        print(f'Status:{self.status}')