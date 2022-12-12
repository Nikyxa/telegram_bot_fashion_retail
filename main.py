from datetime import datetime
import telebot
import init_django_orm  # noqa: F401
from csv_to_db.models import StartDate, Username, OwnerName
import csv
from constants import API_KEY


def run_tgbot():
    bot = telebot.TeleBot(API_KEY)

    @bot.message_handler(commands=["start"])
    def send_hello(msg):
        bot.send_message(
            msg.chat.id, "Hello! This is a test bot for parsing CSV files to DB!"
        )

    @bot.message_handler(content_types=["document"])
    def handle_file(message):
        try:
            file_info = bot.get_file(message.document.file_id)
            downloaded_file = bot.download_file(file_info.file_path)

            file = downloaded_file.decode("UTF-8")
            file = file.split("\r\n")[1:-1]
            reader = csv.reader(file, delimiter=";")

            for row in reader:

                date, _ = StartDate.objects.get_or_create(
                    date=datetime.strptime(row[0], "%d.%m.%Y")
                )
                date.save()

                name = OwnerName(name=row[1])
                name.save()

                username = Username(username=row[2])
                username.save()

            bot.reply_to(message, "Downloaded and added to DB!")

        except Exception as e:
            bot.reply_to(message, e)

    bot.polling(none_stop=True)


if __name__ == "__main__":
    run_tgbot()
