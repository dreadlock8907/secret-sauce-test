# Автоматизация тестирования SauceDemo

Автоматизация тестирования логина на https://www.saucedemo.com/ с использованием Python 3.10, Playwright и Page Object Model.

## Требования

- Docker

## Быстрый старт

1. Установить Docker
2. Запустить `run.bat` (Windows) или `./run.sh` (Linux/Mac)
3. Открыть http://localhost:8080 для просмотра отчета

### Запуск тестов

**Linux/Mac:**
```bash
./run.sh
```

**Windows:**
```bash
run.bat
```

После запуска отчет будет доступен по адресу: **http://localhost:8080**

Остановить сервер отчетов:
```bash
docker-compose down
```

## Команды управления тестами

```bash
make test              # Запустить все тесты
make test-crit         # Запустить только критичные тесты
make clean             # Очистить результаты
```

## Тестовые сценарии

1. **test_successful_login** - успешная авторизация (standard_user / secret_sauce)
2. **test_login_with_invalid_password** - проверка ошибки при неверном пароле
3. **test_locked_out_user_login** - проверка блокировки (locked_out_user)
4. **test_login_with_empty_fields** - валидация пустых полей
5. **test_performance_glitch_user_login** - работа с задержками (performance_glitch_user)

## Протестировано на

- macOS 15.3.2 (24D81)
- Windows 11 Pro (24H2)

## Лицензия

MIT License
