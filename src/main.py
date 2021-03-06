import discord
import time

# Replace this with your bot's token
token = YourTokenHere

# For information on color please see color-info.txt
color = 0x3498db     
   
# If the bot's status should be set (configure below)
status_enabled = True

# Replace this with what you want your bot's status to be shown as
# This would set the bot's status to "Listening to !suggest"
bot_status = '!suggest'

 # Replace this with your suggestions channel id
suggestions_channel_id = YourSuggestionsChannelID

client = discord.Client()

@client.event
async def on_ready():
    print('The bot has logged in as {0.user}'.format(client)) 
    await set_status()
    
async def set_status():
  time.sleep(2)
  if status_enabled == True:
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=bot_status))

@client.event
async def on_message(message):
    suggestionData = '{}'.format(message.content).replace('!suggest', ' ')
    if message.author == client.user:
        return

    if message.content.startswith('!suggest'):
        embed=discord.Embed(title = 'New Suggestion!:')
        embed.add_field(name='Vote Below!', value=suggestionData, inline=True)
        channel=client.get_channel(suggestions_channel_id)
        embed.color=color
        embed.set_footer(text='Suggested by ' + message.author.name, icon_url=message.author.avatar_url)
        up_emoji = '\N{THUMBS UP SIGN}'
        down_emoji = '\N{THUMBS DOWN SIGN}'
        msg = await channel.send(embed=embed)
        await msg.add_reaction(up_emoji)
        await msg.add_reaction(down_emoji)
        await message.channel.send('Your suggestion has been submitted ' + '**' + message.author.name + '**')

client.run(token)

