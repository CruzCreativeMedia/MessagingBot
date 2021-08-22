import slack
import os
import schedule
import time

client=slack.WebClient(token=os.environ['slack_token'])

def messageMe():
  print ("done")
  client.chat_postMessage(channel="dev-slack-apps",text="Hello World!")

schedule.every().sunday.at("20:00").do(messageMe)
print('Script is Run')

while True:
  schedule.run_pending()
  time.sleep(10)