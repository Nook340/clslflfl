from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("27824462"))
API_HASH = getenv("952fa73dd070dd598e7f8a02c28c0700")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("6703043974"))

PING_IMG = getenv("PING_IMG", "https://graph.org/file/6e5004198c3bdbba84bdc.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/6e5004198c3bdbba84bdc.jpg")

SESSION = getenv("BAGB5kgAFm0nYbSIboleRZxF_XWI8ntLnWyEwmkE2xg_kOthzmtgidOwBP3h05X8UQWookw5_dILcSQrKuQ7D562sxLIu2KK9MUEv_jAu-VhxHXHbYtFGOsjBztGqQjbGx82WZDvTg3oE3gdHLgfGng_outWlW8K1vpLNBcHs7P8-opm7E__EGtJ1MyMU7ohfHxK-oh6TmNmkSwIPw3S_oyORgQfOyAGRh9kfBanKpzGtfZYLPztM6OIauB8oeS1lBg4DWiuKa2KUhelCVn_ZCVIRnVjyGhI6_wBN1PsH4raRQdQVhey54lM7k8YokiIAvH7jh9r_yfUNblaMwDkcNilZfL5SwAAAAGSLuyUAA", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/EE_47")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/EE_20")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "6703043974").split()))


FAILED = "https://graph.org/file/6e5004198c3bdbba84bdc.jpg"
