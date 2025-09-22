from django.core.management.base import BaseCommand
from agency.models import Category, Tour, Offer

class Command(BaseCommand):
    help = 'Добавляет туры с изображениями в базу данных'

    def handle(self, *args, **options):
        self.stdout.write('Добавляем туры...')
        
        # Создаем категории, если их нет
        beach, created = Category.objects.get_or_create(
            name="Пляжный отдых",
            defaults={'description': 'Расслабьтесь на лучших пляжах мира.'}
        )
        if created:
            self.stdout.write(f'Создана категория: {beach.name}')
        
        adventure, created = Category.objects.get_or_create(
            name="Приключения",
            defaults={'description': 'Испытайте адреналин и новые впечатления.'}
        )
        if created:
            self.stdout.write(f'Создана категория: {adventure.name}')
        
        cultural, created = Category.objects.get_or_create(
            name="Культурный туризм",
            defaults={'description': 'Погрузитесь в историю и культуру разных стран.'}
        )
        if created:
            self.stdout.write(f'Создана категория: {cultural.name}')
        
        nature, created = Category.objects.get_or_create(
            name="Экотуризм",
            defaults={'description': 'Исследуйте нетронутую природу и дикую жизнь.'}
        )
        if created:
            self.stdout.write(f'Создана категория: {nature.name}')
        
        # Добавляем туры
        tours_data = [
            # Пляжный отдых
            {
                'name': 'Мальдивы',
                'description': 'Райские острова с белым песком и кристально чистой водой. Идеально для романтического отдыха.',
                'price': 97000,
                'category': beach,
                'image': 'maldives.jpg'
            },
            {
                'name': 'Бали, Индонезия',
                'description': 'Тропический рай с потрясающими пляжами, рисовыми террасами и богатой культурой.',
                'price': 65000,
                'category': beach,
                'image': 'bali.jpg'
            },
            {
                'name': 'Сейшелы',
                'description': 'Экзотические острова с уникальной флорой и фауной, идеальные для уединенного отдыха.',
                'price': 120000,
                'category': beach,
                'image': 'seychelles.jpg'
            },
            {
                'name': 'Доминикана',
                'description': 'Карибский рай с белоснежными пляжами, пальмами и теплым морем круглый год.',
                'price': 75000,
                'category': beach,
                'image': 'dominican.jpg'
            },
            
            # Приключения
            {
                'name': 'Сафари в Кении',
                'description': 'Увидеть большую пятерку в дикой природе. Незабываемые впечатления от африканского сафари.',
                'price': 145500,
                'category': adventure,
                'image': 'kenya_safari.jpg'
            },
            {
                'name': 'Треккинг в Непале',
                'description': 'Покорите Эверест или насладитесь видами Гималаев. Для любителей гор и приключений.',
                'price': 85000,
                'category': adventure,
                'image': 'nepal_trekking.jpg'
            },
            {
                'name': 'Рафтинг в Коста-Рике',
                'description': 'Спуск по бурным рекам через тропические джунгли. Адреналин и природа в одном флаконе.',
                'price': 55000,
                'category': adventure,
                'image': 'costa_rica_rafting.jpg'
            },
            {
                'name': 'Дайвинг на Мальдивах',
                'description': 'Исследуйте подводный мир с коралловыми рифами и тропическими рыбами.',
                'price': 78000,
                'category': adventure,
                'image': 'maldives_diving.jpg'
            },
            
            # Культурный туризм
            {
                'name': 'Япония - Страна восходящего солнца',
                'description': 'Погрузитесь в уникальную культуру Японии: от древних храмов до современных мегаполисов.',
                'price': 95000,
                'category': cultural,
                'image': 'japan.jpg'
            },
            {
                'name': 'Италия - Колыбель искусства',
                'description': 'Рим, Флоренция, Венеция - города с богатейшей историей и культурным наследием.',
                'price': 88000,
                'category': cultural,
                'image': 'italy.jpg'
            },
            {
                'name': 'Индия - Духовное путешествие',
                'description': 'От Тадж-Махала до священного Ганга. Погружение в древнюю культуру и традиции.',
                'price': 65000,
                'category': cultural,
                'image': 'india.jpg'
            },
            {
                'name': 'Египет - Земля фараонов',
                'description': 'Пирамиды, сфинксы, древние храмы. Путешествие в прошлое человеческой цивилизации.',
                'price': 45000,
                'category': cultural,
                'image': 'egypt.jpg'
            },
            
            # Экотуризм
            {
                'name': 'Амазонка, Бразилия',
                'description': 'Исследуйте самое биоразнообразное место на планете. Встретьте диких животных в их естественной среде.',
                'price': 75000,
                'category': nature,
                'image': 'amazon.jpg'
            },
            {
                'name': 'Галапагосские острова',
                'description': 'Уникальная экосистема, где можно увидеть животных, которых нет больше нигде в мире.',
                'price': 125000,
                'category': nature,
                'image': 'galapagos.jpg'
            },
            {
                'name': 'Новая Зеландия - Страна длинного белого облака',
                'description': 'Фьорды, ледники, вулканы и нетронутая природа. Родина хоббитов и киви.',
                'price': 110000,
                'category': nature,
                'image': 'new_zealand.jpg'
            },
            {
                'name': 'Исландия - Земля огня и льда',
                'description': 'Гейзеры, водопады, северное сияние и вулканы. Уникальная природа в первозданном виде.',
                'price': 85000,
                'category': nature,
                'image': 'iceland.jpg'
            }
        ]
        
        # Добавляем туры
        for tour_data in tours_data:
            tour, created = Tour.objects.get_or_create(
                name=tour_data['name'],
                defaults={
                    'description': tour_data['description'],
                    'price': tour_data['price'],
                    'category': tour_data['category']
                }
            )
            if created:
                self.stdout.write(f'Добавлен тур: {tour.name} - {tour.price} руб.')
            else:
                self.stdout.write(f'Тур уже существует: {tour.name}')
        
        # Добавляем специальные предложения
        offers_data = [
            {
                'name': 'Скидка на Мальдивы',
                'description': 'Сэкономьте 10% на роскошном отдыхе!',
                'original_price': 97000,
                'discounted_price': 87300
            },
            {
                'name': 'Раннее бронирование Бали',
                'description': 'Забронируйте заранее и получите скидку 15%!',
                'original_price': 65000,
                'discounted_price': 55250
            },
            {
                'name': 'Семейный пакет в Доминикане',
                'description': 'Специальная цена для семей с детьми!',
                'original_price': 75000,
                'discounted_price': 60000
            }
        ]
        
        for offer_data in offers_data:
            offer, created = Offer.objects.get_or_create(
                name=offer_data['name'],
                defaults={
                    'description': offer_data['description'],
                    'original_price': offer_data['original_price'],
                    'discounted_price': offer_data['discounted_price']
                }
            )
            if created:
                self.stdout.write(f'Добавлено предложение: {offer.name}')
            else:
                self.stdout.write(f'Предложение уже существует: {offer.name}')
        
        self.stdout.write(f'\nВсего туров в базе: {Tour.objects.count()}')
        self.stdout.write(f'Всего категорий: {Category.objects.count()}')
        self.stdout.write(f'Всего предложений: {Offer.objects.count()}')
        self.stdout.write(self.style.SUCCESS('Туры успешно добавлены!'))
