# Importação do Módulo
import modulo_execucao


# Mensagens da Aplicação
def títulos(msg):
    print('+=' * 40)
    print(f'{msg:^80}')
    print('+=' * 40)


def grim60():
    print(f'=> Você está com {modulo_execucao.dados["idade"]} anos, portanto, '
          f'está em grupo de risco pela idade e deve procurar um medico.')


def gri():
    print(f'=> Você está com {modulo_execucao.dados["idade"]} anos, portanto, '
          f'não está em grupo de risco pela idade.')


def msganemias():
    print(f'=> Você é anemica, isso agrava o seu quadro ginecologico!')


def msganemian():
    print(f'=> Você não é anemica. Parabéns! Isso pode não agravar seu quadro ginecologico!')
    
def msgmiomas():
    print(f'=> Você pode ter um Mioma, isso agrava o seu quadro ginecologico!')
    
def msgmioman():
    print(f'=> Você não tem um mioma.Parabéns! Isso pode não agravar seu quadro ginecologico!')


def msgdoencass():
    print(f'=> Seu quadro de doenças pré-existentes que podem agravar o fator '
          f'de risco: ')
    print(f'    => {modulo_execucao.doenças}')


def msgdoencasn():
    print(f'=> Você não possui quadro prévio, portanto, não terá o '
          f'risco agravado.')

def msgsintomasmenosgraves():
    print(f'=> Você apresenta sérios sintomas que podem indicar Vulvovaginite. \n'
          f'    Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!')

def msgsintomasgraves():
    print(f'=> Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!')

def msgsintomasendo():
    print(f'=> Você apresenta sérios sintomas que podem indicar Endometriose. \n'
          f'    Procure imediatamente um ponto de atendimento e relate seus sintomas. \n'
          f'    Cuide-se, pois, o seu quadro pode se agravar rapidamente!')



def msgsintomasleves():
    print(f'=> Você apresenta sintomas leves que podem significar Candidiase. \n'
          f'    Se apresentar quadro de colica intensa, procure o sistema de \n'
          f'    saúde imediatamente relatando os sintomas apresentados.')


def msgsemsintomas():
    print(f'=> Você não possui nenhum sintoma de doenca,que pode significar Vulvite. \n'
          f'    Caso o quadro nao melhore, procure o sistema de saúde.')


def cabeçalhorel():
    print(f'{modulo_execucao.dados["nome"]}, segue o relatório baseado '
          f'em suas respostas:')


# Tratamento de Erros
def errodado():
    print(f'=> Dado inválido, tente novamente!')


def errogenerico():
    print(f'=> Houve um erro geral no Sistema!')