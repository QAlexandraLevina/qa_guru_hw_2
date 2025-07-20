from selene import browser, be, have

def test_should_find_selene(setting_browser):
    browser.element('[name="q"]').should(be.blank).type('Hello World!').press_enter() # Находим поле ввода, вводим текст и жмём Enter
    browser.element('html').should(have.text('programming language')) # Ищем указанный текст на странице выдачи результатов
    print('Текст найден!') # Вывод текста после успешного поиска

def test_no_expecting_search_result(setting_browser):
    browser.element('[name="q"]').should(be.blank).type('аппвоповапваплваплвап').press_enter() # Находим поле ввода, вводим текст и жмём Enter
    browser.element('html').should(have.text('По запросу «аппвоповапваплваплвап» ничего не найдено.')) # Ищем указанный текст на странице выдачи результатов
    print('Ничего не найдено!') # Вывод текста после неуспешного поиска