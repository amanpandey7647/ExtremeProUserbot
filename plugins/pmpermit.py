import asyncio
import io

from telethon import events, functions
from telethon.tl.functions.users import GetFullUserRequest
from Extre.utils import *
import os
from sql_helper import pmpermit_sql as pm_sql
Config.INSTANT_BLOCK = os.environ.get("INSTANT_BLOCK", None)
from plugins import *
Config.CUSTOM_PMPERMIT = os.environ.get("COUSTOMPM", None)
# I Have Taken Permisson To Import Pmpermit, Inline, Help from Eiva
# Userbot To Andencento. from Owner Shivansh Proof -
# https://telegra.ph/file/692c46d42e8021ddb61fc.png

DEVLIST = ["1320929227"]

WARN_PIC = os.environ.get("PMPERMIT_PIC", None)
PM_WARNS = {}
PREV_REPLY_MESSAGE = {}
PM_ON_OFF = os.environ.get("PM_PERMIT", None) or "ENABLE"
Config.LOGGER_ID = os.environ.get("LOGGER_ID", None)
CSTM_PMP = (
    Config.CUSTOM_PMPERMIT
    or "**You Have Trespassed To My Master's PM!\n ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ᴘʀɪᴠᴀᴛᴇ ᴜʟᴛʀᴀ ꜱᴇᴄᴜʀɪᴛʏ ᴏꜰ ᴍʏ ᴍᴀꜱᴛᴇʀ .**"
)
Eiva_ZERO = "Go get some sleep retard. \n\n**Blocked !!**"
Eiva_FIRST = (
    "**🔥 ᴀɴᴅᴇɴᴄᴇɴᴛᴏ ᴘʀɪᴠᴀᴛᴇ ᴜʟᴛʀᴀ ꜱᴇᴄᴜʀɪᴛʏ ᴏꜰ ᴍʏ ᴍᴀꜱᴛᴇʀ 🔥**\n\nThis is to inform you that "
    "{} is currently unavailable.\nThis is an automated message.\n\n"
    "{}\n\n**Please Choose Why You Are Here!!**".format(Eiva_mention, CSTM_PMP)
)


@client.on(extremepro_cmd(pattern="block$"))
async def approve_p_m(event):
    if event.fwd_from:
        return
    if event.is_private:
        replied_user = await event.Andencento(
            GetFullUserRequest(await event.get_input_chat())
        )
        firstname = replied_user.user.first_name
        if str(event.chat_id) in DEVLIST:
            await event.edit("**I can't block my Devloper !!**")
            return
        if pm_sql.is_approved(event.chat_id):
            pm_sql.disapprove(event.chat_id)
        await event.edit(
            "Go Get Some Sleep Retard !! \n\n**Blocked** [{}](tg://user?id={})".format(
                firstname, event.chat_id
            )
        )
        await event.Andencento(functions.contacts.BlockRequest(event.chat_id))
    elif event.is_group:
        reply_s = await event.get_reply_message()
        if not reply_s:
            await eod(event, "Reply to someone to block them..")
            return
        replied_user = await event.Andencento(GetFullUserRequest(reply_s.sender_id))
        firstname = replied_user.user.first_name
        if str(reply_s.sender_id) in DEVLIST:
            await event.edit("**I can't Block My Devloper !!**")
            return
        if pm_sql.is_approved(event.chat_id):
            pm_sql.disapprove(event.chat_id)
        await event.edit(
            "Go fuck yourself !! \n\n**Blocked** [{}](tg://user?id={})".format(
                firstname, reply_s.sender_id
            )
        )
        await event.Andencento(functions.contacts.BlockRequest(reply_s.sender_id))
        await asyncio.sleep(3)
        await event.delete()


if PM_ON_OFF != "DISABLE":

    @client.on(events.NewMessage(outgoing=True))
    async def auto_approve_for_out_going(event):
        if event.fwd_from:
            return
        if not event.is_private:
            return
        chat_ids = event.chat_id
        sender = await event.Andencento(GetFullUserRequest(await event.get_input_chat()))
        sender.user.first_name
        if chat_ids == client.uid:
            return
        if sender.user.bot:
            return
        if sender.user.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if str(event.chat_id) in DEVLIST:
            return
        if not pm_sql.is_approved(event.chat_id):
            if event.chat_id not in PM_WARNS:
                pm_sql.approve(event.chat_id, "outgoing")

    @client.on(extremepro_cmd(pattern="(a|approve|allow)$"))
    async def approve(event):
        if event.fwd_from:
            return
        if event.is_private:
            replied_user = await event.Andencento(
                GetFullUserRequest(await event.get_input_chat())
            )
            firstname = replied_user.user.first_name
            if not pm_sql.is_approved(event.chat_id):
                if event.chat_id in PM_WARNS:
                    del PM_WARNS[event.chat_id]
                if event.chat_id in PREV_REPLY_MESSAGE:
                    await PREV_REPLY_MESSAGE[event.chat_id].delete()
                    del PREV_REPLY_MESSAGE[event.chat_id]
                pm_sql.approve(event.chat_id, "Approved")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(
                        firstname, event.chat_id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
            elif pm_sql.is_approved(event.chat_id):
                hel_ = await event.edit("Already In Approved List!!")
                await asyncio.sleep(3)
                await hel_.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit("Reply to someone to approve them !!")
                return
            if not pm_sql.is_approved(reply_s.sender_id):
                replied_user = await event.Andencento(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pm_sql.approve(reply_s.sender_id, "Approved")
                await event.edit(
                    "Approved to pm [{}](tg://user?id={})".format(
                        firstname, reply_s.sender_id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
            elif pm_sql.is_approved(reply_s.sender_id):
                await event.edit("User Already Approved !")
                await event.delete()

    @client.on(extremepro_cmd(pattern="(da|disapprove|disallow)$"))
    async def dapprove(event):
        if event.fwd_from:
            return
        if event.is_private:
            replied_user = await event.Andencento(
                GetFullUserRequest(await event.get_input_chat())
            )
            firstname = replied_user.user.first_name
            if str(event.chat_id) in DEVLIST:
                await event.edit(
                    "**Unable to disapprove this user. Seems like God !!**"
                )
                return
            if pm_sql.is_approved(event.chat_id):
                pm_sql.disapprove(event.chat_id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(
                        firstname, event.chat_id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pm_sql.is_approved(event.chat_id):
                led = await event.edit("I don't think he was approved !!")
                await asyncio.sleep(3)
                await led.delete()
        elif event.is_group:
            reply_s = await event.get_reply_message()
            if not reply_s:
                await event.edit("Reply to someone to Disapprove them !!")
                return
            if str(reply_s.sender_id) in DEVLIST:
                await event.edit(
                    "**Unable to disapprove this user. Seems like God !!**"
                )
                return
            if pm_sql.is_approved(reply_s.sender_id):
                replied_user = await event.Andencento(GetFullUserRequest(reply_s.sender_id))
                firstname = replied_user.user.first_name
                pm_sql.disapprove(reply_s.sender_id)
                await event.edit(
                    "Disapproved User [{}](tg://user?id={})".format(
                        firstname, reply_s.sender_id
                    )
                )
                await asyncio.sleep(3)
                await event.delete()
            elif not pm_sql.is_approved(reply_s.sender_id):
                await event.edit("Not even in my approved list.")
                await event.delete()

    @client.on(extremepro_cmd(pattern="listapproved$"))
    async def approve_p_m(event):
        if event.fwd_from:
            return
        approved_users = pm_sql.get_all_approved()
        APPROVED_PMs = "Current Approved PMs\n"
        if len(approved_users) > 0:
            for a_user in approved_users:
                if a_user.reason:
                    APPROVED_PMs += f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id}) for {a_user.reason}\n"
                else:
                    APPROVED_PMs += (
                        f"👉 [{a_user.chat_id}](tg://user?id={a_user.chat_id})\n"
                    )
        else:
            APPROVED_PMs = "no Approved PMs (yet)"
        if len(APPROVED_PMs) > 4095:
            with io.BytesIO(str.encode(APPROVED_PMs)) as out_file:
                out_file.name = "approved.pms.text"
                await event.Andencento.send_file(
                    event.chat_id,
                    out_file,
                    force_document=True,
                    allow_cache=False,
                    caption="Current Approved PMs",
                    reply_to=event,
                )
                await event.delete()
        else:
            await event.edit(APPROVED_PMs)

    @client.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        if not event.is_private:
            return
        if event.sender_id == client.uid:
            return
        if str(event.sender_id) in DEVLIST:
            return
        if Config.LOGGER_ID is None:
            await bot.send_message(
                client.uid, "Please Set `LOGGER_ID` For Working Of Pm Permit"
            )
            return
        message_text = event.message.raw_text
        chat_ids = event.sender_id
        if Eiva_FIRST == message_text:
            return
        sender = await event.Andencento.get_entity(await event.get_input_chat())
        if chat_ids == client.uid:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if PM_ON_OFF == "DISABLE":
            return
        if pm_sql.is_approved(chat_ids):
            return
        if not pm_sql.is_approved(chat_ids):
            await do_pm_permit_action(chat_ids, event)

    async def do_pm_permit_action(chat_ids, event):
        if chat_ids not in PM_WARNS:
            PM_WARNS.update({chat_ids: 0})
        if PM_WARNS[chat_ids] == Config.MAX_SPAM:
            r = await event.reply(Eiva_ZERO)
            await asyncio.sleep(3)
            await event.Andencento(functions.contacts.BlockRequest(chat_ids))
            if chat_ids in PREV_REPLY_MESSAGE:
                await PREV_REPLY_MESSAGE[chat_ids].delete()
            PREV_REPLY_MESSAGE[chat_ids] = r
            the_message = ""
            the_message += "#BLOCK\n\n"
            the_message += f"[User](tg://user?id={chat_ids}): {chat_ids}\n"
            the_message += f"Message Counts: {PM_WARNS[chat_ids]}\n"
            try:
                await bot.send_message(
                    entity=Config.LOGGER_ID,
                    message=the_message,
                    link_preview=False,
                    silent=True,
                )
                return
            except BaseException:
                pass

        botusername = Config.BOT_USERNAME
        tap = await bot.inline_query(botusername, "pm_warn")
        hel_ = await tap[0].click(event.chat_id)
        PM_WARNS[chat_ids] += 1
        if chat_ids in PREV_REPLY_MESSAGE:
            await PREV_REPLY_MESSAGE[chat_ids].delete()
        PREV_REPLY_MESSAGE[chat_ids] = hel_


NEEDIT = Config.INSTANT_BLOCK
if NEEDIT == "ENABLE":

    @client.on(events.NewMessage(incoming=True))
    async def on_new_private_message(event):
        event.message.message
        event.message.media
        event.message.id
        event.message.to_id
        chat_id = event.chat_id
        sender = await bot.get_entity(chat_id)
        if chat_id == client.uid:
            return
        if chat_id == 1432756163:
            return
        if sender.bot:
            return
        if sender.verified:
            return
        if not pmpermit_sql.is_approved(chat_id):
            await bot(functions.contacts.BlockRequest(chat_id))
CMD_HELP.update(
    {
        "pmsecurity": ".approve/.a\nUse - Approve PM\
        \n\n.disapprove/.da\nUse - DisApprove PM\
        \n\n.listapproved\nUse - Get all approved PMs.\
        \n\nSet var PMPERMIT_PIC for custom PMPic, CUSTOM_PMPERMIT for custom text, PMSECURITY <on/off> to enable/disable, INSTANT_BLOCK <on/off>.\
        \nGet help from @ANDENCENTO."
    }
)
