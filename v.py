import sys
nome = input("Qual o nome do ser que vai fazer a reserva?")
if nome == '':
    print("Erro! É necessário colocar o nome.")
    sys.exit()
checkin_dia = int(input("Qual o dia de check-in?"))
if checkin_dia >= 31 or checkin_dia <= 0:
    print("Erro! A data de check-in é inexistente.")
    sys.exit()
checkin_mes = int(input("Qual o mês de check-in?"))
if checkin_mes >= 13 or checkin_mes <= 0:
    print("Erro! A data de check-in é inexistente.")
    sys.exit()
checkin_mes1 = checkin_mes * 30
checkin_ano = int(input("Qual o ano de check-in?"))
if checkin_ano <= 2024:
    print("Erro! A data de check-in é inexistente.")
    sys.exit()
checkin_ano1 = checkin_ano * 365
checkout_dia = int(input("qual o dia de check-out?"))
if checkout_dia <= checkin_dia:
    print("Erro! A data de check-out é inválida.")
    sys.exit()
checkout_mes = int(input("qual o mês de check-out?"))
if checkout_mes < checkin_mes:
    print("Erro! A data de check-out é inválida.")
    sys.exit()
checkout_ano = int(input("qual o ano de check-out?"))
if checkout_ano < checkin_ano:
    print("Erro! A data de check-out é inválida.")
    sys.exit()
soma_in = checkin_dia + checkin_mes1 + checkin_ano1
soma_out = checkout_dia + checkout_mes + checkout_ano
calc_soma = soma_out - soma_in
if calc_soma < 0:
    print("Erro! A data de check-out é maior que a data de check-in.")
    sys.exit()
elif checkin_dia >= 31:
    print("Erro! É necessário colocar um dia válido.")
    sys.exit()
print ("Digite 1 para escolher o quarto standard \n2 para escolher o quarto premimum \n3 para escolher o quarto de luxo")
quarto = int(input("Qual é o quarto?"))
if quarto == 1:
    valor_total = calc_soma * 100
elif quarto == 2:
    valor_total = calc_soma * 180
elif quarto == 3:
    valor_total = calc_soma * 250
else:
    print("Erro! Escolha um número de quarto válido.")
    sys.exit()
print(f"valor total do quarto será {valor_total} R$.")
