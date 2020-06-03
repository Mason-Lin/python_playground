import click

# argument


@click.command()
@click.option('--count', default=1, help='number of greetings')
@click.argument('name')
def hello(count, name):
    for x in range(count):
        click.echo('Hello %s!' % name)

# required


@click.command()
@click.option('-t', '--to', 'to', help='To who', required=True)
def greeting(to):
    '''Say hello to someone required'''
    print(f'Hello, {to or "stranger"}!')

# group, great!


@click.group()
def cli():
    pass


@cli.command()
def initdb():
    click.echo('Initialized the database')


@cli.command()
def dropdb():
    click.echo('Dropped the database')

# file


@click.command()
@click.argument('f', type=click.File())
def cat(f):
    click.echo(f.read())

# prompt, I like it!


@click.command()
@click.option('--name', prompt=True)
def prompt(name):
    click.echo(f'your name={name}')


if __name__ == '__main__':
    # hello()
    # greeting()
    # cli()
    # cat()
    prompt()
