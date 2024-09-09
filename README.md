# CollegeSheduleScraper
## Инструкция по установке:
1. Создайте виртуальной окружение ```python -m venv venv```
2. Активируйте виртуальное окружение.
    Для windows: ```venv\Scripts\activate```
    Для linux и macos: ```source venv/bin/activate```
3. Установите зависимости: ```pip install -r requirements.txt```
4. Запустите приложение коммандой ```uvicorn main:app```
    дополнительно можете указать нужный порт:
    ```uvicorn main:app --port 8000```

## Документация
Дл просмотра доступных методов откройте авто-сгенерированную документацию по пути http://localhost:port/docs