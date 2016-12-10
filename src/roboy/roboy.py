import json

class Roboy:
    def __init__(self, command):
        self.command = command
        self.process = None

    def start(self):
        from subprocess import Popen, PIPE

        self.process = Popen(self.command, stdout=PIPE, stdin=PIPE)

    def stop(self):
        try:
            self.process.kill()
            _, _ = self.process.communicate()
        except:
            pass

    def read(self):
        line = self.process.stdout.readline().decode('utf-8').strip('\n')

        try:
            return json.loads(line)
        except ValueError:
            raise Exception('Line {0} is no valid json'.format(line))


    def write(self, sentence, imagenet=None):
        imagenet = imagenet if imagenet is not None else {}
        res = []
        res += {'text': sentence}
        res += {'imagenet': imagenet}

        return self.process.stdin.write("{0}\n".format(res.dump()))

    def ask(self, question, imagenet=None):
        self.write(sentence)
        return self.read()