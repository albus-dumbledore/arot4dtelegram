import telegram
import openai
from telegram.ext import CommandHandler, MessageHandler, Filters, Updater

# Initialize the Telegram bot with your bot token
bot = telegram.Bot(token='6275352562:AAFeG6CryMwTPNxLRD1kn7yHc8g2TJ46Clk')

# Initialize the OpenAI API with your API key
openai.api_key = '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'

# Define a function to handle incoming messages and generate a response using ChatGPT
def handle_message(update, context):
    message = update.message.text
    response = openai.Completion.create(
        engine='davinci',
        prompt=message,
        temperature=0.7,
        max_tokens=100,
        n=1,
        stop=None,
        timeout=60,
    )
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.choices[0].text)

# Set up the message handler
updater = Updater(token='6275352562:AAFeG6CryMwTPNxLRD1kn7yHc8g2TJ46Clk', use_context=True)
dispatcher = updater.dispatcher
message_handler = MessageHandler(Filters.text, handle_message)
dispatcher.add_handler(message_handler)

# Start polling for new messages
updater.start_polling()

# Keep the kernel running
import time
while True:
    time.sleep(1)
