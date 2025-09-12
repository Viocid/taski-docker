Taski Docker
Репозиторий для запуска Taski с помощью Docker.

Предварительные требования
Docker

Docker Compose

Быстрый старт
Клонируйте репозиторий:

bash
git clone https://github.com/Viocid/taski-docker.git
cd taski-docker
Запустите приложение:

bash
docker-compose up -d
Откройте в браузере: http://localhost:3000

Структура проекта
text
taski-docker/
├── docker-compose.yml    # Конфигурация Docker Compose
├── nginx/
│   └── nginx.conf       # Конфигурация Nginx
└── README.md            # Этот файл
Конфигурация
Переменные окружения
Вы можете настроить приложение через переменные окружения в docker-compose.yml:

PORT - порт приложения (по умолчанию: 3000)

NODE_ENV - окружение (production/development)

Порт
По умолчанию приложение доступно на порту 3000. Чтобы изменить порт:

Отредактируйте docker-compose.yml

Измените маппинг портов: "Новый_порт:3000"

Команды
Запуск
bash
docker-compose up -d
Остановка
bash
docker-compose down
Просмотр логов
bash
docker-compose logs -f
Перезагрузка
bash
docker-compose restart
Обновление
Чтобы обновить до последней версии Taski:

Остановите контейнеры:

bash
docker-compose down
Перестройте образы:

bash
docker-compose build --no-cache
Запустите снова:

bash
docker-compose up -d
Устранение проблем
Порт уже занят
Если порт 3000 занят, измените маппинг портов в docker-compose.yml:

yaml
ports:
  - "другой_порт:3000"
Проблемы с правами
Если возникают проблемы с правами доступа:

bash
sudo chmod -R 755 .
Лицензия
Этот проект использует ту же лицензию, что и основной проект Taski.

Поддержка
Если у вас возникли проблемы:

Проверьте открытые issues

Создайте новое issue с описанием проблемы

Вклад в проект
Pull requests приветствуются! Для существенных изменений, пожалуйста, сначала откройте issue для обсуждения.

