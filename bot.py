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
    data = aetherProp.computeInfo(int(propertyId), int(progress))
    rooms = round(data[''])
    response = "Property " + str(propertyId) + " will have " + str(rooms) + " rooms at progress " + progress + "."
    await ctx.channel.send(response)

# @bot.command()
# async def propertyInfo(ctx):
#     await ctx.channel.send("This function requires two parameters: propertyId and progress")

# @bot.command()
# async def propertyInfo(ctx, arg):
#     await ctx.channel.send("This function requires two parameters: propertyId and progress")

@bot.command()
async def propertyInfo(ctx, propertyId, progress):
    propId = int(propertyId)
    prog = int(progress)

    response = ''
    if prog > 100 or prog < 0:
        response = 'Progress needs to be between 0 and 100!'
    elif propId < 17 or propId > 119:
        response = 'Currently property values are between 17-119, try again with one of these numbers!'
    else:
        data = aetherProp.computeInfo(propId, prog)
        rooms = round(data['rooms'])
        floors = round(data['floors'])
        response = "Property Number: " + propertyId + "\nProgress: " + progress + "\nFloor Count: " + str(floors) + "\nRoom Count: " + str(rooms)
    await ctx.channel.send(response)

bot.run(config.token)

# handle messages for !propertyRoomCount and !propertyFloorCount
# propertyRoomCount will be the dimensions of the property (2x4) * (floorCount - 1)