import abc


class MarkdownSyntax(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def generate_markdown_format(self):
        pass


class Plain(MarkdownSyntax):
    def __init__(self, text):
        self.text = text

    def generate_markdown_format(self):
        return self.text


class Bold(MarkdownSyntax):
    def __init__(self, text):
        self.text = text

    def generate_markdown_format(self):
        return "**{}**".format(self.text)


class Italic(MarkdownSyntax):
    def __init__(self, text):
        self.text = text

    def generate_markdown_format(self):
        return "*{}*".format(self.text)


class Link(MarkdownSyntax):
    def __init__(self, label, url):
        self.label = label
        self.url = url

    def generate_markdown_format(self):
        return "[{}]({})".format(self.label, self.url)


class InLineCode(MarkdownSyntax):
    def __init__(self, code):
        self.code = code

    def generate_markdown_format(self):
        return '`' + "{}".format(self.code) + '`'


class Header(MarkdownSyntax):
    def __init__(self, level, header):
        self.level = level
        self.header = header

    def generate_markdown_format(self):
        return "#" * int(self.level) + " {}\r".format(self.header)


class OrderedList(MarkdownSyntax):
    def __init__(self, times):
        self.times = times

    def generate_markdown_format(self):
        while True:
            if self.times <= 0:
                print("The number of rows should be greater than zero")
                self.times = int(input("- Number of rows:"))
            else:
                break
        order = ""
        for i in range(self.times):
            order += "{}. ".format(i+1) + input("Row #{}:".format(i+1)) + '\r'
        return order


class UnOrderedList(MarkdownSyntax):
    def __init__(self, times):
        self.times = times

    def generate_markdown_format(self):
        while True:
            if self.times <= 0:
                print("The number of rows should be greater than zero")
                self.times = int(input("- Number of rows:"))
            else:
                break
        unorder = ""
        for i in range(self.times):
            unorder += "* " + input("Row #{}:".format(i+1)) + '\r'
        return unorder


class LineBreak(MarkdownSyntax):
    def generate_markdown_format(self):
        return "\r"


def markdown_syntax_factory(command):
    if command == "plain":
        return Plain(input("- Text:")).generate_markdown_format()
    elif command == "bold":
        return Bold(input("- Text:")).generate_markdown_format()
    elif command == "italic":
        return Italic(input("- Text:")).generate_markdown_format()
    elif command == "link":
        return Link(input("- Label:"), input("- URL:")).generate_markdown_format()
    elif command == "inline-code":
        return InLineCode(input("- Text:")).generate_markdown_format()
    elif command == "header":
        return Header(input("- Level:"), input("- Text:")).generate_markdown_format()
    elif command == "ordered-list":
        return OrderedList(int(input("- Number of rows:"))).generate_markdown_format()
    elif command == "unordered-list":
        return UnOrderedList(int(input("- Number of rows:"))).generate_markdown_format()
    elif command == "line-break":
        return LineBreak().generate_markdown_format()
    elif command == "new-line":
        return LineBreak().generate_markdown_format()


text = ""
while True:
    command = input("- Choose a formatter:")
    if command in ['plain', 'bold', 'italic', 'link', 'inline-code', 'header', 'ordered-list', 'unordered-list', 'new-line', 'line-break']:
        if command in ['header', 'new-line', 'ordered-list', 'unordered-list']:
            text += markdown_syntax_factory(command)
            print(text)
            print("")
        else:
            text += markdown_syntax_factory(command)
            print(text)
    elif command == "!help":
        print("Available formatters: plain bold italic link inline-code header ordered-list unordered-list line-break")
        print("Special commands: !help !done")
    elif command == "!done":
        file = open("output.md", mode='w+')
        file.write(text)
        file.close()
        break
    else:
        print("Unknown formatting type or command")
