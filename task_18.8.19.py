try:
    tickets = int(input('Сколько билетов хотите купить?\n'))
    tickets_list = [i + 1 for i in range(tickets)]
    result = []

    for ticket in tickets_list:
        age = int(input('Сколько лет посетителю с билетом №{}\n'.format(ticket)))
        if age < 18:
            result.append(0)
        elif age < 25:
            result.append(990)
        else:
            result.append(1390)

    if len(result) > 3:
        sale = int(sum(result) * 10 / 100)
        print('Сумма к оплате: {} руб.'.format(sum(result) - sale))
    else:
        print('Сумма к оплате: {} руб.'.format(sum(result)))
except ValueError:
    print('Пожалуйста вводите целые числа')