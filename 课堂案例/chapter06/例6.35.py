favorite_language = {'Jaimin': ['python'], 'chris': ['c', 'ruby'], 'Lucy': ['power shell'],
                     'Candy': ['shell', 'go', 'c++']}

for name, languages in favorite_language.items():
    print("\n" + name.title() + " like programing language: ")
    for language in languages:
        print(language.title())

