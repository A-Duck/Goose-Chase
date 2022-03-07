from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove, Update
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)
import re

LEVEL1, LEVEL2, LEVEL3, LEVEL4, LEVEL5, LEVEL6, LEVEL7, LEVEL8, LEVEL9, LEVEL10, LEVEL11, LEVEL12, LEVEL13, LEVEL14, LEVEL15, LEVEL16, LEVEL17 = range(17)

#############################################################################################################

def control(update: Update, context: CallbackContext) -> None:
    reply_keyboard = [['Yes', 'No']]

    update.message.reply_text(
        'Level 1\nThe Phone Rings...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='Do you answer?'
        ),
    )

    return LEVEL1

#############################################################################################################

def GoToLVL2(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Eat Lunch', 'Drink Coffee', 'Bunk Off', 'Answer Phone']]

    update.message.reply_text(
        'Level 2\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL2

#############################################################################################################

def GoToLVL3(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Eat Lunch', 'Nap', 'Drink Coffee', 'Answer Phone']]

    update.message.reply_text(
        'Level 3\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL3

#############################################################################################################

def GoToLVL4(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Lick Index Finger', 'Lick Middle Finger', 'Lick Thumb', 'Lick Ring Finger', 'Lick Pinky Finger', 'Answer the phone']]

    update.message.reply_text(
        'Level 4\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL4

#############################################################################################################

def GoToLVL5(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Lick Pinky Finger', 'Answer the phone', 'Lick Index Finger', 'Lick Middle Finger', 'Lick Ring Finger', 'Lick Thumb']]

    update.message.reply_text(
        'Level 5\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL5

#############################################################################################################

def GoToLVL6(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Lick Middle Finger', 'Lick Ring Finger', 'Answer the phone', 'Lick Index Finger', 'Lick Pinky Finger', 'Lick Thumb']]

    update.message.reply_text(
        'Level 6\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL6

#############################################################################################################

def GoToLVL7(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Answer the phone', 'Lick Pinky Finger', 'Lick Thumb', 'Lick Index Finger', 'Lick Middle Finger', 'Lick Ring Finger']]

    update.message.reply_text(
        'Level 7\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL7

#############################################################################################################

def GoToLVL8(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Answer the phone', 'Lick Ring Finger', 'Lick Thumb', 'Lick Pinky Finger', 'Lick Index Finger', 'Lick Middle Finger']]

    update.message.reply_text(
        'Level 8\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL8

#############################################################################################################

def GoToLVL9(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Nap', 'Drink Coffee', 'Go to Bathroom', 'Answer the phone', 'Start other hand']]

    update.message.reply_text(
        'Level 9\nYou should probably answer the phone...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL9

#############################################################################################################

def GoToLVL10(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Lick Thumb', 'Lick Index Finger', 'Lick Middle Finger', 'Lick Ring Finger', 'Lick Pinky Finger', 'Answer the phone']]

    update.message.reply_text(
        'Level 10\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL10

#############################################################################################################

def GoToLVL11(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Lick Pinky Finger', 'Answer the phone', 'Lick Index Finger', 'Lick Middle Finger', 'Lick Ring Finger', 'Lick Thumb']]

    update.message.reply_text(
        'Level 11\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL11

#############################################################################################################

def GoToLVL12(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Lick Middle Finger', 'Lick Ring Finger', 'Answer the phone', 'Lick Index Finger', 'Lick Pinky Finger', 'Lick Thumb']]

    update.message.reply_text(
        'Level 12\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL12

#############################################################################################################

def GoToLVL13(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Answer the phone', 'Lick Pinky Finger', 'Lick Thumb', 'Lick Index Finger', 'Lick Middle Finger', 'Lick Ring Finger']]

    update.message.reply_text(
        'Level 13\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL13

#############################################################################################################

def GoToLVL14(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Answer the phone', 'Lick Ring Finger', 'Lick Thumb', 'Lick Pinky Finger', 'Lick Index Finger', 'Lick Middle Finger']]

    update.message.reply_text(
        'Level 14\nWalk me through your day...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL14

#############################################################################################################

def GoToLVL15(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Greet co-worker', 'Nap', 'Go to Bathroom', 'Drink Coffee', 'Answer the phone']]

    update.message.reply_text(
        'Level 15\nThat phone has been ringing for a loong time...',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL15

#############################################################################################################

def GoToLVL16(update: Update, context: CallbackContext) -> int:
    reply_keyboard = [['Nap', 'Answer the phone', 'Go to Bathroom', 'Drink Coffee', 'Greet co-worker']]

    update.message.reply_text(
        'Level 16\nAre you ever going to answer it?',
        reply_markup=ReplyKeyboardMarkup(
            reply_keyboard, one_time_keyboard=True, input_field_placeholder='What do you do?'
        ),
    )

    return LEVEL16

#############################################################################################################

## What Question
def GoToLVL17(update: Update, context: CallbackContext) -> int:
    update.message.reply_text('You pick up the phone... What do you say?')

    return LEVEL17

#############################################################################################################

def LVL17Logic(update, context):
    FilterString = '^((?i)(Hello IT[\.,] Have you tried turning it off and on again\?))$'

    if (re.match(FilterString, update.message.text)):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Your clue is the new number for the emergency services\n\nhttps://endurance.jcpvdb.co.za")
        return ConversationHandler.END
    else:
        Death(update, context)
        return ConversationHandler.END

#############################################################################################################

def Death(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        'What kind of an IT professional are you!?\nTry again!', reply_markup=ReplyKeyboardRemove()
    )

    return ConversationHandler.END

#############################################################################################################

# Creates listeners for the Telegram bot's menu
def main():
    updater = Updater("Your Bot ID goes here")

    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', control)],
        states={
            LEVEL1: [
                MessageHandler(Filters.regex('^(Yes)$'), Death),
                MessageHandler(Filters.regex('^(No)$'), GoToLVL2)
            ],
            LEVEL2: [
                MessageHandler(Filters.regex('^(Eat Lunch)$'), Death),
                MessageHandler(Filters.regex('^(Drink Coffee)$'), GoToLVL3),
                MessageHandler(Filters.regex('^(Bunk Off)$'), Death),
                MessageHandler(Filters.regex('^(Answer Phone)$'), Death)
            ],
            LEVEL3: [
                MessageHandler(Filters.regex('^(Eat Lunch)$'), GoToLVL4),
                MessageHandler(Filters.regex('^(Drink Coffee)$'), Death),
                MessageHandler(Filters.regex('^(Nap)$'), Death),
                MessageHandler(Filters.regex('^(Answer Phone)$'), Death)
            ],
            LEVEL4: [
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), GoToLVL5),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death)
            ],
            LEVEL5: [
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), GoToLVL6),
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
            ],
            LEVEL6: [
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), GoToLVL7),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
            ],
            LEVEL7: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), GoToLVL8),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death)
            ],
            LEVEL8: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), GoToLVL9)
            ],
            LEVEL9: [
                MessageHandler(Filters.regex('^(Nap)$'), Death),
                MessageHandler(Filters.regex('^(Drink Coffee)$'), Death),
                MessageHandler(Filters.regex('^(Go to Bathroom)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Start other hand)$'), GoToLVL10),
            ],
            LEVEL10: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), GoToLVL11),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death)
            ],
            LEVEL11: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), GoToLVL12),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death)
            ],
            LEVEL12: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), GoToLVL13),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death)
            ],
            LEVEL13: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), GoToLVL14),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), Death)
            ],
            LEVEL14: [
                MessageHandler(Filters.regex('^(Lick Index Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Thumb)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Lick Ring Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Middle Finger)$'), Death),
                MessageHandler(Filters.regex('^(Lick Pinky Finger)$'), GoToLVL15)
            ],
            LEVEL15: [
                MessageHandler(Filters.regex('^(Nap)$'), Death),
                MessageHandler(Filters.regex('^(Drink Coffee)$'), GoToLVL16),
                MessageHandler(Filters.regex('^(Go to Bathroom)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), Death),
                MessageHandler(Filters.regex('^(Greet co-worker)$'), Death),
            ],
            LEVEL16: [
                MessageHandler(Filters.regex('^(Nap)$'), Death),
                MessageHandler(Filters.regex('^(Drink Coffee)$'), Death),
                MessageHandler(Filters.regex('^(Go to Bathroom)$'), Death),
                MessageHandler(Filters.regex('^(Answer the phone)$'), GoToLVL17),
                MessageHandler(Filters.regex('^(Greet co-worker)$'), Death),
            ],
            LEVEL17: [
                MessageHandler(Filters.text, LVL17Logic),
            ],
        },
        fallbacks=[CommandHandler('cancel', Death)],
    )

    dispatcher.add_handler(conv_handler)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

#############################################################################################################

main()