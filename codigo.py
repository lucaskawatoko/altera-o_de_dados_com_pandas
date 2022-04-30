import pandas as pd

tabela = pd.read_excel('Pandas\Produtos.xlsx') # caminho do arquivo em sua maquina

# atualizando o multiplicador de seviço/ptoduto
tabela.loc[tabela["Tipo"] == "Serviço","Multiplicador Imposto"] = 1.5
tabela.loc[tabela["Tipo"] == "Produto","Multiplicador Imposto"] = 3.0

# fazer conta dsa tabela base reais

tabela["Preço Base Reais"] = tabela["Multiplicador Imposto"] * tabela["Preço Base Original"]

# salvando as modificações em novo arquivo

tabela.to_excel("Pandas/Nova_Tabela_De_Produtos.xlsx",index=False) # caminho onde a nova planilha será salva
print(tabela)
