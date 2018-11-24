import bs4
import easygui
import requests


def get_html(word):
    """
    INPUT: a string of the word for which you want synonyms
    OUTPUT: html text of the synonym.com page pertaining to the input word
    """
    wp = requests.get(f'http://www.synonym.com/synonyms/{word}')
    return wp.text


def parse_soup(soup):
    """
    INPUT: a BeautifulSoup object
    OUTPUT: a list of synonyms parsed from the input if word is valid;
          otherwise, returns list containing only the error message
    """
    # check to see if there is an error message
    error_message = soup.select('div[id="notification"]')
    if len(error_message) == 1:
        message = ['Word not found', 'Please try again']
    else:
        message = [syn.getText().replace('\n','') for syn in soup.select('.syn')]
        if len(message) == 1:
            # easygui choicebox requires 2 items in the list, so add a blank second item
            message.append('')
    return message


def display_synonyms(synonyms, word):
    """
    INPUT: the original word and the list of its synonyms
    ACTION: opens a gui window that displays the synonyms
    """
    easygui.choicebox(f'Synonyms of {word.upper()}:', choices=synonyms)


def lookup_synonyms(word):
    """
    INPUT: a string of the word for which you want synonyms
    ACTION: a gui window that displays the synonyms
    """
    html = get_html(word)
    soup = bs4.BeautifulSoup(html, 'html.parser')
    synonyms = parse_soup(soup)
    display_synonyms(synonyms, word)
