
search_history=['https://en.wikipedia.org/wiki/Floating_point',
                'https://en.wikipedia.org/wiki/Philosophy',
                'https://en.wikipedia.org/wiki/Scince',
                'https://en.wikipedia.org/wiki/Match',
                'https://en.wikipedia.org/wiki/English',
                '1',
                '2',
                '3',
                '4',
                '5',
                '6',
                ]
target_url ='https://en.wikipedia.org/wiki/Floating_point/'
max_steps =20
if search_history[-1] == target_url:
    print("We've found the target article!")
   # return False
elif len(search_history) > max_steps:
    print("The search has gone on suspiciously long, aborting search!")
   # return False
elif search_history[-1] in search_history[:-1]:
    print("We've arrived at an article we've already seen, aborting search!")
   # return False
else:
   print("nothing")
print(search_history[-1])
print(len(search_history))
