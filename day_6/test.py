import tasks_6


# Test whether a year is a leap year
def test_leap_year():
    is_leap = tasks_6.check_leap_years(2000)
    assert is_leap == True


# Test whether a year is NOT a leap year
def test_not_leap_year():
    not_leap = tasks_6.check_leap_years(1800)
    assert not_leap == False


# Test to get length of the last word in a sentence
def test_length_last_word():
    last_word = tasks_6.word_length("nelson chege")
    assert last_word == 5


# Test  password length

def test_low_password_length():
    password = tasks_6.get_password(6)
    assert len(password) == 6


def test_medium_password_length():
    password = tasks_6.get_password(9)
    assert len(password) == 9


def test_hard_password_length():
    password = tasks_6.get_password(11)
    assert len(password) == 11


def test_very_hard_password_length():
    password = tasks_6.get_password(12)
    assert len(password) == 12


def test_csv_as_dictionary():
    csv_dict = tasks_6.csv_as_dict("C:/Users/nelson/Desktop/skaehub_developer_projects/day_1/schools.csv")
    assert isinstance(csv_dict, dict) == True


def test_when_no_duplicates():
    my_list = tasks_6.remove_duplicates([15, 9, 5,"a", 3,"a", 5,"b","c", 6, 1])
    assert any(my_list.count(element) > 1 for element in my_list) == False