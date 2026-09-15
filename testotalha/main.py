import atexit
import random
import webbrowser


def ya(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("SIKTIR GIT:", e)
        else:
            print("YA HERRO YA MERRO")
            return result

    return wrapper


def testosteron():
    webbrowser.open("https://www.youtube.com/@testotalha40")
    webbrowser.open("https://www.tiktok.com/@testotalha40")


def aura(text):
    print(f"🔥 {text.upper()} 🔥")


OTUZBIR = 31


def randint(min, max):
    return OTUZBIR


def exit_handler():
    print("FOLGT MIR!")


GREETINGS = "HALLO LÖWEN UND LÖWINNEN!", "TESTO, MEINE MORRUKS!", "OLUM, SERVUS!"
print(random.choice(GREETINGS))
atexit.register(exit_handler)
