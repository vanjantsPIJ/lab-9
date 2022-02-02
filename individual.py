#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    flights = []
    while True:
        command = input(">>> ").lower()
        if command == 'exit':
            break

        elif command == 'add':
            flight_destination = input("Введите название пункта назначения ")
            flight_number = input("Введите номер рейса ")
            airplane_type = input("Введите тип самолета ")
            flight = {
                'flight_destination': flight_destination,
                'flight_number': flight_number,
                'airplane_type': airplane_type,
            }
            flights.append(flight)
            if len(flights) > 1:
                flights.sort(
                    key=lambda item:
                    item.get('flight_destination', ''))

        elif command == 'list':
            line = '+-{}-+-{}-+-{}-+-{}-+'.format(
                '-' * 4,
                '-' * 30,
                '-' * 20,
                '-' * 15
            )
            print(line)
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    "No",
                    "Пункт назначения",
                    "Номер рейса",
                    "Тип самолета"
                )
            )
            print(line)

            for idx, flight in enumerate(flights, 1):
                print(
                    '| {:>4} | {:<30} | {:<20} | {:<15} |'.format(
                        idx,
                        flight.get('flight_destination', ''),
                        flight.get('flight_number', ''),
                        flight.get('airplane_type', 0)
                    )
                )
            print(line)

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=1)
            airplane_type = (parts[1].capitalize())
            print(f"Для типа самолета {airplane_type}:")
            count = 0
            for flight in flights:
                if flight.get('airplane_type') == airplane_type:
                    count += 1
                    print(
                        '{:>4}: Пункт назначения: {}; Номер рейса: {}'.format(
                            count,
                            flight.get('flight_destination',
                                       ''),
                            flight.get('flight_number', ''))
                    )
            if count == 0:
                print("рейсы не найдены")

        elif command == 'help':
            # Вывести справку о работе с программой.
            print("Список команд:\n")
            print("add - добавить рейс;")
            print("list - вывести список всех рейсов;")
            print("select <тип самолета> - запросить рейсы указанного типа "
                  "самолета;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")
        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)