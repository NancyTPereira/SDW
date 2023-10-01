import pandas as pd

user_3941 = pd.DataFrame({
    'id': [3941],
    'name': ['Phylipe Phyton'],
    'account_number': ['12345-6'],
    'agency': ['0003'],
    'balance': [1250.00],
    'limit': [1650.00],
    'card_number': ['xxxx xxxx xxxx 1234'],
    'card_limit': [2200.0]
})

user_3942 = pd.DataFrame({
    'id': [3942],
    'name': ['Maria Panda'],
    'account_number': ['78910-1'],
    'agency': ['0003'],
    'balance': [200.00],
    'limit': [800.00],
    'card_number': ['xxxx xxxx xxxx 5678'],
    'card_limit': [200.0]
})


user_3943 = pd.DataFrame({
    'id': [3943],
    'name': ['Joao Almeida'],
    'account_number': ['11122-1'],
    'agency': ['0003'],
    'balance': [300.00],
    'limit': [900.00],
    'card_number': ['xxxx xxxx xxxx 9101'],
    'card_limit': [300.0]
})

user_3944 = pd.DataFrame({
    'id': [3944],
    'name': ['Lia Py'],
    'account_number': ['22222-1'],
    'agency': ['0003'],
    'balance': [400.00],
    'limit': [1000.00],
    'card_number': ['xxxx xxxx xxxx 9201'],
    'card_limit': [500.0]
})

users = pd.DataFrame({
    'id': [3941, 3942, 3943, 3944],
    'name': ['Phylipe Phyton', 'Maria Panda', 'Joao Almeida', 'Lia Py'],
    'balance': [1250.00, 200.00, 300.00, 400.00]
})



users = pd.concat([user_3941, user_3942, user_3943, user_3944])
users = users.fillna(0)
users = users.dropna()

# Aplicando uma função personalizada aos dados
def double_balance(balance):
    return balance * 2

users['balance'] = users['balance'].apply(double_balance)

# Salvando o DataFrame em um arquivo CSV
users.to_csv('users.csv', index=False)

    
# Função que personalize a mensagem para cada usuário
def mensagem_personalizada(nome):
    if nome in users['name'].tolist():
        info = users.loc[users['name'] == nome].iloc[0]
        return f"Olá {nome}, o seu saldo atual é de R${info['balance']:.2f}"
    else:
        return f"Desculpe, não consegui encontrar informações sobre {nome}\nInvista seu dinheiro para garantir o futuro!"

# Função para gerar mensagens personalizadas para cada usuário
print(mensagem_personalizada('Phylipe Phyton'))
print(mensagem_personalizada('Maria Panda'))
print(mensagem_personalizada('Joao Almeida'))
print(mensagem_personalizada('Lia Py'))

def mensagem_personalizada1(nome):
    if nome in users['name'].tolist():
        info = users.loc[users['name'] == nome].iloc[0]
        return f"Olá {nome}, Invista agora e garanta seu futuro financeiro. \nCondições especiais somente para você, aproveite!"
    else:
        return f"Desculpe, não consegui encontrar informações sobre {nome}."
        
print(mensagem_personalizada1('Phylipe Phyton'))
print(mensagem_personalizada1('Maria Panda'))
print(mensagem_personalizada1('Joao Almeida'))
print(mensagem_personalizada1('Lia Py'))

