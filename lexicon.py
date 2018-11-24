import sys
import keyboard
import pyperclip
import synonyms
import definitions


def main():
    try:
        while True:
            # read hotkey combination pressed by user
            keycombo = keyboard.read_hotkey()
            # assign the clipboard contents to 'word'
            word = pyperclip.paste()
            if keycombo == 'ctrl+g+h':
                # if clipboard wasn't blank, find definition of contents
                if word != None:
                    definitions.lookup_definitions(word)
            elif keycombo == 'ctrl+g+y':
                # if clipboard wasn't blank, find synonym of contents
                if word != None:
                    synonyms.lookup_synonyms(word)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == '__main__':
    main()
