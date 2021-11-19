import requests

INPUT_URL = 'https://adventofcode.com/2020/day/%d/input'

def session_token():
    return open('.session', 'r').read().strip()

# Use this to get the entire input as a single string
def get_input(day):
    headers = { 'cookie': 'session=%s' % session_token() }
    return requests.get(INPUT_URL % day, headers=headers).text.rstrip()

# Use this to get the input as a list of strings, one per line
def get_input_lines(day):
    return get_input(day).rsplit('\n')

# Use this to read each line of input as an integer number
def get_input_integers(day):
    return [int(line) for line in get_input_lines(day)]
