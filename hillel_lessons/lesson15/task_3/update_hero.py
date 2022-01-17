from configparser import ConfigParser

file = 'hero.ini'
config = ConfigParser()
config.read(file)


def update_hero(hero=config['Hero stats']['hero'],
                power=config['Hero stats']['power'],
                alive=config['Hero stats']['alive'],
                speed=config['Hero stats']['speed'],
                x=config['Hero stats']['x'],
                y=config['Hero stats']['y']):

    config.set('Hero stats', 'hero', hero)
    config.set('Hero stats', 'power', power)
    config.set('Hero stats', 'alive', alive)
    config.set('Hero stats', 'speed', speed)
    config.set('Hero stats', 'x', x)
    config.set('Hero stats', 'y', y)

    with open(file, 'w') as configfile:
        config.write(configfile)


update_hero(hero="Halk", power='450', y='2.3')
