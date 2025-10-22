# cats-allow-lists

Репозиторий с заблокированными сервисами и подсетями для тех, кому не хватает [allow-domain](https://github.com/itdoginfo/allow-domains)

# Сервисы

## Домены

> [!INFO]
> Сервисы обозначенные звёздочкой (*) не были полностью проверены на работоспособность.

* GitHub Copilot* - [список lst](https://raw.githubusercontent.com/wavy-cat/cats-allow-lists/refs/heads/master/domain/copilot.lst)
* Codecov - [список lst](https://raw.githubusercontent.com/wavy-cat/cats-allow-lists/refs/heads/master/domains/codecov.lst)

## Подсети

* AWS (Amazon Web Services) - [список lst](https://raw.githubusercontent.com/wavy-cat/cats-allow-lists/refs/heads/master/subnets/aws_v4.lst)
* GCP (Google Cloud Platform) - [список lst](https://raw.githubusercontent.com/wavy-cat/cats-allow-lists/refs/heads/master/subnets/gcp_v4.lst)
* Cloudflare - [список lst](https://raw.githubusercontent.com/wavy-cat/cats-allow-lists/refs/heads/master/subnets/cloudflare_v4.lst)

# Установка

## Домены

Включите в настройках Remote Domain Lists, скопируйте необходимые списки lst доменов и вставьте в Remote Domain URLs.

## Подсети

Включите в настройках Remote Subnet Lists, скопируйте необходимые списки lst подсетей и вставьте в Remote Subnet URLs.
