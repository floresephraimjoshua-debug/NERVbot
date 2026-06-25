import requests
import os
from dotenv import load_dotenv

load_dotenv()

def NERVbot():
    os.system("clear")
    """
    print(pyfiglet.figlet_format("NERVbot", font="cosmic"))
    """
    logo()

    api_key = os.getenv("GROQ_API_KEY")
    settings = os.getenv("SYSTEM_SETTINGS")
    while True:
        try:
            ask = input("Pilot: ").strip()

            censor = ask.lower().split()

            for word in censor:
                if word in ("racism", "gay", "nigger", "fuck", "asshole", "nigga"):
                    raise ValueError

            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            }
            json = {
                "model": "llama-3.3-70b-versatile",
                "messages": [
                    {"role": "system", "content": f"{settings}"},
                    {"role": "user", "content": f"{ask}"},
                ],
            }

            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=json,
            )
            response.raise_for_status()
            bot = response.json()

            reply = bot["choices"][0]["message"]["content"]
            print("")
            print(f"NervBot: {reply}")
            print("")

        except requests.RequestException:
            print("NERVbot: Pilot input rejected.")
            print("")
            pass
        except ValueError:
            print("NERVbot: Pilot input rejected.")
            print("")
            pass


def logo():
    art = r"""
                               . :+.*==.
                           :#############+
                          =##############
                #         *#################*.
               :#*        *####################*
                 +*       #######################-
                   #:    #########################*
                    :##############################-
                      +#########################*
         =##*    +*  :###################.--
          ####.  :-   ##+.#################=:
          * +##+ :-   ##+ :##################*
          *   ###+-   ##*:*- *################-
          *    +##-   ##+  :  -################.
          *     :#-   ##*    #  =##############=
         ::.      .  ::::::::.    ##############
                        =**-=+=.  +#############*
                        :##   ##+  #############*
                        :##   ##+  .##=*#########
                        :##+*#*     -## .########
                        :## :##=     #### =#####*
                        :##  .##+     ##    *###*
                       :=++=.  ++=    ::     .###
                                               =#

        GOD'S IN HIS HEAVEN, ALL'S RIGHT WITH THE WORLD

MAGI ACCESS TERMINAL:
"""
    print("\033[91m" + art + "\033[0m")


NERVbot()