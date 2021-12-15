import requests
import re
import secret

# Adapted from @MathisHammel

AOC_COOKIE = secret.cookie # AOC session cookie

class AOC:
    def __init__(self, day, year=2021, path=None):
        self.day = day
        self.year = year
        self.path = '/'.join(path.split('/') [:-1]) + '/' if path is not None else ''
        try:
            self._input = open(self.path + 'input').read()
        except FileNotFoundError:
            self._input = None
        try:
            self._example = open(self.path + 'example').read()
        except FileNotFoundError:
            self._example = None

    @property
    def input(self):
        if self._input is None:
            req = requests.get(
                f'https://adventofcode.com/{self.year}/day/{self.day}/input', headers={'cookie': 'session='+AOC_COOKIE})
            self._input = req.text
            open(self.path + 'input', 'w').write(self._input)
        return self._input

    def get_example(self, offset=0):
        if self._example is None or self._example[0] != offset:
            req = requests.get(
                f'https://adventofcode.com/{self.year}/day/{self.day}', headers={'cookie': 'session='+AOC_COOKIE})
            self._example = (offset, re.sub('&lt;', '<', re.sub('&gt;', '>', re.sub(
                '<[^<]+?>', '', req.text.split('<pre><code>')[offset+1].split('</code></pre>')[0]))))
            open(self.path + 'example', 'w').write(self._example[1] + '\n')
        return self._example[1]
    example = property(get_example)

    def submit(self, part, answer):
        print(f'You are about to submit the follwing answer:')
        print(f'>>>>>>>>>>>>>>>>> {answer}')
        input('Press enter to continue or Ctrl+C to abort.')
        data = {
            'level': str(part),
            'answer': str(answer)
        }

        response = requests.post(f'https://adventofcode.com/{self.year}/day/{self.day}/answer',
                                 headers={'cookie': 'session='+AOC_COOKIE}, data=data)
        if 'You gave an answer too recently' in response.text:
            # You will get this if you submitted a wrong answer less than 60s ago.
            print('VERDICT : TOO MANY REQUESTS')
        elif 'not the right answer' in response.text:
            if 'too low' in response.text:
                print('VERDICT : WRONG (TOO LOW)')
            elif 'too high' in response.text:
                print('VERDICT : WRONG (TOO HIGH)')
            else:
                print('VERDICT : WRONG (UNKNOWN)')
        elif 'seem to be solving the right level.' in response.text:
            # You will get this if you submit on a level you already solved.
            # Usually happens when you forget to switch from `PART = 1` to `PART = 2`
            print('VERDICT : ALREADY SOLVED')
        else:
            print('VERDICT : OK !')
