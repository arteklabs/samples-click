import click

profiles = {
    'd': 'dev',
    't': 'test',
    'p': 'prod',
}

@click.command()
@click.option("-a", "--action", prompt="enter your profile action", help="login")
@click.argument('profile', type=click.Choice(profiles.keys()), default='d')
@click.argument('requirements', type=click.Path(exists=False), required=0)
@click.argument('requirement', required=0)
def test(action, profile, requirement, requirements):
    """_summary_

    .. code:: python

       $ python app.py test requirements.txt test
       enter your profile action: del
       performing action 'del'
       selecting profile 'dev'

    :param action: _description_
    :type action: _type_
    :param profile: _description_
    :type profile: _type_
    :param requirement: _description_
    :type requirement: _type_
    :param requirements: _description_
    :type requirements: _type_
    """
    click.echo(f"performing action '{action}'")
    click.echo(f"selecting profile '{profiles[profile]}'")
    if requirements and requirement:
        with open(requirements,'a+') as file:
            file.write(requirement)

@click.group()
def cmds():
    pass

cmds.add_command(test)

if __name__ == '__main__':
    cmds()
