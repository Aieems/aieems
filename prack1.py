import time
import random
def slow_print(text):
  """Функция для постепенного вывода текста."""
  for char in text:
    print(char, end='', flush=True)
    # time.sleep(0.05)
  print("\n") # Переход на новую строку после завершения вывода

# Класс для персонажа
class Character:
  def __init__(self, name, health): # Исправлено на __init__
    self.name = name
    self.health = health

# Создаем основных персонажей
fox = Character("Лис", 100)
elly = Character("Элли", 100)
opponent = Character("Глава производства", 100)


class Fox:
    def __init__(self):
        self.health = 100
        self.inventory = []  # Инвентарь для хранения предметов

def add_item(item):
        fox.inventory.append(item)
        slow_print(f"Вы добавили {item} в инвентарь.")

def use_potion():
        if 'зелье' in fox.inventory:
            fox.health += 20  # Восстанавливаем здоровье
            fox.inventory.remove('зелье')  # Удаляем зелье из инвентаря
            slow_print("Вы использовали зелье. Ваше здоровье восстановлено на 20.")
        else:
            slow_print("У вас нет зелья!")

def use_potion1():
    usepotion = input("Хотите выпить зелье здоровья или оставить на потом? (сейчас/потом): ")
    if usepotion.lower() == 'сейчас':
        use_potion() # Вызов метода правильно

    else:
        slow_print("Вы оставили зелье на потом")

def use_gun():
    if 'ружье' in fox.inventory:
        return True  # У вас есть ружье, можно использовать
    return False

fox = Fox()  # Создаем экземпляр мистера Лиса

# Основная игра
def main_game():
    scena_1 = [
        "И вот как ни в чем не бывало мистер Лис со своей женой Элли пошли воровать еду.",
        "Ведь это их работа, которой они зарабатывают себе на жизнь, получая еду и деньги."
    ]
    
    for sentence in scena_1:
        slow_print(sentence)

    slow_print("ИГРА: БЕСПОДОБНЫЙ МИСТЕР ЛИС")
    slow_print("ГЛАВА 1: ВОРОВСТВО")
    
    name_Fox = input("Введите имя мистера лиса: ")
    

    scena_1_1 = [
        "Хм, дорогая, к кому ты сегодня хочешь наведаться за едой?",
        "Есть 3 человека, мне кажется, можно пойти к..."
    ]
    
    for sentence in scena_1_1:
        slow_print(f"{name_Fox}: {sentence}")  # Объединение строки перед выводом
    
      
    people_list = {
       "1.Мирен": {"описание": "не хитрый человек, но обладает большой массой. Ест очень много, поэтому он высокий", "Производит": "индейку", "Сила": "10/10", "Ум/хитрость": "4/10"},
       "2.Толик": {"описание": "чуть хитрее, очень низкий, но быстрый и ловкий.", "Производит": "овощи", "Сила": "7/10", "Ум/хитрость": "7/10"},
       "3.Геральд": {"описание": "самый хитрый из всех, хлиплый дрыщь, который обладает большим умом.", "Производит": "сидр и яблоки", "Сила": "4/10", "Ум/хитрость": "10/10"}}
   
    for predmet, info in people_list.items():
        print(f"{predmet} ({info['описание']})")
        print(f"  Производит: {info['Производит']}")
        print(f"  Сила: {info['Сила']}")
        print(f"  Ум/хитрость: {info['Ум/хитрость']}")
    

    name_people = input("Выберете человека, к которому пойдете воровать(напишите цифру): ")
    if name_people == "1":
        turkey_heist()
    elif name_people == "2":
        vegetables_heist()
    elif name_people == "3":
        cider_heist()
    else:
        slow_print("Неверный выбор, попробуйте снова.")
        return 
    
    

    

def turkey_heist():
    slow_print("Вы подошли к заводу индейки.")
    slow_print("Уже из далека чуствовался приятный запах свежей индейки, что вы хотели быстрее проникнуть туда.")
    path_choice()

def vegetables_heist():
    slow_print("Вы подошли к овощному заводу.")
    slow_print("Самое то для ужина под мясо, будет дополнять вкус, и есть витамины.")
    path_choice()

def cider_heist():
    slow_print("Вы подошли к заводу сидра.")
    slow_print("Этим прекрасным напитком вы сможете долго наслаждаться на праздниках и не только, как дополнение яблоки очень вкусные.")
    path_choice()


def path_choice():
    slow_print("Вот два варианта пути, кототрые ведут к главному человеку")
    path_list = {
       "1.Длинный": {"описание": "живописный путь, очень красивый и расслабляющий"},
       "2.Короткий": {"описание": "короткий и быстрый, вряд ли что-то встретите интересное"}}
    for predmet, info in path_list.items():
        print(f"{predmet} ({info['описание']})")
    path = input("А теперь выберете путь, по которому пойдете(напишите цифру): ")
    
    if path == "1":
        long_path()
    elif path == "2":
        short_path()
    else:
        slow_print("Неверный выбор, попробуйте снова.")
    path_choice()


def long_path():
  slow_print("Ну что, Элли, пойдем тогда по красивой дорожке, надеюсь, что нибудь увидим.")
  slow_print("По дороге вы замечаете какие-то блестящие предметы в траве...")
  
  choice = input("1. Проверить, что это\n2. Игнорировать и идти дальше\nВыберите (1 или 2): ")
  
  if choice == "1":
    slow_print("Вы подошли ближе и увидели зелье здоровья!")
    slow_print("Элли сказала: 'Это может пригодиться, если нас поймают.'")
    slow_print("Вы решили забрать зелье с собой.")
    add_item('зелье')
    
    slow_print("Вы продолжаете путь и вскоре достигаете производства.")
    steal_from_factory()
  else:
    slow_print("Вы проигнорировали блестящие предметы и продолжили путь.")
    steal_from_factory()


def short_path():
  slow_print("Ну что, Элли, пойдем тогда по короткой дорожке, надеюсь, быстро дойдем.")
  slow_print("Спустя некоторое время вы находите старый склад.")
  
  choice = input("1. Исследовать склад\n2. Игнорировать и двигаться дальше\nВыберите (1 или 2): ")
  
  if choice == "1":
    slow_print("Вы заходите в склад и находите старое ружье.")
    slow_print("Элли говорит: 'Это отличное средство для защиты!'")
    slow_print("Вы берете ружье с собой на всякий случай.")
    add_item('ружье')
    steal_from_factory()
  else:
    slow_print("Вы решили не отвлекаться и продолжили путь, но вскоре оказались на углу улицы.")
    steal_from_factory()
  
def steal_from_factory():
  slow_print("Вы и Элли начали красть вещи на производстве.")
  slow_print("Вдруг из-за неосторожности на вас падает решетка.")
  slow_print("Элли в панике говорит: 'Что нам делать?! Я беременна, обещай мне, что ты больше не будешь воровать!'")

  promise = input("Вы: 1. 'Я обещаю!'\n 2. 'Сейчас не время!' \nВыберите (1 или 2): ")

  if promise == "1":
    slow_print("Элли успокаивается и говорит: 'Спасибо... Я верю тебе.'")
    puzzle_solution()
  else:
    slow_print("Элли расстраивается и говорит: 'Я не могу поверить в это! Нам нужно выбраться!'")
    fox.health -= 20  # Потеря здоровья за неисполнение обещания
    slow_print("Ваше здоровье: {}".format(fox.health))
    use_potion1()
           
    
    puzzle_solution()

def puzzle_solution():
  slow_print("Вам нужно решить головоломку, чтобы выбраться из ловушки.")
  slow_print("Ваша задача — активировать три переключателя по порядку.")

  switches = [1, 2, 3]
  random.shuffle(switches) # перемешиваем номера переключателей
  print("\nПереключатели: ", switches)

  for i in range(3):
    choice = int(input(f"Нажмите переключатель {i + 1}: "))
    if choice == switches[i]:
      slow_print(f"Вы успешно активировали переключатель {choice}!")
    else:
      slow_print("Неудача! Вы не выбрали правильный переключатель.")
      slow_print("Вам не удалось сбежать, не повредив себя. Вам оторвало кусочек хвоста.")
      fox.health -= 30  # Потеря здоровья 
      use_potion1()
      setup_next_part()
      
  slow_print("Вы активировали все переключатели!")
  slow_print("Решетка поднимается, и вы выбегаете на свободу!")
  setup_next_part()

def puzzle_solution2():
  slow_print("Вам нужно собрать пули, решив головоломку, чтобы ружье выстрелило.")
  slow_print("Ваша задача — активировать три переключателя по порядку.")

  switches = [1, 2, 3]
  random.shuffle(switches) # перемешиваем номера переключателей
  print("\nПереключатели: ", switches)

  for i in range(3):
    choice = int(input(f"Нажмите переключатель {i + 1}: "))
    if choice == switches[i]:
      slow_print(f"Вы успешно активировали переключатель {choice}!")
    else:
      slow_print("Неудача! Вы не выбрали правильный переключатель.")
      slow_print("Вам не удалось выстрелить, теперь вы сражаетесь.")
      fox.health -= 30  # Потеря здоровья 
      use_potion1()
      setup_next_part()
      
  slow_print("Вы активировали все переключатели!")
  slow_print("Решетка поднимается, и вы выбегаете на свободу!")
  setup_next_part()

def setup_next_part():
    slow_print("ГЛАВА 2: ПАРУ ЛЕТ СПУСТЯ")
    slow_print("Прошло несколько лет. У мистера Лиса и Элли родился сын.")
    slow_print("Они решили переехать в дом в дереве, так как в норке лису очень надоело жить, и хотели житьс красивым видом ")
    slow_print("Но он находится в опасном районе.")
    slow_print("С одной стороны дома расположены три завода людей.")
    
    decision = input("Вы хотите: 1. Попробовать украсть что-нибудь, чтобы обеспечить семью\n2. Преждевременно переехать, не рискуя\nВыберите (1 или 2): ")
    
    if decision == "1":
        slow_print("Вы решаете украсть еще раз тайно от жены.")
        steal_for_family()
    else:
        slow_print("Вы решаете не рисковать и перебраться с семьей в безопасное место, но влияет на вашу психику.")
        slow_print("Вам не нравится ваша жизнь и доживаете последние годы в грусти.")
        viborpup = input("Вам точно этого хочется? Пройти выбор заново или оставить все как есть(заново/пройти): ")
        if viborpup == "заново":  
            setup_next_part()
        else:
            slow_print("Спасибо за игру.")


def steal_for_family():
    slow_print("Вы стараетесь действовать крайне осторожно, однако вы не один.")
    slow_print("Люди знают, где вы живете, и готовятся к вашему приходу.")

    encounter()



def encounter():
    slow_print("Вы столкнулись с врагом!")
    if 'ружье' in fox.inventory:
        use_gun()
        slow_print("Вы используете ружье в сражении!")
        puzzle_solution2()
        slow_print("Враг повержен!")
        slow_print("Вы успешно сразились с главой завода и забрали нужные вещи!")
        slow_print("Ваши усилия обеспечили семью.")
    else:
        slow_print("Вы не имеете оружия, готовьтесь к битве!")
        battle()
        
    

def battle():
    slow_print("Глава приближается и собирается наносить по вам удар.")
    if fox.health > 0 and opponent.health > 0:
        slow_print(f"Здоровье лиса: {fox.health}")
        slow_print(f"Здоровье врага: {opponent.health}")

        choice = input("Выберите действие: (1) Увернуться от удара, (2) Напасть в ответ, (3) Укусить в ногу: ")
        
        if choice == '1':
            slow_print(f"{fox.name} решил увернуться от сражения.")
            slow_print("Это было зря. Вы не успели увернуться, и вас пнули ногой об стену.")
            slow_print("Вы потеряли 30 хп.")
            slow_print(f"Здоровье: {fox.health}")
            fox.health -= 30  # Потеря здоровья 
            use_potion1()
            slow_print(str(fox.health))

            battle2_3()
        
        elif choice == '2':
            slow_print("Вам получилось напасть на врага и снести ему 50хп.")
            opponent.health -= 50
            slow_print(str(opponent.health))
            battle2()

        elif choice == '3':
            slow_print("Вам получилось укусить врага и снести ему 50хп. Теперь он храмает и не может быстро двигаться")
            opponent.health -= 50
            slow_print(str(opponent.health))
            battle2_2()
    else:
        die_fox()


def battle2_2():
    if fox.health > 0 and opponent.health > 0:
        slow_print("Глава снова собирается наносить по вам удар, но учтите, что он медленне.")
        slow_print(f"Здоровье лиса: {fox.health}")
        slow_print(f"Здоровье врага: {opponent.health}")

        choice = input("Выберите действие: (1) Попробовать увернуться , (2) Вцепиться когтями, (3) Заскалиться, пытаясь напугать: ")
        
        if choice == 1:
            slow_print("Вам получилось напасть на врага и снести ему еще 50хп.")
            opponent.health -= 50
            slow_print(str(opponent.health))
            die_glava()
            
        
        elif choice == 2:
            slow_print("Вам получилось напасть на врага и снести ему еще 50хп.")
            opponent.health -= 50
            slow_print(str(opponent.health))
            die_glava()


        elif choice == 3:
            
            slow_print(f"{fox.name} решил напугать врага.")
            slow_print("Так как глава был медленне, вы дали ему шанс вас ударить.")
            fox.health -= 40  # Потеря здоровья 
            use_potion1()
            slow_print(str(fox.health))
    else:
        die_fox()

def battle2():
    if fox.health > 0 and opponent.health > 0:
        slow_print("Глава снова собирается наносить по вам удар.")
        slow_print(f"Здоровье лиса: {fox.health}")
        slow_print(f"Здоровье врага: {opponent.health}")

        choice = input("Выберите действие: (1)  Напасть еще раз, (2) Укусить за руку, (3) Спрятаться за куст: ")
        
        if choice == 1:
            slow_print("Вам получилось напасть на врага и снести ему еще 50хп.")
            opponent.health -= 50
            slow_print(str(opponent.health))
            die_glava()
            
        
        elif choice == 2:
            slow_print("Укусив главу, он не смог вырваться, и вы снесли ему еще 50хп.")
            opponent.health -= 50
            slow_print(str(opponent.health))
            die_glava()


        elif choice == 3:
            slow_print("Вас быстро нашли, так как вы яркого цвета, и нанесли по вам удар -40хп.")
            fox.health -= 40  # Потеря здоровья
            use_potion1()
            slow_print(str(fox.health))
    else:
        die_fox()

def battle2_3():
    if fox.health > 0 and opponent.health > 0:
        slow_print("Глава снова собирается наносить по вам удар.")
        slow_print(f"Здоровье лиса: {fox.health}")
        slow_print(f"Здоровье врага: {opponent.health}")

        choice = input("Выберите действие: (1) На полу валяется пульт, попробовать?  , (2) Зарычать, напугав, (3) Используя все свои силы, укусить еще раз: ")
        
        if choice == 1:
            slow_print("Вы нажали на пульт, от туда резко выскочила маленькая бомбочка и взорволась возле человека. Он испугался, и вы снесли ему 50хп")
            opponent.health -= 50
            slow_print(str(opponent.health))
            die_glava()
            
        
        elif choice == 2:
            slow_print("Вам снесли 40хп, бедный лис.")
            fox.health -= 40  # Потеря здоровья 
            use_potion1()
            slow_print(str(fox.health))
            


        elif choice == 3:
            slow_print("Используя все ваши силы, вы снесли ему еще 50хп.")
            opponent.health -= 50
            slow_print(str(opponent.health))
            die_glava()
    else:
        die_fox()

def die_glava():
    slow_print("Вы нанесли решающий удар по врагу, и он больше не смог сражаться, поэтому убежал.")
    slow_print("Победа за вами!!!!. Теперь ваша семья живет мирно и счастливо")

def die_fox():
    slow_print("Вы получили смертельный удар.")
    slow_print("К сожалению вы мерли.")
    choice2 = input("Вы можете попробовать переиграть(заново/закончить): ")
    if choice2 == "заново":
        battle()
    else:
        slow_print("GAME OVER")

main_game()