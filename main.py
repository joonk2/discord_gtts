from gtts import gTTS
import asyncio
import time
import discord
from discord.ext import commands     #discord.ext를 쓴다는 것은 discord.py를 쓴다는 뜻이다.
from discord.utils import get
from discord import FFmpegPCMAudio
import os


# pip install gTTS하고 버젼을 바꾸고싶다? ---> pip install gTTS==1.1.4

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('login: ')
    print(bot.user.name)
    print('gtts')
    await bot.change_presence(status=discord.Status.online, activity=None)

@bot.command(name="gtts")
async def play_tts(ctx, *, text):
    if os.path.exists(f'voice.mp3'): 
       os.remove(f'voice.mp3') 
    print("소리")
    global vc
    vc = get(bot.voice_clients, guild=ctx.guild) 
    print(text)
    if not vc:        
        vc = await ctx.author.voice.channel.connect() 
                                                              
                                                                          
    language = "en" if text.replace(" ", "").encode().isalpha() else "ko"  # encode 한국어가 외계어로 나오는거 방지
    print(language) #이거 있어도되고 없어도됨                              # isalpha = 이게 알파벳인가 아닌가?  즉 알파벳이면 true가 되서
    tts = gTTS(text=str(text), lang=str(language), slow=False, tld='co.uk')           #en이 되고 아니면 ko가 됨
                                                                         #str은 문자열로 바꿔줌  # 애초에 명령어를문자열로 받아옴
    tts.save('voice.mp3')                                      
                                                                        # replace(" ", "")  띄워쓰기를 없애줌 쉽게설명은 밑에
    vc.play(discord.FFmpegPCMAudio('voice.mp3'), after=None)            #1 isalpha()가 모든 문자열에 하나 하나 이게 알파벳인지 대조하는건데
                                                                        #2 띄워쓰기는 알파벳이 아니니까 한국어로 판명이 된다
                                                                        #3 즉  language 값에서만 잠시 스페이스를 없앤 것이다.
    embed = discord.Embed(title=f"{ctx.author.name} 📢", description=text, color=discord.Color.dark_gray())
    await ctx.send(embed=embed)




@bot.command(name="leave", description="leaving voice channel")
#async def quit_tts(self, ctx, *args):
async def quit_tts(ctx, *args):

    global vc
    vc = get(bot.voice_clients, guild=ctx.guild)

    voice = ctx.voice_client
    if voice.is_connected():
        await voice.disconnect()
        embed = discord.Embed(title='"', description='"'
        ,color=discord.Color.blue)
        await ctx.send(embed=embed)

bot.run('MTE4ODI4NDk5Nzg1NDA0NDI0Mg.G28iKw.pjqpiFkGSAKecdzIVd1qgdKDdPztBEY9N6N7uU')


