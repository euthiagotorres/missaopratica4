from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

pessoa=Pessoa('José', '12345', '2024-05-04', 'Ativo')
pessoa.imprimir_dados()

pessoa_fisica=PessoaFisica('Maria', '12344', '2024-04-04', 'Ativo', '2000-05-05', '01234567891', '123456')
pessoa_fisica.imprimir_dados()

pessoa_juridica=PessoaJuridica('Empresa Tal', '12345', '2024-05-02', 'Ativo', '2024-02-02', '12.123.456/0001-00')
pessoa_juridica.imprimir_dados()

#alterando dados via Setter
pessoa.nome='João Silva'
pessoa_fisica.cpf='12312312345'
pessoa_juridica._cnpj='00000000/0001-11'

pessoa.imprimir_dados()
pessoa_fisica.imprimir_dados()
pessoa_juridica.imprimir_dados()


