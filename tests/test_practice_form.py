from selene.support.shared import browser
from demoqa_tests.model.pages import practice_form


def test_fill_practice_form(window_size):
    browser.open('https://demoqa.com/automation-practice-form')
    practice_form.set_first_name('Ivan')
    practice_form.set_last_name('Petrov')
    practice_form.set_email('test_practice_form@mail.ru')
    practice_form.select_gender('Other')
    practice_form.set_mobile_number('8999577120')
    practice_form.set_birthday(5, 1920, 21)
    practice_form.set_subjects('Maths')
    practice_form.select_hobbies('Reading')
    practice_form.select_picture('test_image.png')
    practice_form.set_current_address('Starokolpaksky alley')
    practice_form.select_state('Uttar Pradesh')
    practice_form.select_city('Lucknow')
    practice_form.submit()


def test_should_be_correct_result_form_():
    practice_form.check_results('Ivan Petrov', 'test_practice_form@mail.ru', 'Other', '8999577120',
                                '21 May,1920', 'Maths', 'Reading', 'test_image.png',
                                'Starokolpaksky alley', 'Uttar Pradesh Lucknow')








