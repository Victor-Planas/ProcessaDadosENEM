import pandas as pd

def criaTabelaGabarito(df):

    df1 = df[['NU_INSCRICAO', 'TX_RESPOSTAS_MT', 'TX_GABARITO_MT']]

    for i in range(45):
        df1.insert(len(df1.columns), 'Q'+str(i+1)+' MT', 0)

    rowNumber = 0
    for index, row in df1.iterrows():
        
        for i in range(len(row['TX_RESPOSTAS_MT']) ):
            
            if row['TX_RESPOSTAS_MT'][i] == row['TX_GABARITO_MT'][i]:
                columnName = 'Q' + str(i+1) + ' MT'
                df1.at[rowNumber, columnName] = 1
        
        rowNumber +=1

    return df1.drop(['TX_RESPOSTAS_MT', 'TX_GABARITO_MT'], axis=1)


def cria_excel(df):
    print('Criando Excel...')
    writer = pd.ExcelWriter('saidaMT.xls')
    df.to_excel(writer)
    writer.save()
    print('Excel criado com sucesso!')

