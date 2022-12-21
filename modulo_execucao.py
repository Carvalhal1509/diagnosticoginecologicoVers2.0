# Importação Biblioteca de Mensagens
import modulo_mensagens

# Dicionário e Listas (Informações dos Pacientes)
dados = dict()
doenças = list()


# Coleta de Dados e Inserção em Dicionário e Lista
def dadospessoais():
    while True:
        nome = str(input('Informe o seu nome: ')).strip().upper()
        if nome.isalpha() is True:
            dados['nome'] = nome
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['idade'] = int(input(f'{dados["nome"]}, informe a sua idade: '))
        if dados['idade'] >= 1 and dados['idade'] < 120:
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['incomodo'] = str(input(f'{dados["nome"]}, Você tem algum incomodo na area genital? [s/n]: ')).strip().upper()[0]
        if dados['incomodo'] in 'S':
            break
        else:
            modulo_mensagens.errodado()

def dadosdoenças():
    while True:
        dados['anemia'] = str(input(f'A) Você tem anemia [s/n]: ')).strip().upper()[0]
        if dados['anemia'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['constipacao'] = str(input(f'B) Você tem constipação intestinal [s/n]: ')).strip().upper()[0]
        if dados['constipacao'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['diabetes'] = str(input(f'C) Você é diabético(a) [s/n]: ')).strip().upper()[0]
        if dados['diabetes'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()


def dadossintomas():
    while True:
        dados['intcolica'] = str(input(f'A) Você está com colica intensa? [s/n]: ')).strip().upper()[0]
        if dados['intcolica'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['colica'] = str(input(f'A) Você está com colica? [s/n]: ')).strip().upper()[0]
        if dados['colica'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['coceira'] = str(input(f'B) Você está com coceira? [s/n]: ')).strip().upper()[0]
        if dados['coceira'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['corrimento'] = str(input(f'C) Você está com corrimento esbranquiçado? [s/n]: ')).strip().upper()[0]
        if dados['corrimento'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['irritacao'] = str(input(f'D) Você está com irritação na vulva? [s/n]: ')).strip().upper()[0]
        if dados['irritacao'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
            
    while True:
        dados['vermelhidao'] = str(input(f'E) Você está com vermelhidão na vulva? [s/n]: ')).strip().upper()[0]
        if dados['vermelhidao'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['dor'] = str(input(f'F) Você está com dor durante a relação sexual? [s/n]: ')).strip().upper()[0]
        if dados['dor'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()
    while True:
        dados['sangramento'] = str(input(f'G) Você está com sangramento fora do periodo menstrual? [s/n]: ')).strip().upper()[0]
        if dados['sangramento'] in 'SN':
            break
        else:
            modulo_mensagens.errodado()

# Análise de Dados para Relatório
def análise1():
    if dados['idade'] >= 60:
        modulo_mensagens.grim60()
        if dados['dor'] == 'S':
            modulo_mensagens.msganemias()
        else:
            modulo_mensagens.msganemian()
    else:
        modulo_mensagens.gri()
        if dados['sangramento'] == 'S':
            modulo_mensagens.msgmiomas()
        else:
            modulo_mensagens.msgmioman()


def análise2():
    if dados['anemia'] == 'S':
        doenças.append(str('ANEMIA'))
    if dados['constipacao'] == 'S':
        doenças.append(str('CONSTIPACAO'))
    if dados['diabetes'] == 'S':
        doenças.append(str('DIABETES'))
    if doenças == []:
        modulo_mensagens.msgdoencasn()
    else:
        modulo_mensagens.msgdoencass()


def análise3():
    sintomasgraves = 0
    if dados['anemia'] == 'S':
        sintomasgraves += 1
    if dados['sangramento'] == 'S':
        sintomasgraves += 1
    if sintomasgraves == 1 or sintomasgraves == 2:
        modulo_mensagens.msgsintomasgraves()

    if dados['anemia'] == 'N' and dados['sangramento'] == 'N':
        sintomasmenosgraves = 0
        if dados['dor'] == 'S':
            sintomasmenosgraves += 1
        if dados['vermelhidao'] == 'S':
            sintomasmenosgraves += 1
    if sintomasmenosgraves == 1 or sintomasmenosgraves == 2:
        modulo_mensagens.msgsintomasmenosgraves()
        
        
    if dados['dor'] == 'N' and dados['vermelhidao'] == 'N':
        sintomasendo = 0
        if dados['colica'] == 'S':
            sintomasendo += 1
        if dados['constipacao'] == 'S':
            sintomasendo += 1
    if sintomasendo == 1 or sintomasendo == 2:
        modulo_mensagens.msgsintomasendo()
        
    if dados['colica'] == 'N' and dados['constipacao'] == 'N':
        sintomasleves = 0
        if dados['coceira'] == 'S':
            sintomasleves += 1
        if dados['corrimento'] == 'S':
            sintomasleves += 1
        if sintomasleves == 0:
            modulo_mensagens.msgsemsintomas()
        if sintomasleves == 1 or sintomasleves == 2:
            modulo_mensagens.msgsintomasleves()


def log_erro(msg):
    with open('log_erro.txt', 'a+') as file:
        file.write(f'{msg}\n')