import pandas as pd
from twilio.rest import Client


# Your Account SID from twilio.com/console
account_sid = "AC7719479fabd8a1963077f604640f77de"
# Your Auth Token from twilio.com/console
auth_token  = "f1c0b9eb2052616ae294bc04630ada36"

client = Client(account_sid, auth_token)

#Passo a passo da silução 
# Twilio senha: 
# Abrir os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
   tabela_vendas = pd.read_excel(f'{mes}.xlsx')  
   if (tabela_vendas['Vendas'] >= 55000).any():
    vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendedor'].values[0]
    vendas = tabela_vendas.loc[tabela_vendas['Vendas'] >= 55000, 'Vendas'].values[0]
    print(f'No mes {mes} alguem bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
    message = client.messages.create(
        to="+5561981912241", 
        from_="+15618212390",
        body=f'No mes {mes} alguem bateu a meta. Vendedora: {vendedor}, Vendas: {vendas}')

    print(message.sid)






# Para cada arquivo:

# Verificar sem algum valor na coluna Vendas daquele arquivo é maior que 55.000

# Se for maior que 55.000 -> Envia um SMS com o nome, o mês e as vendas do vendedor

# Caso não seja maior que 55.000 não quero fazer nada 