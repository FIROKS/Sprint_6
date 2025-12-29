class MainPageQuestions: 
    QUESTIONS = {
        'COST': 'Сколько это стоит? И как оплатить?',
        'SEVERAL_SCOOTERS': 'Хочу сразу несколько самокатов! Так можно?',
        'RENTAL_TIME': 'Как рассчитывается время аренды?',
        'ORDER_FOR_TODAY': 'Можно ли заказать самокат прямо на сегодня?',
        'EXTEND_OR_RETURN': 'Можно ли продлить заказ или вернуть самокат раньше?',
        'CHARGING_DELIVERY': 'Вы привозите зарядку вместе с самокатом?',
        'CANCEL_ORDER': 'Можно ли отменить заказ?',
        'OUTSIDE_MRR': 'Я жизу за МКАДом, привезёте?'
    }

    ANSWERS = {
        'COST': 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
        'SEVERAL_SCOOTERS': 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
        'RENTAL_TIME': 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
        'ORDER_FOR_TODAY': 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
        'EXTEND_OR_RETURN': 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
        'CHARGING_DELIVERY': 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
        'CANCEL_ORDER': 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
        'OUTSIDE_MRR': 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
    }

class Endpoints:
    MAIN_PAGE = 'https://qa-scooter.praktikum-services.ru/'
    ORDER_PAGE = 'https://qa-scooter.praktikum-services.ru/order'
    DZEN_PAGE = 'https://dzen.ru/?yredirect=true'

ORDERDATA = [
    ('Иван', 'Иванов', 'ул. Пушкина, 67', '1', '88888888888', '10', 'сутки', 'black', 'Комментарий'),
    ('Федор', 'Васильев', 'ул. Новогодняя, 26', '2', '88005553535', '31', 'двое суток', 'grey', ''),
]

QUESTIONS_DATA= [
    (0, 0, MainPageQuestions.ANSWERS['COST'], MainPageQuestions.QUESTIONS['COST']),
    (1, 1, MainPageQuestions.ANSWERS['SEVERAL_SCOOTERS'], MainPageQuestions.QUESTIONS['SEVERAL_SCOOTERS']),
    (2, 2, MainPageQuestions.ANSWERS['RENTAL_TIME'], MainPageQuestions.QUESTIONS['RENTAL_TIME']),
    (3, 3, MainPageQuestions.ANSWERS['ORDER_FOR_TODAY'], MainPageQuestions.QUESTIONS['ORDER_FOR_TODAY']),
    (4, 4, MainPageQuestions.ANSWERS['EXTEND_OR_RETURN'], MainPageQuestions.QUESTIONS['EXTEND_OR_RETURN']),
    (5, 5, MainPageQuestions.ANSWERS['CHARGING_DELIVERY'], MainPageQuestions.QUESTIONS['CHARGING_DELIVERY']),
    (6, 6, MainPageQuestions.ANSWERS['CANCEL_ORDER'], MainPageQuestions.QUESTIONS['CANCEL_ORDER']),
    (7, 7, MainPageQuestions.ANSWERS['OUTSIDE_MRR'], MainPageQuestions.QUESTIONS['OUTSIDE_MRR']),
]