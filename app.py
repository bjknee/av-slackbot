import os
from slack_bolt import App
import recipe
from datetime import datetime
import pandas as pd
import slack_tokens

# GETS SLACK CREDENTIALS
token = slack_tokens.get_slack_tokens()
SLACK_BOT_TOKEN = token[0]
SLACK_SIGNING_SECRET = token[1]



# Initializes your app with your bot token and signing secret
app = App(
    token=SLACK_BOT_TOKEN,
    signing_secret=SLACK_SIGNING_SECRET
)

@app.command("/bluejolly")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(recipe.bluejolly['name'] + " " + recipe.bluejolly['size'])
    for i in recipe.bluejolly['ingredients']:
        say(i['brand'] + " " + i['flavor'] + " " + str(i['quantity']))
    say("              ")
    say("Do you want to confirm this base? If so type /yes")
    user_id = command['user_name']
    update = updateInventory(recipe.envy)
    if update:
        updateBaseHistory(user_id, recipe.bluejolly['name'])

@app.command("/berryblast")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(recipe.berryblast['name'] + " " + recipe.berryblast['size'])
    for i in recipe.berryblast['ingredients']:
        say(i['brand'] + " " + i['flavor'] + " " + str(i['quantity']))
    say("              ")
    say("Do you want to confirm this base? If so type /yes")
    user_id = command['user_name']
    update = updateInventory(recipe.berryblast)
    if update:
        updateBaseHistory(user_id, recipe.berryblast['name'])

@app.command("/banana_ice")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(recipe.banana_ice['name'] + " " + recipe.banana_ice['size'])
    for i in recipe.banana_ice['ingredients']:
        say(i['brand'] + " " + i['flavor'] + " " + str(i['quantity']))
    say("              ")
    say("Do you want to confirm this base? If so type /yes")
    user_id = command['user_name']
    update = updateInventory(recipe.banana_ice)
    if update:
        updateBaseHistory(user_id, recipe.banana_ice['name'])

@app.command("/dads_blend")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(recipe.dads_blend['name'] + " " + recipe.dads_blend['size'])
    for i in recipe.dads_blend['ingredients']:
        say(i['brand'] + " " + i['flavor'] + " " + str(i['quantity']))
    say("              ")
    say("Do you want to confirm this base? If so type /yes")
    user_id = command['user_name']
    update = updateInventory(recipe.dads_blend)
    if update:
        updateBaseHistory(user_id, recipe.dads_blend['name'])

@app.command("/envy")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(recipe.envy['name'] + " " + recipe.envy['size'])
    for i in recipe.envy['ingredients']:
        say(i['brand'] + " " + i['flavor'] + " " + str(i['quantity']))
    say("              ")
    say("Do you want to confirm this base? If so type /yes")
    user_id = command['user_name']
    update = updateInventory(recipe.envy)
    if update:
        updateBaseHistory(user_id, recipe.envy['name'])

@app.command("/wadu")
def repeat_text(ack, say, command):
    # Acknowledge command request
    ack()
    say(recipe.wadu['name'] + " " + recipe.wadu['size'])
    for i in recipe.wadu['ingredients']:
        say(i['brand'] + " " + i['flavor'] + " " + str(i['quantity']))
    say("              ")
    say("Do you want to confirm this base? If so type /yes")
    user_id = command['user_name']
    update = updateInventory(recipe.wadu)
    if update:
        updateBaseHistory(user_id, recipe.wadu['name'])

def updateInventory(recipe):
    @app.command("/yes")
    def confirm_base(ack, say, command):
        ack()
        data = pd.read_excel('flavors.xlsx')
        df = pd.DataFrame(data)
        for i in recipe['ingredients']:
            for x in df.index:
                if df.loc[x, "Flavor"] == i['flavor'] and df.loc[x, "Brand"] == i['brand']:
                    df.loc[x, "Quantity"] = df.loc[x, "Quantity"] - i['quantity']
        df.to_excel('flavors.xlsx', index=False)
        say("Inventory updated")
        say("              ")


def updateBaseHistory(user, basename):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    input = basename + " Created on: " + dt_string + " by " + user
    f = open("base_history.txt", "a")
    f.write(str(input)+"\n")
    f.close()

# Start your app
if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))

