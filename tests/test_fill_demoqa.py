import os
import allure
from selene import browser, have, by

file_path = os.path.join(os.path.dirname(__file__), 'testfile.txt')

def test_fill_demoqa(setup_browser):

    with allure.step('Open registration form'):
        browser.open('/automation-practice-form')
        browser.execute_script('window.scrollBy(0, 550)')

    with allure.step('Fill form'):
        browser.element('#firstName').type("Иван")
        browser.element('#lastName').type("Иванов")
        browser.element('#userEmail').type("ivaniv@gmail.com")
        browser.element('#genterWrapper').element(by.text('Male')).click()
        browser.element('#userNumber').type("1949949949")

        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__year-select').click()
        browser.element('.react-datepicker__year-select option[value="1990"]').click()
        browser.element('.react-datepicker__month-select').click()
        browser.element('.react-datepicker__month-select option[value="0"]').click()
        browser.element('.react-datepicker__day--001').click()

        browser.element('#subjectsInput').type('English').press_enter()
        browser.element('label[for="hobbies-checkbox-3"]').with_(click_by_js=True).click()

        browser.element('#uploadPicture').send_keys(file_path)

        browser.element('#currentAddress').type("Пушкинская 23")

        browser.element('#state').click()
        browser.element('#react-select-3-option-3').click()
        browser.element('#city').click()
        browser.element('#react-select-4-option-1').click()

        browser.element('#submit').click()

    with allure.step("Check form"):
        browser.element('.table-responsive').all('tr').should(
            have.exact_texts(
                'Label Values',
                'Student Name Иван Иванов',
                'Student Email ivaniv@gmail.com',
                'Gender Male', 'Mobile 1949949949',
                'Date of Birth 01 January,1990',
                'Subjects English',
                'Hobbies Music',
                'Picture testfile.txt',
                'Address Пушкинская 23',
                'State and City Rajasthan Jaiselmer'))