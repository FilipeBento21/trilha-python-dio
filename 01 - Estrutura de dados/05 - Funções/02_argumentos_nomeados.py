def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
#Caso inverta valores ele irá exibir de forma incorreta;

salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
#possui vantagem de manter os valores corretos independente da ordem;
#Possue desvantagem, caso mude algum argumento inicial causará um erro;

salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})
#kwargs, colocando valores em forma de dicionário;