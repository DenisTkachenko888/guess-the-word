import random
from colorama import init, Fore

init(autoreset=True)

# Списки слов
words_ru = ['человек', 'работа', 'вопрос', 'сторона', 'страна', 'случай', 'голова', 'ребенок', 'система',
             'отношение', 'женщина', 'деньги', 'машина', 'проблема', 'решение', 'история', 'власть', 'тысяча',
             'возможность', 'результат', 'область', 'статья', 'компания', 'группа', 'развитие', 'процесс', 'условие',
             'средство', 'начало', 'уровень', 'минута', 'качество', 'дорога', 'действие', 'государство', 'любовь',
             'взгляд', 'общество', 'деятельность', 'организация', 'президент', 'комната', 'порядок', 'момент',
             'письмо', 'помощь', 'ситуация', 'состояние', 'квартира', 'внимание', 'смерть', 'программа', 'задача',
             'предприятие', 'разговор', 'правительство', 'производство', 'информация', 'положение', 'интерес',
             'федерация', 'правило', 'управление', 'мужчина', 'партия', 'сердце', 'движение', 'материал', 'неделя',
             'чувство', 'газета', 'причина', 'основа', 'товарищ', 'культура', 'данные', 'мнение', 'документ',
             'институт', 'проект', 'встреча', 'директор', 'служба', 'судьба', 'девушка', 'очередь', 'состав',
             'количество', 'событие', 'объект', 'создание', 'значение', 'период', 'искусство', 'структура', 'пример',
             'исследование', 'гражданин', 'начальник', 'принцип', 'воздух', 'характер', 'борьба', 'использование',
             'размер', 'образование', 'мальчик', 'представитель', 'участие', 'девочка', 'политика', 'картина', 'доллар',
             'территория', 'изменение', 'направление', 'рисунок', 'течение', 'церковь', 'население', 'большинство',
             'музыка', 'правда', 'свобода', 'память', 'команда', 'договор', 'дерево', 'хозяин', 'природа', 'телефон',
             'позиция', 'писатель', 'самолет', 'солнце', 'спектакль', 'способ', 'журнал', 'руководитель', 'специалист',
             'оценка', 'регион', 'процент', 'родитель', 'требование', 'основание', 'половина', 'анализ', 'автомобиль',
             'экономика', 'литература', 'бумага', 'степень', 'господин', 'надежда', 'предмет', 'вариант', 'министр',
             'граница', 'модель', 'операция', 'название', 'старик', 'миллион', 'счастье', 'ребята', 'кабинет',
             'магазин', 'пространство', 'знание', 'защита', 'руководство', 'площадь', 'сознание', 'возраст', 'участник',
             'участок', 'желание', 'доктор', 'председатель', 'представление', 'солдат', 'художник', 'оружие',
             'соответствие', 'парень', 'зрение', 'генерал', 'понятие', 'строительство', 'услуга', 'содержание',
             'радость', 'безопасность', 'продукт', 'комплекс', 'бизнес', 'сотрудник', 'предложение', 'технология',
             'реформа', 'отсутствие', 'собака', 'камень', 'будущее', 'рассказ', 'контроль', 'продукция', 'техника',
             'здание', 'необходимость', 'подготовка', 'республика', 'хозяйство', 'бюджет', 'деревня', 'элемент',
             'обстоятельство', 'победа', 'источник', 'звезда', 'сестра', 'практика', 'проведение', 'карман',
             'определение', 'функция', 'войско', 'комиссия', 'применение', 'капитан', 'работник', 'обеспечение',
             'офицер', 'фамилия', 'предел', 'выборы', 'ученый', 'бутылка', 'теория', 'разработка', 'личность',
             'праздник', 'влияние', 'читатель', 'удовольствие', 'ответственность', 'учитель', 'множество',
             'особенность', 'показатель', 'корабль', 'впечатление', 'частность', 'детство', 'профессор', 'прошлое',
             'командир', 'коридор', 'поддержка', 'собрание', 'болезнь', 'клетка', 'заявление', 'попытка', 'сравнение',
             'расчет', 'депутат', 'комитет', 'выражение', 'здоровье', 'десяток', 'глубина', 'студент', 'секунда',
             'скорость', 'ошибка', 'режиссер', 'поверхность', 'ощущение', 'станция', 'революция', 'колено',
             'министерство', 'стекло', 'высота', 'бабушка', 'трубка', 'мастер', 'поведение', 'столица', 'механизм',
             'передача', 'способность', 'подход', 'энергия', 'существование', 'исполнение', 'сожаление', 'заместитель',
             'ресурс', 'рождение', 'администрация', 'стоимость', 'улыбка', 'артист', 'фигура', 'субъект', 'реакция',
             'список', 'фотография', 'журналист', 'нарушение', 'заседание', 'больница', 'существо', 'свойство',
             'поколение', 'животное', 'усилие', 'отличие', 'остров', 'противник', 'реализация', 'страница',
             'формирование', 'житель', 'красота', 'растение', 'явление', 'наличие', 'одежда', 'кресло', 'больной',
             'университет', 'традиция', 'декабрь', 'ладонь', 'сведение', 'цветок', 'октябрь', 'занятие', 'сентябрь',
             'помещение', 'январь', 'зритель', 'редакция', 'фактор', 'август', 'известие', 'зависимость', 'охрана',
             'оборудование', 'концерт', 'отделение', 'расход', 'выставка', 'милиция', 'переход', 'произведение',
             'родина', 'собственность', 'лагерь', 'имущество', 'кровать', 'аппарат', 'середина', 'клиент', 'отрасль',
             'беседа', 'законодательство', 'продажа', 'повышение', 'полковник', 'сомнение', 'понимание', 'апрель',
             'кодекс', 'настроение', 'должность', 'преступление', 'лестница', 'установка', 'появление', 'получение',
             'образец', 'главное', 'костюм', 'ценность', 'обязанность', 'таблица', 'воспоминание', 'лошадь', 'коллега',
             'организм', 'ученик', 'учреждение', 'открытие', 'характеристика', 'выполнение', 'оборона', 'выступление',
             'температура', 'перспектива', 'подруга', 'приказ', 'жертва', 'ресторан', 'километр', 'признак',
             'промышленность', 'американец', 'заключение', 'восток', 'исключение', 'постановление', 'перевод',
             'секретарь', 'польза', 'звонок', 'обстановка', 'чиновник', 'соглашение', 'деталь', 'русский', 'тишина',
             'зарплата', 'подарок', 'тюрьма', 'конкурс', 'книжка', 'изучение', 'просьба', 'публика', 'сообщение',
             'угроза', 'достижение', 'назначение', 'реклама', 'портрет', 'стакан', 'творчество', 'телевизор',
             'инструмент', 'концепция', 'лейтенант', 'реальность', 'знакомый', 'конфликт', 'переговоры', 'запись',
             'площадка', 'последствие', 'сотрудничество', 'зеркало', 'академия', 'палата', 'потребность', 'ноябрь',
             'увеличение', 'поездка', 'потеря', 'февраль', 'мероприятие', 'принятие', 'устройство', 'вещество',
             'категория', 'гостиница', 'издание', 'объединение', 'темнота', 'человечество', 'колесо', 'опасность',
             'разрешение', 'воздействие', 'коллектив', 'камера', 'следствие', 'кандидат', 'родственник', 'давление',
             'присутствие', 'взаимодействие', 'партнер', 'двигатель', 'достоинство', 'страсть', 'испытание', 'оплата',
             'разница', 'водитель', 'снижение', 'формула', 'капитал', 'новость', 'эффект', 'губернатор', 'доклад',
             'убийство', 'эксперт', 'автобус', 'платье', 'общение', 'психология', 'проверка', 'процедура', 'рабочий',
             'ремонт', 'обращение', 'обучение', 'ожидание', 'памятник', 'корень', 'наблюдение', 'доказательство',
             'признание', 'постель', 'владелец', 'компьютер', 'инженер', 'старуха', 'ракета', 'вершина', 'выпуск',
             'торговля', 'молодежь', 'корпус', 'недостаток', 'сущность', 'талант', 'эффективность', 'полоса',
             'основное', 'рассмотрение', 'следователь', 'описание', 'редактор', 'дворец', 'забота', 'столик',
             'эксперимент', 'печать', 'кольцо', 'пистолет', 'воспитание', 'начальство', 'профессия', 'ворота', 'дружба',
             'окончание', 'величина', 'записка', 'инициатива', 'совесть', 'активность', 'кредит', 'господь',
             'конференция', 'потолок', 'библиотека', 'помощник', 'конструкция', 'металл', 'молоко', 'прокурор',
             'транспорт', 'поэзия', 'соединение', 'краска', 'расстояние', 'подразделение', 'сигнал', 'атмосфера',
             'контакт', 'сигарета', 'восторг', 'золото', 'премия', 'король', 'подъезд', 'автомат', 'мальчишка',
             'чтение', 'поселок', 'свидетель', 'ставка', 'удивление', 'поворот', 'возвращение', 'мгновение', 'статус',
             'параметр', 'сказка', 'тенденция', 'дыхание', 'версия', 'масштаб', 'монастырь', 'хозяйка', 'эксплуатация',
             'коммунист', 'пенсия', 'приятель', 'объяснение', 'производитель', 'философия', 'мощность', 'обязательство',
             'кризис', 'указание', 'яблоко', 'препарат', 'действительность', 'москвич', 'остаток', 'изображение',
             'сделка', 'сочинение', 'покупатель', 'затрата', 'строка', 'единица', 'обработка', 'чемпионат']

words_en = ['person', 'job', 'question', 'side', 'country', 'case', 'head', 'child', 'system',
             'attitude', 'woman', 'money', 'car', 'problem', 'solution', 'history', 'power', 'thousand',
             'opportunity', 'result', 'area', 'article', 'company', 'group', 'development', 'process', 'condition',
             'means', 'beginning', 'level', 'minute', 'quality', 'road', 'action', 'state', 'love',
             'view', 'society', 'activity', 'organization', 'president', 'room', 'order', 'moment',
             'letter', 'help', 'situation', 'condition', 'apartment', 'attention', 'death', 'program', 'task',
             'enterprise', 'conversation', 'government', 'production', 'information', 'position', 'interest',
             'federation', 'rule', 'management', 'man', 'party', 'heart', 'movement', 'material', 'week',
             'feeling', 'newspaper', 'reason', 'basis', 'comrade', 'culture', 'data', 'opinion', 'document',
             'institute', 'project', 'meeting', 'director', 'service', 'fate', 'girl', 'queue', 'staff',
             'quantity', 'event', 'object', 'creation', 'value', 'period', 'art', 'structure', 'example',
             'research', 'citizen', 'boss', 'principle', 'air', 'character', 'struggle', 'use',
             'size', 'education', 'boy', 'representative', 'participation', 'girl', 'politics', 'painting', 'dollar',
             'territory', 'change', 'direction', 'pattern', 'current', 'church', 'population', 'majority',
             'music', 'truth', 'freedom', 'memory', 'command', 'contract', 'tree', 'host', 'nature', 'phone',
             'position', 'writer', 'airplane', 'sun', 'performance', 'method', 'magazine', 'supervisor', 'specialist',
             'score', 'region', 'percentage', 'parent', 'requirement', 'base', 'half', 'analysis', 'car',
             'economics', 'literature', 'paper', 'degree', 'mister', 'hope', 'subject', 'option', 'minister',
             'border', 'model', 'operation', 'name', 'old man', 'million', 'happiness', 'guys', 'cabinet',
             'shop', 'space', 'knowledge', 'protection', 'guidance', 'area', 'consciousness', 'age', 'participant',
             'plot', 'desire', 'doctor', 'chairman', 'performance', 'soldier', 'artist', 'weapon',
             'compliance', 'guy', 'vision', 'general', 'concept', 'construction', 'service', 'content',
             'joy', 'safety', 'product', 'complex', 'business', 'employee', 'offer', 'technology',
             'reform', 'absence', 'dog', 'stone', 'future', 'story', 'control', 'products', 'technique',
             'building', 'necessity', 'preparation', 'republic', 'economy', 'budget', 'village', 'element',
             'circumstance', 'victory', 'source', 'star', 'sister', 'practice', 'holding', 'pocket',
             'definition', 'function', 'army', 'commission', 'application', 'captain', 'employee', 'provision',
             'officer', 'surname', 'limit', 'election', 'scientist', 'bottle', 'theory', 'development', 'personality',
             'celebration', 'influence', 'reader', 'pleasure', 'responsibility', 'teacher', 'multitude',
             'feature', 'indicator', 'ship', 'impression', 'particularity', 'childhood', 'professor', 'past',
             'commander', 'corridor', 'support', 'meeting', 'illness', 'cell', 'statement', 'attempt', 'comparison',
             'calculation', 'deputy', 'committee', 'expression', 'health', 'ten', 'depth', 'student', 'second',
             'speed', 'error', 'director', 'surface', 'sensation', 'station', 'revolution', 'knee',
             'ministry', 'glass', 'height', 'grandmother', 'tube', 'master', 'behavior', 'capital', 'mechanism',
             'transfer', 'ability', 'approach', 'energy', 'existence', 'fulfillment', 'regret', 'substitute',
             'resource', 'birth', 'administration', 'cost', 'smile', 'artist', 'figure', 'subject', 'reaction',
             'list', 'photograph', 'journalist', 'violation', 'meeting', 'hospital', 'creature', 'property',
             'generation', 'animal', 'effort', 'difference', 'island', 'opponent', 'realization', 'page',
             'formation', 'inhabitant', 'beauty', 'plant', 'phenomenon', 'presence', 'clothing', 'armchair', 'patient',
             'university', 'tradition', 'December', 'palm', 'mixing', 'flower', 'October', 'occupation', 'September',
             'room', 'January', 'spectator', 'editorial office', 'factor', 'August', 'news', 'dependence', 'security',
             'equipment', 'concert', 'department', 'expense', 'exhibition', 'militia', 'transition', 'work',
             'homeland', 'property', 'camp', 'property', 'bed', 'apparatus', 'middle', 'client', 'industry',
             'conversation', 'legislation', 'sale', 'promotion', 'colonel', 'doubt', 'understanding', 'April',
             'code', 'mood', 'position', 'crime', 'ladder', 'installation', 'appearance', 'receipt',
             'sample', 'main thing', 'costume', 'value', 'duty', 'table', 'memory', 'horse', 'colleague',
             'organism', 'student', 'institution', 'discovery', 'characteristic', 'performance', 'defense', 'performance',
             'temperature', 'perspective', 'girlfriend', 'order', 'victim', 'restaurant', 'kilometer', 'sign',
             'industry', 'American', 'conclusion', 'east', 'exclusion', 'resolution', 'translation',
             'secretary', 'benefit', 'call', 'situation', 'official', 'agreement', 'detail', 'Russian', 'silence',
             'salary', 'gift', 'prison', 'competition', 'book', 'study', 'request', 'public', 'message',
             'threat', 'achievement', 'purpose', 'advertisement', 'portrait', 'glass', 'creativity', 'TV',
             'tool', 'concept', 'lieutenant', 'reality', 'familiar', 'conflict', 'negotiation', 'recording',
             'playground', 'consequence', 'cooperation', 'mirror', 'academy', 'chamber', 'need', 'November',
             'increase', 'trip', 'loss', 'February', 'event', 'acceptance', 'device', 'substance',
             'category', 'hotel', 'edition', 'association', 'darkness', 'humanity', 'wheel', 'danger',
             'resolution', 'impact', 'team', 'camera', 'investigation', 'candidate', 'relative', 'pressure',
             'presence', 'interaction', 'partner', 'engine', 'dignity', 'passion', 'trial', 'payment',
             'difference', 'driver', 'reduction', 'formula', 'capital', 'news', 'effect', 'governor', 'report',
             'murder', 'expert', 'bus', 'dress', 'communication', 'psychology', 'verification', 'procedure', 'worker',
             'repair', 'treatment', 'training', 'waiting', 'monument', 'root', 'observation', 'proof',
             'recognition', 'bed', 'owner', 'computer', 'engineer', 'old woman', 'rocket', 'top', 'graduation',
             'trade', 'youth', 'corps', 'disadvantage', 'essence', 'talent', 'efficiency', 'stripe',
             'main', 'review', 'investigator', 'description', 'editor', 'palace', 'care', 'table',
             'experiment', 'seal', 'ring', 'pistol', 'upbringing', 'boss', 'profession', 'gate', 'friendship',
             'end', 'magnitude', 'note', 'initiative', 'conscience', 'activity', 'credit', 'lord',
             'conference', 'ceiling', 'library', 'assistant', 'construction', 'metal', 'milk', 'prosecutor',
             'transport', 'poetry', 'connection', 'paint', 'distance', 'division', 'signal', 'atmosphere',
             'contact', 'cigarette', 'delight', 'gold', 'award', 'king', 'entrance', 'automatic machine', 'boy',
             'reading', 'settlement', 'witness', 'bet', 'surprise', 'turn', 'return', 'moment', 'status',
             'parameter', 'fairy tale', 'trend', 'breath', 'version', 'scale', 'monastery', 'mistress', 'exploitation',
             'communist', 'pension', 'buddy', 'explanation', 'producer', 'philosophy', 'power', 'commitment',
             'crisis', 'indication', 'apple', 'drug', 'reality', 'Moskvich', 'remainder', 'image',
             'transaction', 'essay', 'buyer', 'cost', 'line', 'unit', 'processing', 'championship']

# --- Алфавиты ---
alphabet_ru = set('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
alphabet_en = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# --- Языковые сообщения ---
messages = {
    'ru': {
        'new_game': "🎮 Слово из {n} букв. Начнём!",
        'input': "Введите букву или слово: ",
        'only_letters': "⚠️ Введите только буквы.",
        'wrong_alphabet': "⚠️ Буквы не из русского алфавита. Попробуйте снова.",
        'already_letter': "🔁 Уже вводили эту букву.",
        'no_letter': "❌ Буквы {ch} нет в слове.",
        'has_letter': "✅ Буква {ch} есть в слове!",
        'already_word': "🔁 Уже пробовали это слово.",
        'wrong_word': "❌ Неверное слово.",
        'wrong_format': "⚠️ Неверный формат ввода.",
        'win': "🎉 Победа! Слово: {word}",
        'lose': "💀 Проигрыш. Было слово: {word}",
        'tries_left': "Осталось попыток: {n}",
        'score': "🎯 Ваш счёт: {n} очков",
        'choose_lang': "Выберите язык / Choose language (ru/en): ",
        'choose_diff': "Выберите сложность:\n1 — Лёгкий\n2 — Средний\n3 — Сложный\nВаш выбор: ",
        'invalid_diff': "⚠️ Введите 1, 2 или 3.",
        'invalid_lang': "⚠️ Введите 'ru' или 'en'.",
        'play_again': "Сыграть ещё? (да/yes/нет/no): ",
        'final_score': "🏁 Финальный счёт: {n}. До встречи!",
        'invalid_answer': "⚠️ Введите 'да' / 'yes' или 'нет' / 'no'.",
        'goodbye': "До свидания! Спасибо за игру."
    },
    'en': {
        'new_game': "🎮 The word has {n} letters. Let's begin!",
        'input': "Enter a letter or full word: ",
        'only_letters': "⚠️ Please enter letters only.",
        'wrong_alphabet': "⚠️ Letters not in English alphabet. Try again.",
        'already_letter': "🔁 You've already tried this letter.",
        'no_letter': "❌ The letter {ch} is not in the word.",
        'has_letter': "✅ The letter {ch} is in the word!",
        'already_word': "🔁 You've already tried this word.",
        'wrong_word': "❌ Incorrect word.",
        'wrong_format': "⚠️ Invalid input format.",
        'win': "🎉 You guessed it! The word was: {word}",
        'lose': "💀 You lost. The word was: {word}",
        'tries_left': "Tries left: {n}",
        'score': "🎯 Your score: {n} points",
        'choose_lang': "Choose language / Выберите язык (ru/en): ",
        'choose_diff': "Choose difficulty:\n1 — Easy\n2 — Medium\n3 — Hard\nYour choice: ",
        'invalid_diff': "⚠️ Enter 1, 2 or 3.",
        'invalid_lang': "⚠️ Enter 'ru' or 'en'.",
        'play_again': "Play again? (yes/да/no/нет): ",
        'final_score': "🏁 Final score: {n}. Goodbye!",
        'invalid_answer': "⚠️ Enter 'yes' / 'да' or 'no' / 'нет'.",
        'goodbye': "Goodbye! Thanks for playing."
    }
}

# --- Отрисовка виселицы ---
def display_hangman(tries):
    stages = [
        '''
        _______
        |     |
        |     O
        |    \\|/
        |     |
        |    / \\
        | GAME OVER
        ''',
        '''
        _______
        |     |
        |     O
        |    \\|/
        |     |
        |    /
        |
        ''',
        '''
        _______
        |     |
        |     O
        |    \\|/
        |     |
        |
        |
        ''',
        '''
        _______
        |     |
        |     O
        |    \\|
        |     |
        |
        |
        ''',
        '''
        _______
        |     |
        |     O
        |     |
        |     |
        |
        |
        ''',
        '''
        _______
        |     |
        |     O
        |
        |
        |
        |
        ''',
        '''
        _______
        |     |
        |
        |
        |
        |
        | START
        '''
    ]
    return stages[tries]

# --- Выбор слова по сложности ---
def choose_word(words, difficulty):
    if difficulty == '1':
        filtered = [w for w in words if 4 <= len(w) <= 6]
    elif difficulty == '2':
        filtered = [w for w in words if 7 <= len(w) <= 9]
    else:
        filtered = [w for w in words if len(w) >= 10]
    return random.choice(filtered).upper() if filtered else random.choice(words).upper()

# --- Игровой процесс ---
def play(word, lang):
    m = messages[lang]
    alphabet = alphabet_ru if lang == 'ru' else alphabet_en
    word_completion = "_" * len(word)
    guessed_letters = []
    guessed_words = []
    tries = 6
    score_change = 0

    print(Fore.CYAN + m['new_game'].format(n=len(word)))
    print(display_hangman(tries))
    print('Word:', ' '.join(word_completion))
    print(Fore.YELLOW + m['tries_left'].format(n=tries))

    while "_" in word_completion and tries > 0:
        guess = input(Fore.BLUE + m['input']).upper()

        if not guess.isalpha():
            print(Fore.RED + m['only_letters'])
            continue
        if any(c not in alphabet for c in guess):
            print(Fore.RED + m['wrong_alphabet'])
            continue

        if len(guess) == 1:
            if guess in guessed_letters:
                print(m['already_letter'])
            elif guess not in word:
                print(m['no_letter'].format(ch=guess))
                tries -= 1
                guessed_letters.append(guess)
            else:
                print(m['has_letter'].format(ch=guess))
                guessed_letters.append(guess)
                word_completion = ''.join([guess if word[i] == guess else word_completion[i] for i in range(len(word))])
        elif len(guess) == len(word):
            if guess in guessed_words:
                print(m['already_word'])
            elif guess != word:
                print(m['wrong_word'])
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word
        else:
            print(Fore.RED + m['wrong_format'])

        print(display_hangman(tries))
        print('Word:', ' '.join(word_completion))
        print(Fore.MAGENTA + m['tries_left'].format(n=tries))

    if "_" not in word_completion:
        print(Fore.GREEN + m['win'].format(word=word))
        score_change = 10
    else:
        print(Fore.RED + m['lose'].format(word=word))
        score_change = -5

    return score_change

# --- Главный цикл ---
def main():
    score = 0
    while True:
        lang = input(messages['en']['choose_lang']).strip().lower()
        if lang not in ['ru', 'en']:
            print(messages['en']['invalid_lang'])
            continue

        m = messages[lang]
        words = words_ru if lang == 'ru' else words_en

        diff = input(m['choose_diff']).strip()
        if diff not in ['1', '2', '3']:
            print(m['invalid_diff'])
            continue

        word = choose_word(words, diff)
        score += play(word, lang)
        print(Fore.CYAN + m['score'].format(n=score))

        while True:
            again = input(m['play_again']).strip().lower()
            if again in ['да', 'yes']:
                break
            elif again in ['нет', 'no']:
                print(Fore.CYAN + m['final_score'].format(n=score))
                print(Fore.CYAN + m['goodbye'])
                return
            else:
                print(Fore.RED + m['invalid_answer'])

if __name__ == "__main__":
    main()