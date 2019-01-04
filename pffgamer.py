import random
import discord
import asyncio
import requests
import json
import time
import datetime
import safygiphy
import os
from random import randint

g = safygiphy.Giphy()
start_time = {"start_time1": time.time()}
COR = 0xc017b6


client = discord.Client()


cor = {'000000000000000000': {'color': '0x00000'}}



@client.event
async def on_ready():
    print(client.user.name)
    print('Logged in as ---->', client.user)
    print('ID:', client.user.id)
    print("Servidores: {} Serves".format(str(len(client.servers))))
    while True:
        await client.change_presence(game=discord.Game(name="{} Usuários 💜".format(str(len(set(client.get_all_members())))), type=1, url='https://www.twitch.tv/robertinhapfaff'), status='streaming')
        await asyncio.sleep(20)

        await client.change_presence(game=discord.Game(name="Vamos conversar? Live no streamcraft 💌", type=1,url='https://www.twitch.tv/robertinhapfaff'), status='streaming')
        await asyncio.sleep(40)

        await client.change_presence(game=discord.Game(name="Oi Gente , Oi Gente ,Oiiii Genteeeee 💋", type=1,url='https://www.twitch.tv/robertinhapfaff'), status='streaming')
        await asyncio.sleep(50)


@client.event
async def on_message(message):
    if message.content.startswith('pf!membros'):
        # Importar time e datetime
        user = message.author.name
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        membros_embed = discord.Embed(title="\n", description="Quantidade De Membros No Servidor!", color=COR)
        membros_embed.set_thumbnail(url=message.server.icon_url)
        membros_embed.set_footer(text="Comando requisitado por {} Hoje as {}".format(user, horario))
        membros_embed.add_field(name="Membros no servidor:", value=len(message.server.members), inline=True)
        await client.send_message(message.channel, embed=membros_embed)
    
    
    
    
    if message.content.lower().startswith('pf!msg'):
     if message.author.server_permissions.administrator:
        msg = message.content.strip('pf!msg')
        embed2 = discord.Embed(title='📌 Mensagem sendo enviada...', description='`Mensagem escolhida`\n' + (msg),color=COR)
        await client.delete_message(message)
        await client.send_message(message.channel, embed=embed2)
        x = list(message.server.members)
        s = 0
        for member in x:
            user = message.author.name
            horario = datetime.datetime.now().strftime("%H:%M:%S")
            embed1 = discord.Embed(title="💜 PFAFFGAMER 💜", url="", color=COR,description='**Mensagem nova para você 💌**\n<@{}> \n\n**Aviso:🍧**\n\n**{}**\n'.format(member.id, msg))
            embed1.set_image(url="https://cdn.discordapp.com/attachments/505165436464267295/530184598580363266/Roberta_2.png")
            embed1.set_thumbnail(url="https://cdn.discordapp.com/attachments/505165436464267295/530184598580363266/Roberta_2.png")
            embed1.set_footer(text="Enviado por --> {} • Hoje às {}".format(user, horario))
            try:
                await client.send_message(member, embed=embed1)
                print(member.name)
                s += 1
            except:
                pass
        print('\nAviso enviado para {} membros de {}'.format(s, len(x)))
        embed2 = discord.Embed(title='Concluido', color=COR,description='\nAviso enviado para **{}** de **{}**'.format(s, len(x)))
        embed2.set_footer(text=message.server.name, icon_url=message.server.icon_url)
        await client.send_message(message.channel, embed=embed2)

        
        
        
        

    if message.content.lower().startswith('pf!inforuser'):
        user = message.author
        embedinfo = discord.Embed(title='**Suas informações:**', color=COR, description='\n')
        embedinfo.set_thumbnail(url=user.avatar_url)
        embedinfo.add_field(name='<:page_facing_up:443039280890118155>Nome', value=user.name)
        embedinfo.add_field(name='<:satellite:443039280999432202>Id usuario', value=user.id)
        embedinfo.add_field(name='<:inbox_tray:443039280852631552>Entrou em',value=user.joined_at.strftime("%d %b %Y %H:%M"))
        embedinfo.add_field(name='<:video_game:475429382211502127>Jogando', value=user.game)
        await client.send_message(message.channel, embed=embedinfo)

    if not (not message.content.startswith('pf!fale') and not message.content.startswith('pf!falar')):
        if message.author.id == 'ID DO BOT':
            return
        try:
            mensagem = message.content[7:]
            await client.delete_message(message)
            await client.send_message(message.channel, mensagem, tts=False)
            print('Fale on')
            print(mensagem)
        except:
            await client.send_message(message.channel, "Você precisa escrever algo para eu falar!")


    if message.content.startswith('pf!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(str(rgif.get("data", {}).get('image_original_url')), stream=True)
        await client.send_message(message.channel, '<:frame_photo:462594078899568651>')
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    if message.content.startswith('pf!server'):
        serverinfo_embed = discord.Embed(color=COR)
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)
        serverinfo_embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        serverinfo_embed.add_field(name="Nome", value=message.server.name, inline=True)
        serverinfo_embed.add_field(name="Dono", value=message.server.owner.mention)
        serverinfo_embed.add_field(name="ID", value=message.server.id, inline=True)
        serverinfo_embed.add_field(name="Cargos", value=len(message.server.roles),inline=True)
        serverinfo_embed.add_field(name="Membros", value=len(message.server.members),inline=True)
        serverinfo_embed.add_field(name="Criado em:",value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        serverinfo_embed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
        await client.send_message(message.channel, embed=serverinfo_embed)

    if message.content.lower().startswith('pf!clima'):
        s = message.content.strip('.pf!')
        url = 'http://api.apixu.com/v1/current.json?key=7fa4b4027a2349e8b44114046182304&q=' + s
        r = requests.get(url)
        if r.status_code == 200:
            js = r.json()
            nome = js['location']['name']
            regiao = js['location']['region']
            pais = js['location']['country']

            temp = str(js['current']['temp_c']) + "°C"
            temp2 = str(js['current']['temp_f']) + "\n°F"
            tenp = str(js['current']['feelslike_c']) + "°C"
            tenp2 = str(js['current']['feelslike_f']) + "\n°F"

            umi = str(js['current']['humidity']) + "%"
            vento = str(js['current']['wind_kph']) + "km/h"
            chuva = str(js['current']['precip_mm'])
            nuvem = str(js['current']['cloud'])
        try:
            clima = discord.Embed(color=COR)
            clima.add_field(name='Cidade', value=nome, inline=True)
            clima.add_field(name='Região', value=regiao, inline=True)
            clima.add_field(name='Pais', value=pais, inline=True)
            clima.add_field(name='Temperatura', value=temp + temp2, inline=True)
            clima.add_field(name='Sensação termica', value=tenp + tenp2,inline=True)
            clima.add_field(name='Umidade', value=umi, inline=True)
            clima.add_field(name=' Chuva', value=chuva, inline=True)
            clima.add_field(name='Nuvem', value=nuvem, inline=True)
            clima.add_field(name='Vento', value=vento, inline=True)
            clima.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=clima)
        except UnboundLocalError:
            await client.send_message(message.channel,'`Infelizmente está cidade não é existente`')






    elif message.content.lower().startswith('pf!avatar'):
        try:
            membro = message.mentions[0]
            avatarembed = discord.Embed(title="", color=COR, description="[Clique aqui para baixar a imagem](" + membro.avatar_url + ")")
            avatarembed.set_author(name=membro.name)
            avatarembed.set_image(url=membro.avatar_url)
            avatarembed.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, f"{message.author.mention}", embed=avatarembed)
        except:
            avatarembed2 = discord.Embed(title="", color=COR, description="[Clique aqui para baixar a imagem](" + message.author.avatar_url + ")")
            avatarembed2.set_author(name=message.author.name)
            avatarembed2.set_image(url=message.author.avatar_url)
            avatarembed2.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, f"{message.author.mention}", embed=avatarembed2)


    if message.content.lower().startswith('pf!memoria'):
        await client.delete_message(message)
        emb = discord.Embed(title='Processando...', color=COR)
        random = randint(0, 9)
        string = str(random)
        pingm0 = await client.send_message(message.channel, embed=emb)
        pingm1 = discord.Embed(title='Memória utilizada pelo bot:',description='`64{}Gb`'.format(string), color=COR)
        await client.edit_message(pingm0, embed=pingm1)


    if message.content.lower().startswith('pf!servidor'):
        try:
            servidor = message.server
            criado_em = str(servidor.created_at.strftime("%d/%m/20%y - %H:%M:%S"))
            cargos = len([y.id for y in servidor.role_hierarchy])
            informacao = "\n:writing_hand::skin-tone-1: Nome : " + str(servidor.name) + " " + "\n:briefcase: Id : " + str(servidor.id) + " ""\n:tophat: Dono : " + str(servidor.owner) + " \n:alarm_clock: Criado em : " + str(criado_em) + " "
            emojis = len([y.id for y in servidor.emojis])
            cargos = len([y.id for y in servidor.role_hierarchy])
            verificao = str(servidor.verification_level).replace("low", "Baixa").replace("medium", "MÃ©dia").replace("high", "Alta").replace("4", "Super Alta").replace("none", "Nenhuma")
            localizacao = str(servidor.region).title()
            informacao_add = "\n:sunglasses:  " + str(emojis) + " Emojis" + "\n:robot:  " + str(cargos) + " Cargos" + "\n:bookmark_tabs: VerificaÃ§Ã£o : " + str(verificao) + " " + "\n:earth_americas: LocalizaÃ§Ã£o : " + str(localizacao) + " "
            bots = len([y.id for y in servidor.members if y.bot])
            humanos = len([y.id for y in servidor.members if not y.bot])
            usuario_total = bots + humanos
            usuarios = "\n:robot: " + str(bots) + " Bots\n:bust_in_silhouette: " + str(humanos) + " Humanos"
            servidor = message.server
            online = len([y.id for y in servidor.members if y.status == discord.Status.online])
            afk = len([y.id for y in servidor.members if y.status == y.status == discord.Status.idle])
            offline = len([y.id for y in servidor.members if y.status == y.status == discord.Status.offline])
            dnd = len([y.id for y in servidor.members if y.status == y.status == discord.Status.dnd])
            status_usuarios = "\n:green_heart: " + str(online) + " Online \n:yellow_heart:  " + str(afk) + " Ausente \n:heart: " + str(dnd) + " NÃ£o Pertube \n:white_circle:  " + str(offline) + " Offline"
            texto = len([y.id for y in servidor.channels if y.type == discord.ChannelType.text])
            voz = len([y.id for y in servidor.channels if y.type == discord.ChannelType.voice])
            if texto > 0:
                text = 1
            else:
                text = 0
            if voz > 0:
                voice = 1
            else:
                voice = 0
            categoria = voice + text
            canais = "\n:books: " + str(categoria) + " Categoria\n:scroll: " + str(
                texto) + " Texto\n:loud_sound: " + str(voz) + " voz"
            canais_total = texto + voz
            if servidor.icon_url == "":
                img = "https://ethospsicotestes.com.br/images/sem_foto.png"
            else:
                img = servidor.icon_url
            embed = discord.Embed(colour=COR)
            embed.add_field(name="Informações ", value=informacao, inline=True)
            embed.add_field(name="Usuários [" + str(usuario_total) + "]", value=usuarios, inline=True)
            embed.add_field(name="Canais [" + str(canais_total) + "]", value=canais, inline=True)
            embed.add_field(name="Status do usuários", value=status_usuarios, inline=True)
            embed.add_field(name="Informações Adicional", value=informacao_add, inline=True)
            embed.set_thumbnail(url=img)

            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "Erro ao obter a Informações do servidor!")

    if message.content.lower().startswith('pf!nick'):
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, 'Você não tem permissão')
        try:
            user = message.mentions[0]
            msg = str(message.content[26:]).replace('<', '').replace('>', '').replace('@', '').replace(user.id, '')
            embed1 = discord.Embed(title='Nick Mudado Com Sucesso...', color=COR)
            await client.change_nickname(user, msg)
            await client.send_message(message.channel, embed=embed1)
        except IndexError:

            await client.send_message(message.channel, 'Especifique O Nome Do Usuário')



    if message.content.startswith('pf!clear'):
        try:
         await client.delete_message(message)
        except:
         pass
        if not message.author.server_permissions.manage_messages:
            embed = discord.Embed(color=COR, description="Sem Permissão Para Limpar Chat, Só Mods Ou Adms Podem Usar Isso!")
            embed.set_footer(text=message.author.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed)
        if message.author.server_permissions.manage_messages:
            try:
                lim = int(message.content[8:])
                await client.purge_from(message.channel, limit=lim)
                embed = discord.Embed(color=COR,description="`{}` mensagens deletadas com sucesso por {}".format(lim, message.author.mention))
                embed.set_footer(text=message.author.name, icon_url=client.user.avatar_url)
                await client.send_message(message.channel, embed=embed)
            except:
              pass    


@client.event
async def on_member_join(member):
    role1 = "Inscrito(a)"
    role = discord.utils.find(lambda r: r.name == "{}".format(role1), member.server.roles )
    await client.add_roles(member, role)
    embedvindo = discord.Embed(color=color, title='\n',description='\n' + member.mention + '\n• **Seja Bem vindo ao servidor da PFAFFGAMER**\n\n**• Link do canal da Streamcraft**\n\n**https://streamcraft.com/user/2015336440**\n\n**• Link do canal do Youtube**\n\n**https://www.youtube.com/user/Pfaffgamer**')
    embedvindo.set_thumbnail(url=member.avatar_url)
    embedvindo.set_image(url="https://cdn.discordapp.com/attachments/499686934700883981/513021860259299329/bem_vindo_robertaaaa.png")
    embedvindo.set_author(name=member.name, icon_url=member.avatar_url)
    embedvindo.set_footer(text=member.name, icon_url=member.avatar_url)
    embedvindo.timestamp = datetime.datetime.utcnow()
    mensagemvindo2 = "🚪bem-vindos🚪"
    bemvindo = discord.utils.find(lambda c: c.name == "{}".format(mensagemvindo2), member.server.channels )
    await client.send_message(bemvindo, embed=embedvindo)



client.run(str(os.environ.get('TOKEN')))
