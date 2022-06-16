from functools import wraps
import heroku3
from bot import HEROKU_API_KEY, HEROKU_APP_NAME


def check_heroku(func):
    if HEROKU_API_KEY:
        heroku_client = heroku3.from_key(HEROKU_API_KEY)

    @wraps(func)
    async def heroku_cli(client, message):
        heroku_app = None
        if not heroku_client:
            await message.reply_text(
                "`Please Add HEROKU_API_KEY Key For This To Function To Work!`",
                parse_mode="markdown",
            )
        elif not HEROKU_APP_NAME:
            await message.reply_text(
                "`Please Add HEROKU_APP_NAME For This To Function To Work!`",
                parse_mode="markdown",
            )
        if HEROKU_APP_NAME and heroku_client:
            try:
                heroku_app = heroku_client.app(HEROKU_APP_NAME)
            except Exception:
                await message.reply_text(
                    message,
                    "`Heroku Api Key And App Name Doesn't Match!`",
                    parse_mode="markdown",
                )
            if heroku_app:
                await func(client, message, heroku_app)

    return heroku_cli
    
    
 
 
def fetch_heroku_git_url(api_key, app_name):
    if not api_key:
        return None
    if not app_name:
        return None
    heroku = heroku3.from_key(api_key)
    try:
        heroku_applications = heroku.apps()
    except:
        return None
    heroku_app = None
    for app in heroku_applications:
        if app.name == app_name:
            heroku_app = app
            break
    if not heroku_app:
        return None
    return heroku_app.git_url.replace("https://", "https://api:" + api_key + "@")

HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
