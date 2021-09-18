import config
import discord
from discord.ext import commands
import aetherProp

bot = commands.Bot(command_prefix=".")

@bot.command()
async def propertyInfo(ctx, propertyId, progress):
    propId = int(propertyId)
    prog = int(progress)

    embedObj = discord.Embed(color=0x00ff00)
    embedObj.set_footer(text=config.footer)
    if prog > 100 or prog < 15:
        embedObj.title = 'Error'
        embedObj.add_field(name='Message', value='Progress needs to be between 15 and 100!')
    elif propId < 16 or propId > 119:
        embedObj.title = 'Error'
        embedObj.add_field(name='Message', value='Currently property values are between 16-119, try again with one of these numbers!')
    else:
        data = aetherProp.computeInfo(propId, prog)
        rooms = round(data['rooms'])
        floors = round(data['floors'])
        embedObj.title = 'Property #' + propertyId + ' Info'
        embedObj.add_field(name='Floors', value=str(floors))
        embedObj.add_field(name='Rooms', value=str(rooms))
    
    await ctx.channel.send(embed=embedObj)

bot.run(config.token)

# handle messages for !propertyRoomCount and !propertyFloorCount
# propertyRoomCount will be the dimensions of the property (2x4) * (floorCount - 1)