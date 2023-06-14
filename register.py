@app.message("登録")
def select_date(say):
    send_message_from_json("JSON/register_date.json","C05A7G0ARB7")

@app.action("select_date")
def handle_register_hour(ack, body, say):
    global GLOBAL_DATE
    GLOBAL_DATE = body["actions"][0]["selected_date"]
    with open("selected_date.json", "w") as file:
        json.dump(GLOBAL_DATE, file)
        #say(GLOBAL_DATE)
    ack()
    global GLOBAL_YEAR, GLOBAL_MONTH, GLOBAL_DAY
    GLOBAL_YEAR, GLOBAL_MONTH, GLOBAL_DAY = GLOBAL_DATE.split("-")

@app.action("select_hour")
def handle_register_hour(ack, body, say):
    global GLOBAL_HOUR
    GLOBAL_HOUR = body["actions"][0]["selected_option"]["value"]
    with open("selected_date.json", "w") as file:
        json.dump(GLOBAL_HOUR, file)
        #say(GLOBAL_HOUR)
    ack()

@app.action("select_minute")
def handle_register_minute(ack, body, say):
    global GLOBAL_MINUTE
    GLOBAL_MINUTE = body["actions"][0]["selected_option"]["value"]
    with open("selected_date.json", "w") as file:
        json.dump(GLOBAL_MINUTE, file)
        #say(GLOBAL_MINUTE)
    ack()
    
@app.action("register_date")
def check_register_date(ack, body, say):
    global GLOBAL_YEAR, GLOBAL_MONTH, GLOBAL_DAY, GLOBAL_DAY, GLOBAL_HOUR, GLOBAL_MINUTE
    ack()
    message = f"あなたが登録したのは、{GLOBAL_YEAR}年{GLOBAL_MONTH}月{GLOBAL_DAY}日{GLOBAL_HOUR}時{GLOBAL_MINUTE}分です"
    say(message)