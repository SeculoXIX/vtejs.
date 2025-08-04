import sys
from datetime import datetime

disponibilida_stadard = 10
disponibilida_premium = 5
disponibilida_luxo = 3
quantidade_de_reservas = 0
soma_total_reservas = 0
maior_quant_reserva = 0

#Entrada e processamento de dados
for x in range(999999):
    if x == 0:
        print('''O que você quer fazer?
Uma reserva [1]
Encerra o programa [2]''')
        menu = int(input(':'))
    else:
        print('''O que você quer fazer?
    Uma uma outra reserva [1]
    Encerra o programa [2]''')
        menu = int(input(':'))

    if menu == 2:
        break
    if menu != 1 and 2:
        print('Digite um número válido')

    nome_responsavel = input('Qual o nome do respónsavel da reserva: ').strip()
    if nome_responsavel == '':
        print('Você precisa escrever o nome do respónsavel')
        sys.exit()

    check_in = input('Qual o dia da reserva: (aa/mm/aaaa) ')
    check_out = input('Qual o dia de saída: ')
    try:
        data_checkin = datetime.strptime(check_in, "%d/%m/%Y")
    except ValueError:
        print('Data inválida em check_in!')
        quit()
    try:
        data_checkout = datetime.strptime(check_out, "%d/%m/%Y")
    except ValueError:
        print('Data de check-out inválida!')
        quit()
    Quantida_de_dias = data_checkout - data_checkin

    #DISPONIBILIDADE DE QUARTOS
    print('Aqui está a quantidade de quartos disponíveis')
    print()
    print('Quarto standard = ',disponibilida_stadard)
    print('Quarto premium = ',disponibilida_premium)
    print('Quarto luxo = ',disponibilida_luxo)
    print()
    tipo_quarto = int(input('''Qual o tipo de quarto: 
Digite (1) para Standard 
Digite (2) para Premuim 
Digite (3) para Luxo 
:'''))
    if tipo_quarto == 1:
        quantidade_quartos = int(input('Qual a quantidade de quartos stander você quer: '))
        disponibilida_stadard -= quantidade_quartos
        if disponibilida_stadard < 0:
            print('Não temos essa quantidade de quantos dispobívais para esse quarto')
        else:
            if quantidade_quartos > maior_quant_reserva:
                maior_quant_reserva = quantidade_quartos
            valor_dias = Quantida_de_dias * 100
            soma_total_reservas += valor_dias
    
    
    elif tipo_quarto == 2:
        quantidade_quartos = int(input('Qual a quantidade de quartos stander você quer: '))
        disponibilida_premium -= quantidade_quartos
        if disponibilida_stadard < 0:
            print('Não temos essa quantidade de quantos dispobívais para esse quarto')
        else:
            if quantidade_quartos > maior_quant_reserva:
                maior_quant_reserva = quantidade_quartos
            valor_dias = Quantida_de_dias * 180
            soma_total_reservas += valor_dias

    elif tipo_quarto == 3:
        quantidade_quartos = int(input('Qual a quantidade de quartos stander você quer: '))
        disponibilida_luxo -= quantidade_quartos
        if disponibilida_stadard < 0:
            print('Não temos essa quantidade de quartos dispobívais para esse quarto')
        else:
            if quantidade_quartos > maior_quant_reserva:
                maior_quant_reserva = quantidade_quartos
            valor_dias = Quantida_de_dias * 250
            soma_total_reservas += valor_dias
    else:
        print('Escolha um tipo de querto possível')
    quantidade_de_reservas += 1
