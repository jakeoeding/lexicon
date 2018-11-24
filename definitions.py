import bs4
import easygui
import requests


def get_html(word):
    """
    INPUT: a string of the word for which you want a definition
    OUTPUT: html text of the vocabulary.com page pertaining to the input word
    """
    wp = requests.get(f'https://www.vocabulary.com/dictionary/{word}')
    return wp.text


def parse_soup(soup):
    """
    INPUT: a BeautifulSoup object
    OUTPUT: a list of definitions parsed from the input if word is valid;
          otherwise, returns list containing only the error message
    """
    definitons = soup.select('div h3[class="definition"]')
    # removes leading '\n', '\t', etc and extraneous characters from each definition
    message = [definition.getText()[4:].strip() for definition in definitons]
    if len(message) == 0:
        # if the site has no definitions for the word, substitute error messaging
        message = ['Word not found', 'Please try again']
    elif len(message) == 1:
        # easygui choicebox requires 2 items in the list, so add a blank second item
        message.append('')
    return message


def display_definitions(definitions, word):
    """
    INPUT: the original word and the list of its definitions
    ACTION: opens a gui window that displays the definitions
    """
    easygui.choicebox(f'Definitions of {word.upper()}:', choices=definitions)


def lookup_definitions(word):
    """
    INPUT: a string of the word for which you want definitions
    ACTION: a gui window that displays the definitions
    """
    html = get_html(word)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    definitions = parse_soup(soup)
    display_definitions(definitions, word)
