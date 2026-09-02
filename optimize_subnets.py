#!/usr/bin/env python3
"""
Укрупняет (агрегирует) соседние подсети и удаляет избыточные
(те, что уже покрываются другими подсетями из списка).

Использование:
    python collapse_subnets.py subnets.txt

Формат входного файла — по одной подсети в строке, например:
    104.156.80.0/24
    104.156.81.0/24
    ...

Пустые строки и строки, начинающиеся с '#', игнорируются.
"""

import sys
import ipaddress


def read_networks(path):
    networks = []
    with open(path, "r", encoding="utf-8") as f:
        for lineno, raw_line in enumerate(f, start=1):
            line = raw_line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                # strict=False — на случай, если в строке указан не адрес сети,
                # а произвольный IP с маской (например, host-адрес внутри подсети)
                net = ipaddress.ip_network(line, strict=False)
            except ValueError as e:
                print(f"[строка {lineno}] пропущено: '{line}' — {e}", file=sys.stderr)
                continue
            networks.append(net)
    return networks


def main():
    if len(sys.argv) != 2:
        print(f"Использование: {sys.argv[0]} <файл_с_подсетями>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    networks = read_networks(input_path)

    if not networks:
        print("Не найдено ни одной корректной подсети.", file=sys.stderr)
        sys.exit(1)

    # collapse_addresses сам:
    #  - убирает подсети, целиком входящие в другие (избыточные)
    #  - объединяет соседние подсети в более крупные, если это возможно
    #    без захвата "чужих" адресов
    collapsed = list(ipaddress.collapse_addresses(networks))
    collapsed.sort()

    for net in collapsed:
        print(net)


if __name__ == "__main__":
    main()
