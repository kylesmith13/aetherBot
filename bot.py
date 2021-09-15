import config
from discord.ext import commands
import aetherProp

bot = commands.Bot(command_prefix="$")

@bot.command()
async def propertyFloorCount(ctx, propertyId, progress):
    floors = round(aetherProp.computeHeight(int(propertyId), int(progress)))
    response = "Property " + str(propertyId) + " will have " + str(floors) + " floors at progress " + progress + "."
    await ctx.channel.send(response)

@bot.command()
async def propertyRoomCount(ctx, propertyId, progress):
    rooms = round(aetherProp.computeRooms(int(propertyId), int(progress)))
    response = "Property " + str(propertyId) + " will have " + str(rooms) + " rooms at progress " + progress + "."
    await ctx.channel.send(response)

bot.run(config.token)

# handle messages for !propertyRoomCount and !propertyFloorCount
# propertyRoomCount will be the dimensions of the property (2x4) * (floorCount - 1)