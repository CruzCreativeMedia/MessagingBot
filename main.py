import slack
import os
import schedule
import time

client=slack.WebClient(token=os.environ['slack_token'])

def messageMe():
  print ("done")
  client.chat_postMessage(channel="dev-slack-apps",text="Hey! Agata I like you")

schedule.every().sunday.at("19:48").do(messageMe)
print('Script is Run')

while True:
  schedule.run_pending()
  time.sleep(10)