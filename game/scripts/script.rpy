## Council of Chalcedon - Main Entry Point

label main_menu:
    return

label start:
    # Initialize progress tracking
    $ persistent.sessions_viewed = set() if persistent.sessions_viewed is None else persistent.sessions_viewed
    $ persistent.canons_read = set() if persistent.canons_read is None else persistent.canons_read

    jump prologue

label after_session(session_num):
    $ persistent.sessions_viewed.add(session_num)
    return
