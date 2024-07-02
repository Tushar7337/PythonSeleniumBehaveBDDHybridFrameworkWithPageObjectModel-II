from datetime import datetime

def current_timestamp():
    unique = datetime.now().strftime("%d-%m-%Y_%H_%M_%S")
    return unique