'''
1 - Gustavo Ferreira Galazzo - RA: 2302539
2 - Guilherme Mauricio Lima - RA: 2303163
3 - Diego Nascimento de Faria - RA: 2302808
4 - Daniel dos Santos Silva - RA: 2302763
5 - Bianca Tsuruda Prado - RA: 2302593
'''
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Criação do banco de dados SQLite e configuração do SQLAlchemy
engine = create_engine('sqlite:///hospital.db')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Definição das tabelas
class Paciente(Base):
    __tablename__ = 'PACIENTE'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255))
    cpf = Column(String(255))
    idade = Column(Integer)
    exames = relationship('Exame', back_populates='paciente')

class Medico(Base):
    __tablename__ = 'MEDICO'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(255))
    crm = Column(String(255))
    especializacao = Column(String(255))
    exames = relationship('Exame', back_populates='medico')

class Exame(Base):
    __tablename__ = 'EXAME'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_medico = Column(Integer, ForeignKey('MEDICO.id'))
    id_paciente = Column(Integer, ForeignKey('PACIENTE.id'))
    descricao = Column(String(255))
    resultado = Column(String(255))
    medico = relationship('Medico', back_populates='exames')
    paciente = relationship('Paciente', back_populates='exames')

# Criação das tabelas no banco de dados 
Base.metadata.create_all(engine)

# Funções para o menu de operações
def cadastrar_medico(nome, crm, especializacao):
    medico = Medico(nome=nome, crm=crm, especializacao=especializacao)
    session.add(medico)
    session.commit()
    print("Médico cadastrado com sucesso!")

def cadastrar_paciente(nome, cpf, idade):
    paciente = Paciente(nome=nome, cpf=cpf, idade=idade)
    session.add(paciente)
    session.commit()
    print("Paciente cadastrado com sucesso!")

def cadastrar_exame(id_medico, id_paciente, descricao, resultado):
    exame = Exame(id_medico=id_medico, id_paciente=id_paciente, descricao=descricao, resultado=resultado)
    session.add(exame)
    session.commit()
    print("Exame cadastrado com sucesso!")

def consultar_exames_paciente(id_paciente):
    exames = session.query(Exame).filter_by(id_paciente=id_paciente).all()
    if exames:
        for exame in exames:
            print(f"ID do Exame: {exame.id}, Descrição: {exame.descricao}, Resultado: {exame.resultado}")
    else:
        print("Nenhum exame encontrado para este paciente.")

def menu():
    while True:
        print("\n--- HealthCare Manager ---")
        print("Menu de Opções:")
        print("1. Cadastrar médico")
        print("2. Cadastrar paciente")
        print("3. Cadastrar exame")
        print("4. Consultar exames de um paciente")
        print("5. Sair")
        opcao = int(input("Escolha uma opção: "))
        
        if opcao == 1:
            nome = input("Nome do médico: ")
            crm = input("CRM do médico: ")
            especializacao = input("Especialização do médico: ")
            cadastrar_medico(nome, crm, especializacao)
        elif opcao == 2:
            nome = input("Nome do paciente: ")
            cpf = input("CPF do paciente: ")
            idade = int(input("Idade do paciente: "))
            cadastrar_paciente(nome, cpf, idade)
        elif opcao == 3:
            id_medico = int(input("ID do médico: "))
            id_paciente = int(input("ID do paciente: "))
            descricao = input("Descrição do exame: ")
            resultado = input("Resultado do exame: ")
            cadastrar_exame(id_medico, id_paciente, descricao, resultado)
        elif opcao == 4:
            id_paciente = int(input("ID do paciente: "))
            consultar_exames_paciente(id_paciente)
        elif opcao == 5:
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()