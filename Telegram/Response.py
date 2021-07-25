from datetime import datetime


def sample_response(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "hey! how is ur day?"

    if user_message in ("good", "fine"):
        return "that's awesome man "

    if user_message in ("who are you", "who is this", "who are you?"):
        return "As it is my name,so i think that's enough"

    if user_message in ("how are you?", "how are you", "how is your day", "how was your day"):
        return "fine!...what about You?"

    if user_message in ("time", "date", "time?", "whats the time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "i dont understand you "
