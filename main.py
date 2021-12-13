import mido

with mido.open_input("W-49C 0") as kb:
    c = 100
    on = 0
    off = 0
    while 1:
        msg_type = kb.receive().type
        if msg_type == "note_on":
            on += 1
        elif msg_type == "note_off":
            off += 1
            print("{} : [on = {}], [off = {}], [diff = {}]".format(c, on, off, on - off))
        c -= 1