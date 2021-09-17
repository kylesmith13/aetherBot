FROM gorialis/discord.py:3.9-alpine

RUN pip install web3

WORKDIR /app
COPY . .

CMD [ "python3", "bot.py"]