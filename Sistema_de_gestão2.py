import sys
from datetime import datetime
import os

disponibilida_stadard = 10
disponibilida_premium = 5
disponibilida_luxo = 3
quantidade_de_reservas = 0
soma_total_reservas = 0
maior_quant_reserva = 0
nome_reserva_mais_cara = ''
menu = 2

#Entrada e processamento de dados

while menu != 1:
    print('O que você quer fazer \nUma reserva [1] \nEncerra o programa[2]')
    menu = int(input(':'))

    nome_responsavel = input('Qual o nome do respónsavel da reserva: ').strip()
    if nome_responsavel == "":
        print('Você precisa escrever o nome do respónsavel')
        sys.exit()
    os.system('clear')
    check_in = input('Qual o dia da reserva: (aa/mm/aaaa) ')
    try:
        data_checkin = datetime.strptime(check_in, "%d/%m/%Y")
    except ValueError:
        print('Data inválida em check_in!')
        quit()
    check_out = input('Qual o dia de saída: ')
    os.system('clear')
    try:
        data_checkout = datetime.strptime(check_out, "%d/%m/%Y")
    except ValueError:
        print('Data de check-out inválida!')
        quit()
    Quantida_de_dias_delta = data_checkout - data_checkin
    Quantida_de_dias = Quantida_de_dias_delta.days
    if Quantida_de_dias < 0:
        print('Data de check-in maior que de check-out')
        sys.exit()

    os.system('clear')

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
                nome_reserva_mais_cara = nome_responsavel
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
                nome_reserva_mais_cara = nome_responsavel
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
                nome_reserva_mais_cara = nome_responsavel
            valor_dias = Quantida_de_dias * 250
            soma_total_reservas += valor_dias
    else:
        print('Escolha um tipo de querto possível')
    quantidade_de_reservas += 1
if quantidade_de_reservas == 0:
    media_reservas = soma_total_reservas
    pass
else:
    media_reservas = soma_total_reservas / quantidade_de_reservas

print(f'O total de reservas realizadas = {quantidade_de_reservas}')
print(f'Soma total das reservas = {soma_total_reservas}')
print(f'Média total das reservas = {media_reservas}')
print(f'Maior valor de reserva foi de {maior_quant_reserva} e o respónsavel é {nome_reserva_mais_cara}')
