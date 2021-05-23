import discord
        # Replace this with your bot's token
token = YourTokenHere
color = 0x3498db         # Replace this with your suggestions channel id
suggestions_channel_id = YourSuggestionsChannelID

client = discord.Client()

@client.event
async def on_ready():
    print('The bot has logged in as {0.user}'.format(client)) 

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

