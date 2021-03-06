# Copyright (C) 2020 BristolMyers
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
# ExelonUserBot - EfsaneUserbot
import io
import asyncio
from .sql_helper import pmpermit_sql as pmpermit_sql
from telethon.tl.functions.users import GetFullUserRequest
from telethon import events, functions
from .. import ALIVE_NAME, CMD_HELP
from ..utils import admin_cmd
from . import check

PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
CACHE = {}
PMPERMIT_PIC = Config.PMPERMIT_PIC
DEFAULTUSER = str(
    ALIVE_NAME) if ALIVE_NAME else "**Henüz bir isim belirlenmedi nibba, sabitlenmiş mesajı kontrol et** @EfsaneUserBot"
USER_BOT_WARN_ZERO = "`Ustamın gelen kutusuna spam gönderiyordunuz, bundan böyle ustamın EfsaneUserbotu tarafından engelleniyorsunuz.` **Şimdi Önemli bir işim olabilir** "

if Var.PRIVATE_GROUP_ID is not None:
    @borg.on(admin_cmd(pattern="approve ?(.*)"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        reason = event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id in PM_WARNS:
                    del PM_WARNS[chat.id]
                if chat.id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[chat.id].delete()
                    del PREV_REPLY_MESSAGE[chat.id]
                pmpermit_sql.approve(chat.id, reason)
                await event.edit("Pm için onaylandı [{}](tg://user?id={})".format(firstname, chat.id))
                await asyncio.sleep(3)
                await event.delete()

    @bot.on(events.NewMessage(outgoing=True))
    async def you_dm_niqq(event):
        if event.fwd_from:
            return
        chat = await event.get_chat()
        if event.is_private:
            if not pmpermit_sql.is_approved(chat.id):
                if chat.id not in PM_WARNS:
                    pmpermit_sql.approve(chat.id, "outgoing")

    @borg.on(admin_cmd(pattern="disapprove ?(.*)"))
    async def disapprove_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit("disapproved to pm [{}](tg://user?id={})".format(firstname, chat.id))

    @borg.on(admin_cmd(pattern="block ?(.*)"))
    async def block_p_m(event):
        if event.fwd_from:
            return
        replied_user = await event.client(GetFullUserRequest(event.chat_id))
        firstname = replied_user.user.first_name
        event.pattern_match.group(1)
        chat = await event.get_chat()
        if event.is_private:
            if pmpermit_sql.is_approved(chat.id):
                pmpermit_sql.disapprove(chat.id)
                await event.edit(
                    " ███████▄▄███████████▄  \n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓█░░░░░░░░░░░░░░█\n▓▓▓▓▓▓███░░░░░░░░░░░░█\n██████▀▀▀█░░░░██████▀  \n░░░░░░░░░█░░░░█  \n░░░░░░░░░░█░░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░█░░█  \n░░░░░░░░░░░░▀▀ \n\nYou are blocked. Now You Can't Message Me..[{}](tg://user?id={})".format(
                        firstname, chat.id
                    )
                )
                await asyncio.sleep(3)
                await event.client(functions.contacts.BlockRequest(chat.id))

    @borg.on(admin_cmd(pattern="listapproved$"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pmpermit_sql.get_all_approved()
        APPROVED_PMs = "Geçerli Onaylanmış PMler\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
        else:
            APPROVED_PMs = "Onaylanmış PM yok (henüz)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.client.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Mevcut Onaylanmış PM'ler",
                    reply_to=event
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @bot.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if event.from_id == bot.uid:
            return
        if Var.PRIVATE_GROUP_ID is None:
            return
        if not event.is_private:
            return
        message_text = event.message.message
        chat_id = event.from_id
        exelonid = chat_id
        message_text.lower()
        USER_BOT_NO_WARN = (
            f"[──▄█▀█▄─────────██ \n▄████████▄───▄▀█▄▄▄▄ \n██▀▼▼▼▼▼─▄▀──█▄▄ \n█████▄▲▲▲─▄▄▄▀───▀▄ \n██████▀▀▀▀─▀────────▀▀](tg://user?id={exelonid})\n\n"
            "Bu, efsane güvenlik hizmetinden otomatik olarak oluşturulan bir mesajdır\n\n"
            f"Merhaba dostum ustam {DEFAULTUSER} henüz sizi onaylamadı. yani ,"
            "Adınızı, nedeninizi ve 10.000 $ 'ı bırakın ve umarım 2 ışıkyılı içinde yanıt alırsınız.\n\n"
            "**Gönder** `/start` ** Böylece ustam neden burada olduğuna karar verebilir.**")
        if USER_BOT_NO_WARN == message_text:
            # userbot's should not reply to other userbot's
            # https://core.telegram.org/bots/faq#why-doesn-39t-my-bot-see-messages-from-other-bots
            return
        if event.from_id in CACHE:
            sender = CACHE[event.from_id]
        else:
            sender = await bot.get_entity(event.from_id)
            CACHE[event.from_id] = sender
        if chat_id == bot.uid:
            # don't log Saved Messages
            return
        if sender.bot:
            # don't log bots
            return
        if sender.verified:
            # don't log verified accounts
            return
        if (len(event.raw_text) == 1):
            if check(event.raw_text):
                return
        if not pmpermit_sql.is_approved(chat_id):
            # pm permit
            await do_pm_permit_action(chat_id, event)

    async def do_pm_permit_action(chat_id, event):
        if chat_id not in PM_WARNS:
            PM_WARNS.update({chat_id: 0})
        if PM_WARNS[chat_id] == Config.MAX_FLOOD_IN_P_M_s:
            r = await event.reply(USER_BOT_WARN_ZERO)
            await asyncio.sleep(1)
            await event.client(functions.contacts.BlockRequest(chat_id))
            if chat_id in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_id].delete()
            PREV_REPLY_MESSAGE[chat_id] = r
            the_message = ""
            the_message += "#BLOCKED_PMs\n\n"
            the_message += f"[Kullanıcı](tg://user?id={chat_id}): {chat_id}\n"
            the_message += f"Mesaj Sayısı: {PM_WARNS[chat_id]}\n"
            # the_message += f"Media: {message_media}"
            try:
                await event.client.send_message(
                    entity=Var.PRIVATE_GROUP_ID,
                    message=the_message,
                    # reply_to=,
                    # parse_mode="html",
                    link_preview=False,
                    # file=message_media,
                    silent=True
                )
                return
            except BaseException:
                return
        exelonid = chat_id
        if PMPERMIT_PIC:
            if Config.CUSTOM_PMPERMIT_TEXT:
                USER_BOT_NO_WARN = (
                    Config.CUSTOM_PMPERMIT_TEXT +
                    '\n\n' +
                    "**Gönder** `/start` ** Böylece ustam neden burada olduğuna karar verebilir**")
            else:
                USER_BOT_NO_WARN = (
                    "Bu, exelon güvenlik hizmetinden otomatik olarak oluşturulan bir mesajdır\n\n"
                    f"Merhaba dostum ustam {DEFAULTUSER} henüz sizi onaylamadı. yani ,"
                    "Adınızı, nedeninizi ve 10.000 $ 'ı bırakın ve umarım 2 ışıkyılı içinde yanıt alırsınız.\n\n"
                    "**Gönder** `/start` ** Böylece ustam neden burada olduğuna karar verebilir.**")
            r = await event.reply(USER_BOT_NO_WARN, file=PMPERMIT_PIC)
        else:
            if Config.CUSTOM_PMPERMIT_TEXT:
                USER_BOT_NO_WARN = (
                    Config.CUSTOM_PMPERMIT_TEXT +
                    '\n\n' +
                    "**Gönder** `/start` ** Böylece ustam neden burada olduğuna karar verebilir.**")
            else:
                USER_BOT_NO_WARN = (
                    f"[──▄█▀█▄─────────██ \n▄████████▄───▄▀█▄▄▄▄ \n██▀▼▼▼▼▼─▄▀──█▄▄ \n█████▄▲▲▲─▄▄▄▀───▀▄ \n██████▀▀▀▀─▀────────▀▀](tg://user?id={exelonid})\n\n"
                    "Bu, efsane güvenlik hizmetinden otomatik olarak oluşturulan bir mesajdır\n\n"
                    f"Merhaba dostum ustam {DEFAULTUSER} henüz sizi onaylamadı. yani ,"
                    "Adınızı, nedeninizi ve 10.000 $ 'ı bırakın ve umarım 2 ışıkyılı içinde yanıt alırsınız.\n\n"
                    "**Gönder** `/start` ** Böylece ustam neden burada olduğuna karar verebilir.**")
            r = await event.reply(USER_BOT_NO_WARN)
        PM_WARNS[chat_id] += 1
        if chat_id in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_id].delete()
        PREV_REPLY_MESSAGE[chat_id] = r

CMD_HELP.update({
    "pmpermit":
    "**📌Komut ➥ **.approve\
\n**Kullanım ➥  ** Söz konusu / cevaplanan kişiyi PM'ye onaylar.\
**📌Komut ➥ **.disapprove\
\n**Kullanım ➥ ** Sözü edilen / yanıtlanan kişiyi PM'e reddeder.\
\n\n**📌Komut ➥ **.block\
\n**Kullanım ➥  **Kişiyi engeller.\
\n\n**📌Komut ➥ **.listapproved\
\n**Kullanım ➥  ** Onaylanan tüm kullanıcıları listelemek için.\
"
})
