import logging

import uvicorn
from aiogram import Bot, Router, types, Dispatcher
from aiogram.filters import CommandStart
from fastapi import FastAPI, Request
from buttons import keyboard
from config import API_TOKEN, WEBHOOK_PATH, WEBHOOK_URL

bot = Bot(token=API_TOKEN)
router = Router()
dp = Dispatcher()
dp.include_router(router)

app = FastAPI()

logging.basicConfig(level=logging.INFO)


@router.message(CommandStart())
async def send_welcome(message: types.Message):
    await message.answer("""Текст, который будет написан после инициализации бота.\n\nEarn $SCLUB by completing tasks, playing mini-game and inviting your\nfrieds.Be among the first to join a wide-ranging sports ecosystem!\n\nДавайте добавим кнопки "Join Community, Follow SCLUB on X,  Let's go 🏆" под этим текстом.""",reply_markup=keyboard)



@app.on_event("startup")
async def on_startup():
    await bot.set_webhook(WEBHOOK_URL)


@app.on_event("shutdown")
async def on_shutdown():
    await bot.delete_webhook()


# Webhook endpoint
@app.post(WEBHOOK_PATH)
async def webhook_handler(request: Request):
    update = await request.json()
    update = types.Update(**update)
    await dp.feed_update(bot, update)
    return {"ok": True}

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)