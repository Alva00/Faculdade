def obter_saldo_usuario():
    while True:
        try:
            valor_inicial = float(input("Insira o valor do seu saldo atual.\nR$ ").replace(",", "."))
            despesas = float(input("Insira o valor total das suas dívidas atuais.\nR$ ").replace(",", "."))
            num_simulacoes_saldo_usuario = int(input("Insira a quantidade de simulações desejada.\n"))
        except ValueError:
            print("Erro. Insira um valor válido (ex.: 1212,12 ou 5).")
            continue
        if despesas < 0:
            print("A dívida deve ser positiva ou nula.")
            continue
        elif num_simulacoes_saldo_usuario < 1:
            print("Deve ocorrer pelo menos 1 simulação.")
            continue      
        break      
    
    saldos_finais = calcular_saldos_finais_usuario(valor_inicial, despesas, num_simulacoes_saldo_usuario)
    exibir_saldos_finais_usuario(valor_inicial, saldos_finais, num_simulacoes_saldo_usuario)
    
def calcular_saldos_finais_usuario(saldo_inicial, despesas, num_simulacoes_saldo_usuario):   
    saldos_finais = []
    for i in range(num_simulacoes_saldo_usuario):
        simulacao_saldo_inicial = round(saldo_inicial*(i+1) - despesas, 2)
        saldos_finais.append(simulacao_saldo_inicial)
    return saldos_finais

def exibir_saldos_finais_usuario(valor_inicial, saldos_finais, num_simulacoes_saldo_usuario):
    print(f'Saldo final: R$ {saldos_finais[0]} ---> Saldo inicial original, sem alterações.')
    
    if num_simulacoes_saldo_usuario > 1:
        for i in range(1, len(saldos_finais)):
            print(f'Possível saldo final: R$ {saldos_finais[i]} ---> Para saldo inicial multiplicado por {i+1} (R$ {(i+1)*valor_inicial}).')

def main():
    obter_saldo_usuario()

if __name__ == "__main__":
    main()