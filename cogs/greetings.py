import discord
from discord.ext import commands


class Greetings(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author == self.bot.user:
            return
        if "hello" in message.content.lower():
            await message.channel.send(f"Hello, {message.author.mention}!")

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        """Greets new members and provides command info via DM."""
        user = member
        welcome_message = (f"Welcome {user.mention} to the {user.guild.name} server!\n\n"
                           f"Type `{self.bot.command_prefix}help` to see the available commands.\n"
                           f"The command prefix is `{self.bot.command_prefix}`.")

        try:
            await user.send(welcome_message)
        except discord.Forbidden:  # Unable to send DM
            pass

    @commands.command()
    async def ping(self, ctx):
        """Check the bot's latency."""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f"Pong! Latency: {latency}ms")

    @commands.command()
    async def greet(self, ctx, *, target: discord.Member = None):
        """Greet a specific member or the command invoker."""
        target = target or ctx.author
        await ctx.send(f"Hello, {target.mention}!")

    @commands.command()
    async def introduce(self, ctx):
        """Introduce the bot."""
        await ctx.send("Hi, I'm your friendly bot! Feel free to ask me anything.")

    @commands.command()
    async def goodbye(self, ctx):
        """Say goodbye."""
        await ctx.send("Goodbye! See you next time!")

    @commands.command()
    async def invite(self, ctx):
        """Get an invite link for the bot."""
        await ctx.send("Invite me to your server with this link: <invite_link>")



async def setup(bot):
    await bot.add_cog(Greetings(bot))
