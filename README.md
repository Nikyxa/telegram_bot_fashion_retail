# Telegram bot for CSV files

Telegam bot which can be used for parsing CSV files and adding them to Data Base.

## Prepare the project
Use these commands to install and test Telegram bot.

```
git clone https://github.com/Nikyxa/telegram_bot_fashion_retail.git
python -m venv venv
venv\Scripts\activate (on Windows)
source venv/bin/activate (on macOS)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver (or use button)
```

## For testing in Telegram
- Find https://t.me/fashion_retail_bot
- Write command **/start**
- Add necessary file in CSV format