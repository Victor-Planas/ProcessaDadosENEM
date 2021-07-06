import pandas as pd

def criaTabelaGabarito(df):

    df1 = df[['NU_INSCRICAO', 'TX_RESPOSTAS_LC', 'TX_GABARITO_LC']]

    for i in range(50):
        df1.insert(len(df1.columns), 'Q'+str(i+1)+' LC', 0)

    rowNumber = 0
    for index, row in df1.iterrows():
        
        if row['TX_RESPOSTAS_LC'] == row['TX_RESPOSTAS_LC']:
            for i in range(len(row['TX_RESPOSTAS_LC'])):
                
                if row['TX_RESPOSTAS_LC'][i] == row['TX_GABARITO_LC'][i]:
                    columnName = 'Q' + str(i+1) + ' LC'
                    df1.at[rowNumber, columnName] = 1
        
        rowNumber +=1

    return df1.drop(['TX_RESPOSTAS_LC', 'TX_GABARITO_LC'], axis=1)

def cria_excel(df):
    print('Criando Excel...')
    writer = pd.ExcelWriter('saidaLC.xls')
    df.to_excel(writer)
    writer.save()
    print('Excel criado com sucesso!')
