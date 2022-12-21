# Importação
import modulo_execucao
import modulo_mensagens

# Principal
try:
    modulo_mensagens.títulos('SISTEMA DE AJUDA NO DIAGNÓSTICO DE DOENCAS GINECOLOGICAS')
    modulo_execucao.dadospessoais()
    modulo_mensagens.títulos('DOENÇAS PRÉ-EXISTENTES')
    modulo_execucao.dadosdoenças()
    modulo_mensagens.títulos('SINTOMAS APRESENTADOS')
    modulo_execucao.dadossintomas()

except Exception as erro:
    modulo_mensagens.errogenerico()
    modulo_execucao.log_erro(erro)

else:
    modulo_mensagens.títulos('RELATÓRIO DOS DADOS INFORMADOS')
    modulo_mensagens.cabeçalhorel()
    modulo_execucao.análise1()
    modulo_execucao.análise2()
    modulo_execucao.análise3()

# Mensagens Personalizadas ao Final do Script
finally:
    modulo_mensagens.títulos('O DIAGNOSTICO APRESENTADO NAO SUBSTITUI UM DIAGNOSTICO MEDICO,SE O CASO PERSISTIR CONSULTE UM MEDICO!')
    modulo_mensagens.títulos('SE ALIMENTE BEM,BEBA AGUA E EVITE ROUPAS APERTADAS !')
    modulo_mensagens.títulos('OBRIGADO POR UTILIZAR O SISTEMA!')