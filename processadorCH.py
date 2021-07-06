import pandas as pd


def criaTabelaGabarito(df):
    ##carrega somente as colunas pertinentes
    df1 = df[['NU_INSCRICAO', 'TX_RESPOSTAS_CH', 'TX_GABARITO_CH']]

    ##Gera tabela de 45 questões vazias com zeros
    for i in range(45):
        df1.insert(len(df1.columns), 'Q'+str(i+1)+' CH', 0)


    ##para cada um dos alunos(linhas), compara a string de respostas com a de gabarito e preenche com 1 nas posições corretas.
    rowNumber = 0
    for index, row in df1.iterrows():
        
        if row['TX_RESPOSTAS_CH'] == row['TX_RESPOSTAS_CH']:
            for i in range(len(row['TX_RESPOSTAS_CH'])):
                
                if row['TX_RESPOSTAS_CH'][i] == row['TX_GABARITO_CH'][i]:
                    columnName = 'Q' + str(i+1) + ' CH'
                    df1.at[rowNumber, columnName] = 1
        
        rowNumber +=1
    ##dropa colunas nao pertinentes
    return df1.drop(['TX_RESPOSTAS_CH', 'TX_GABARITO_CH'], axis=1)

##método que gera o excel específico
def cria_excel(df):
    print('Criando Excel...')
    writer = pd.ExcelWriter('saidaCH.xls')
    df.to_excel(writer)
    writer.save()
    print('Excel criado com sucesso!')

