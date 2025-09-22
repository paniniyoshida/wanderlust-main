from agency.models import HomePage, AboutPage, ContactPage, FindUsPage, ToursPage, CartPage, Category, Tour, Offer

def populate():
    HomePage.objects.create(
        headline="Добро пожаловать в Туры Wanderlust!",
        description="Исследуйте мир с нашими уникальными турами.",
        banner_image="banner1.jpg",
        cta_text="Исследовать туры"
    )
    AboutPage.objects.create(
        headline="О нас",
        description="Мы создаем незабываемые путешествия.",
        banner_image="banner2.jpg"
    )
    ContactPage.objects.create(
        headline="Свяжитесь с нами",
        description="Мы здесь, чтобы помочь вам спланировать поездку.",
        banner_image="banner3.jpg"
    )
    FindUsPage.objects.create(
        headline="Как нас найти",
        description="Наши офисы расположены по всему миру.",
        banner_image="banner4.jpg"
    )
    ToursPage.objects.create(
        headline="Наши туры",
        description="Выберите свое следующее приключение.",
        banner_image="banner5.jpg",
        category_cta_text="Категории",
        all_tours_cta_text="Все туры"
    )
    CartPage.objects.create(
        headline="Ваша корзина",
        description="Просмотрите выбранные туры.",
        banner_image="banner6.jpg"
    )
    beach = Category.objects.create(
        name="Пляжный отдых",
        description="Расслабьтесь на лучших пляжах мира."
    )
    adventure = Category.objects.create(
        name="Приключения",
        description="Испытайте адреналин и новые впечатления."
    )
    Tour.objects.create(
        name="Мальдивы",
        description="Райские острова с белым песком.",
        price=97000,
        category=beach
    )
    Tour.objects.create(
        name="Сафари в Кении",
        description="Увидеть большую пятерку в дикой природе.",
        price=145500,
        category=adventure
    )
    Offer.objects.create(
        name="Скидка на Мальдивы",
        description="Сэкономьте на роскошном отдыхе!",
        original_price=97000,
        discounted_price=87300
    )

if __name__ == '__main__':
    populate()