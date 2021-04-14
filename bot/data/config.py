from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")

DATABASE_PATH = env.str("DATABASE_PATH")

DATABASES = {
    'sqlite3': {
        'driver': 'sqlite',
        'database': DATABASE_PATH,
        'foreign_keys': True
    }
}





