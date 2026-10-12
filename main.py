# Drill 2: getting data from a textbox
from pyscript import display, document


def check_name(e):
    document.getElementById('div1').innerHTML = ' '
    f_name = document.getElementById('fname').value 
    l_name = document.getElementById('lname').value 

    first_names = ['raeven', 'carizza', 'gary', 'roman']
    last_names = ['davis', 'alfaro', 'thurman', 'loreto']

    pangalan = document.getElementById('fname').value.lower().strip()
    name = document.getElementById('lname').value.lower().strip()
    fname_checker = pangalan in first_names # True(1) or False (0)
    lname_checker = name in last_names # True(1) or False (0)

    display_message = ('Sorry your name is not in the list.', f'Congratulations, {f_name} {l_name}! You are now in the Communication Arts Club!')
    display(display_message[fname_checker], target='div1')