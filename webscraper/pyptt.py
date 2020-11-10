from PyPtt import PTT
ptt_bot = PTT.API(host=PTT.data_type.host_type.PTT2)
post_info = ptt_bot.get_post('Python', post_index=7486)
