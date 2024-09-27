from models import Pessoa


def insere_pessoa():
    pessoa = Pessoa(nome='Rafael', idade=29)
    pessoa.save()
    print(pessoa)


def consulta():
    pessoa = Pessoa.query.all()

    pessoa = Pessoa.query.filter_by(nome='Rafael').first()
    print(pessoa)

def altera_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Rafael').first()

    pessoa.idade = 99
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoa.query.filter_by(nome='Rafael').first()
    pessoa.delete()

if __name__ == '__main__':
    #insere_pessoa()
    #consulta()
    altera_pessoa()