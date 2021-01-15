import discord
from discord.ext import commands
from helpers.books_helpers import book_search, author_book_search
from helpers.paginate import paginate

class Books(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief='search for a book')
    async def book(self, ctx, *, book_name):
        book = book_search(book_name)
        if book is None:
            await ctx.send('No book found.')
        else:
            embed = discord.Embed(title=book['title'], url=book['url'], description=book['description'])
            embed.set_author(name=book['author'])
            embed.set_thumbnail(url=book['image'])
            await ctx.send(embed=embed)

    @commands.command(brief='search for an author\'s top books')
    async def author(self, ctx, *, author_name):
        author_books_list = author_book_search(author_name)
        if author_books_list is None:
            await ctx.send(f'No book found by {author_name}.')
        else:
            # create list of embeds
            book_embeds_list = []
            for i in range(len(author_books_list)):
                book = author_books_list[i]
                embed = discord.Embed(title=f'{i+1}. {book["title"]}', url=book['url'], description=book['description'])
                embed.set_thumbnail(url=book['image'])
                book_embeds_list.append(embed)
            await ctx.send(f'Here are {author_name}\'s top {len(author_books_list)} books:')
            await paginate(ctx, self.bot, book_embeds_list, isEmbed=True)

def setup(bot):
    bot.add_cog(Books(bot))
    print('Books cog successfully added.')