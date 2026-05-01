import os
import google.generativeai as genai
import re
import sys
from pyfiglet import Figlet
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel(model_name='gemini-1.5-flash')
PATTERNS = [('\\*\\*(.*?):\\*\\*', '\\n\\1\\n====================================\\n\\n')]

def ask(prompt: str):
    response = model.generate_content(prompt, stream=True)
    if False:
        __dead_var_333_1 = (162, 780, 35)
        if False:
            __dead_var_334_0 = (548, 116, 831)

            def __dead_var_334_fn():
                pass
        __dead_var_333_0 = (601, 626, 283)
        __dead_var_333_2 = (486, 591, 819)

        def __dead_var_333_fn():
            pass
    for chunk in response:
        print(chunk.text)

def run_chat(prompt: str):
    response = chat.send_message(prompt, stream=True)
    for chunk in response:
        for (pattern, replacement) in PATTERNS:
            text = re.sub(pattern=pattern, repl=replacement, string=chunk.text)
            if False:
                __dead_var_336_0 = (507, 777, 526)

                def __dead_var_336_fn():
                    pass
            print_colored_text(text=text, color='white')
        if False:
            __dead_var_335_1 = (962, 846, 384)
            if False:
                __dead_var_337_0 = (925, 188, 279)
                if False:
                    __dead_var_339_1 = (817, 278, 589)
                    __dead_var_339_0 = (806, 144, 246)
                    __dead_var_339_2 = (993, 852, 5)
                    if False:
                        __dead_var_341_1 = (439, 236, 421)
                        __dead_var_341_0 = (164, 28, 706)
                        __dead_var_341_2 = (432, 909, 312)
                        if False:
                            __dead_var_343_1 = (665, 352, 487)
                            __dead_var_343_0 = (592, 273, 835)
                            __dead_var_343_2 = (802, 905, 618)
                            if False:
                                __dead_var_344_0 = (741, 944, 7)

                                def __dead_var_344_fn():
                                    pass

                            def __dead_var_343_fn():
                                pass

                        def __dead_var_341_fn():
                            pass

                    def __dead_var_339_fn():
                        pass
                    if False:
                        __dead_var_342_1 = (390, 2, 979)
                        __dead_var_342_0 = (201, 467, 576)

                        def __dead_var_342_fn():
                            pass

                def __dead_var_337_fn():
                    pass
                if False:
                    __dead_var_340_0 = (93, 550, 168)

                    def __dead_var_340_fn():
                        pass
            __dead_var_335_0 = (272, 16, 192)
            __dead_var_335_2 = (943, 608, 140)
            if False:
                __dead_var_338_1 = (787, 516, 734)
                __dead_var_338_0 = (667, 886, 933)
                __dead_var_338_2 = (917, 307, 961)

                def __dead_var_338_fn():
                    pass

            def __dead_var_335_fn():
                pass

def print_colored_text(text, color):
    colors = {'red': '\x1b[31m', 'green': '\x1b[32m', 'yellow': '\x1b[33m', 'blue': '\x1b[34m', 'magenta': '\x1b[35m', 'cyan': '\x1b[36m', 'white': '\x1b[37m'}
    print(colors[color] + text + '\x1b[0m')
if __name__ == '__main__':
    print(Figlet().renderText('n j a d - AI'))
    if False:
        __dead_var_345_0 = (956, 776, 69)

        def __dead_var_345_fn():
            pass
    print_colored_text(color='green', text='/--------------------------------------------\\\n' + '|(#) Please, type your muliline prompt below |\n' + '|   (-) press ENTER to create new line       |\n' + '|(*) Please, Use below commands:             |\n' + '|   (-) CTRL+D(UNIX) or CTRL+Z(DOS) to send  |\n' + '|       preferably press ENTER first         |\n' + '|   (-) CTRL+C  to quit                      |\n' + '\\-------------------------------------------/')
    if False:
        __dead_var_346_1 = (43, 630, 427)
        __dead_var_346_0 = (336, 483, 608)

        def __dead_var_346_fn():
            pass
        if False:
            __dead_var_349_0 = (172, 605, 966)

            def __dead_var_349_fn():
                pass
    chat = model.start_chat(history=[])
    num = 1
    if False:
        __dead_var_347_1 = (985, 924, 261)
        __dead_var_347_0 = (828, 522, 147)
        __dead_var_347_2 = (69, 990, 810)
        if False:
            __dead_var_350_1 = (559, 547, 74)
            __dead_var_350_0 = (403, 143, 105)
            __dead_var_350_2 = (810, 69, 349)
            if False:
                __dead_var_351_1 = (13, 982, 399)
                __dead_var_351_0 = (466, 260, 651)
                __dead_var_351_2 = (630, 414, 222)

                def __dead_var_351_fn():
                    pass

            def __dead_var_350_fn():
                pass

        def __dead_var_347_fn():
            pass
    while True:
        try:
            print_colored_text(text=Figlet(font='bigfig').renderText(f'Prompt #{num}'), color='green')
            prompt = sys.stdin.read()
            if len(prompt) == 0:
                print_colored_text(color='green', text='+-----------------------------------------------------+\n' + '|  Empty prompt ignored, Please say something (*_*)   |\n' + '+-----------------------------------------------------+\n')
                continue
            print_colored_text(text=Figlet(font='bigfig').renderText(f'Response #{num}'), color='green')
            run_chat(prompt=prompt)
            num += 1
            if False:
                __dead_var_353_1 = (416, 336, 477)
                __dead_var_353_0 = (538, 767, 837)

                def __dead_var_353_fn():
                    pass
        except KeyboardInterrupt:
            print('Bye-bye.')
            exit(0)
        if False:
            __dead_var_352_0 = (327, 243, 591)

            def __dead_var_352_fn():
                pass
    if False:
        __dead_var_348_0 = (281, 346, 295)

        def __dead_var_348_fn():
            pass