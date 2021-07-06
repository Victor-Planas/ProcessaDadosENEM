import pandas as pd
import processadorCN as proccn
import processadorLC as proclc
import processadorMT as procmt
import processadorCH as procch

##método de criar excel
def cria_excel_final(df):
    print('Criando Excel...')
    writer = pd.ExcelWriter('saidaTotal.xls')
    df.to_excel(writer)
    writer.save()
    print('Excel criado com sucesso!')

##carrega o excel no dataFrame
df = pd.read_excel (r'dadosSemiProcessados2019.xls')
print('Rodando...')

##Gera o data frame para o caderno CN
##dfCN = proccn.criaTabelaGabarito(df).drop('NU_INSCRICAO', axis=1)
##proccn.cria_excel(dfCN)
##dfCN.to_csv(r'valoresNaoCalibrados2019CN.txt', header=None, index=None, sep=' ', mode='a')
##print('CN criado com sucesso!')

##Gera o data frame para o caderno MT
##dfMT = procmt.criaTabelaGabarito(df).drop('NU_INSCRICAO', axis=1)
##procmt.cria_excel(dfMT)
##dfMT.to_csv(r'valoresNaoCalibrados2019MT.txt', header=None, index=None, sep=' ', mode='a')
##print('MT criado com sucesso!')

##Gera o data frame para o caderno CH
##dfCH = procch.criaTabelaGabarito(df).drop('NU_INSCRICAO', axis=1)
##procch.cria_excel(dfCH)
##dfCH.to_csv(r'valoresNaoCalibrados2019CH.txt', header=None, index=None, sep=' ', mode='a')
##print('CH criado com sucesso!')

##Gera o data frame para o caderno LC sem as questoes de idioma
dfLC = proclc.criaTabelaGabarito(df).drop(['NU_INSCRICAO','Q1 LC', 'Q2 LC', 'Q3 LC', 'Q4 LC', 'Q5 LC', 'Q6 LC', 'Q7 LC', 'Q8 LC', 'Q9 LC', 'Q10 LC',], axis=1)
##proclc.cria_excel(dfLC)
dfLC.to_csv(r'valoresNaoCalibrados2019LCsemlingua.txt', header=None, index=None, sep=' ', mode='a')
print('LC criado com sucesso!')

##junta todas as tabelas e gera um arquivo com todas as matrizes
##tabelas_questoes = [dfCN, dfCH, dfMT, dfLC]
##dfFinal = pd.concat(tabelas_questoes, join='outer', axis=1)
##dfFinal.to_csv(r'valoresNaoCalibrados2019semLingua.txt', header=None, index=None, sep=' ', mode='a')
##cria_excel_final(dfFinal)