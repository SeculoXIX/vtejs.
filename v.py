import sys
nome = input("Qual o nome do ser que vai fazer a reserva?")
if nome == '':
    print("Erro! É necessário colocar o nome.")
    sys.exit()
checkin_dia = int(input("Qual o dia de check-in?"))
checkin_mes = int(input("Qual o mês de check-in?"))
checkin_ano = int(input("Qual o ano de check-in?"))
checkout_dia = int(input("qual o dia de check-out?"))
checkout_mes = int(input("qual o mês de check-out?"))
checkout_ano = int(input("qual o ano de check-out?"))
soma_in = checkin_dia + checkin_mes + checkin_ano
soma_out = checkout_dia + checkin_mes + checkout_ano
calc_soma = soma_out - soma_in
if calc_soma < 0:
    print("Erro! A data de check-in é maior que a data de check-out.")
    sys.exit()
elif checkin_dia >= 31:
    print("Erro! É necessário colocar um dia válido.")
    sys.exit()
print ("Digite 1 para escolher o quarto standard\n 2 para escolher o quarto premimum \n 3 para escolher o quarto de luxo")
quarto = int(input("Qual é o quarto?"))
if quarto != "1" or "2" or "3":
    print("Erro! Escolha um número de quarto possível.")
    sys.exit()
if quarto == 1:
    valor_total = calc_soma * 100
elif quarto == 2:
    valor_total = calc_soma * 180
else:
    valor_total = calc_soma * 250
print(f"valor total do quarto será {valor_total} R$.")
