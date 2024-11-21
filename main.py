import parser

def repr():
    print("Yellow REPR prerelease v0.1")
    parse = parser.Parser()
    while True:
        prompt = input(">")
        if 'exit' in prompt:
            break
        ast = parse.parse(prompt)
        print(parser.prettyPrint(ast))

repr()