from student import StudentDB
import pytest 

db=None
# set_up and tear down methods  :- setup will be execute before executing the tests
def  setup_module(module):
    print("-----------setup----------------")
    global db
    db=StudentDB()
    db.connect('data.json')

# it will free our resources
def teardown_module(module):
    print("---------tear down--------")
    db.close()

def test_Senpai_data():
    # db=StudentDB()
    # db.connect('data.json')
    Senpai_data = db.get_data('Senpai')
    assert Senpai_data['ID'] == '1'
    assert Senpai_data['Name']=='Senpai'
    assert Senpai_data['Class']=='32'

def test_Yui_Rio_data():
    # db=StudentDB()
    # db.connect('data.json')
    Yui_Rio_data = db.get_data('Yui_Rio')
    print("------------Yui_Rio_data_________",Yui_Rio_data)
    assert Yui_Rio_data['ID'] == '2'
    assert Yui_Rio_data['Name']=='Yui_Rio'
    assert Yui_Rio_data['Class']=='11'
