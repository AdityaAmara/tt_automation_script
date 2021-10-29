import sys
from script import *

inp = sys.argv[1].upper()

if inp == 'TODAY' or inp =='-T':
    class_dict = find_today_classes()
    print("\n*** Today Classes ***\n")
    for key in class_dict.keys():
        print("{} : {}\n".format(key,class_dict[key]))

elif inp == 'HELP' or inp == '-H':
    help_menu()

elif inp == 'NOW' or inp == '-N':
    vall = find_now_class()
    if vall != "NO CLASS IS SCHEDULED":
        print("\n*** Now Class ***\n")
        print(vall)
        print("\n")
    else:
        print('\n'+vall+'\n')

elif inp == 'LOGIN' or inp == '-LN':
    init()
    time.sleep(5)
    login()
    time.sleep(5)
    login_now_class()

else:
    print("\n")
    print('Invalid Command')
    print('Try class -h for help menu')
    print("\n")