def to_weird_case(string='This is a test'):
    nova_string = [let.upper() if i % 2 == 0 else let.lower()
                   for i,let in enumerate(string)
                 
                  ]
    print(nova_string)
    return ''.join(nova_string) 
print(to_weird_case())