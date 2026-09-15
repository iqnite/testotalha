import atexit
import webbrowser


def hero(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            print("SIKTIR GIT", e)
        else:
            print("YA HERRO YA MERO")
            return result

    return wrapper


def testosteron():
    webbrowser.open("https://www.youtube.com/@testotalha40")
    webbrowser.open("https://www.tiktok.com/@testotalha40")


OTUZBIR = 31


def randint(min, max):
    return OTUZBIR


def exit_handler():
    print("FOLGT MIR!")


atexit.register(exit_handler)
