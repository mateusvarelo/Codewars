def to_weird_case(string):
    nova_string = [let.upper() if i % 2 == 0 else let.lower()
                   for i,let in enumerate(string)
                  ]
    return ''.join(nova_string) 