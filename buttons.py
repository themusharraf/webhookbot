from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Join Community", url="https://example.com/join"
            )
        ],
        [
            InlineKeyboardButton(
                text="Follow SCLUB on X", url="https://example.com/follow"
            )
        ],
        [
            InlineKeyboardButton(
                text="Let's go 🏆",
                web_app=WebAppInfo(url="webapp")
            )
        ]
    ]
)

