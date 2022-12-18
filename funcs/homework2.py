import json

# Напоминание: вам понадобится материал лекций:
# 3 - Списки и кортежи
# 4 - Словари и множества
# 7 и 8 - Классы
# 9 - Работа с файлами

# =====================================
# ЗАДАНИЕ 1: Работа с файлами
# =====================================
# TODO 1-1
#  Прочитайте данные из файла pilot_path.json (лекция 9)

# ВАШ КОД:
def json_reader(filepath):

    with open(filepath, 'r') as jsonfile:
        content = json.load(jsonfile)

    return content


# =====================================
# ЗАДАНИЕ 2: Расчет статистик
# =====================================
# TODO 2-1) Подсчитайте, сколько миссий налетал каждый пилот. Выведите результат в порядке убывания миссий
# ИНФОРМАЦИЯ:
        
# структура данных в файле: {"имя_пилота": "список_миссий":[миссия1, ...]]
# структура одной миссии: {"drone":"модель_дрона", "mission":[список точек миссии]}
# у пилотов неодинаковое количество миссий (и миссии могут быть разной длины). у каждой миссии - произвольная модель дрона

# РЕЗУЛЬТАТ:
# Пилоты в порядке убывания количества миссий: {'pilot3': 6, 'pilot8': 6, 'pilot6': 5, 'pilot2': 5, 'pilot7': 4, 'pilot9': 3, 'pilot5': 3, 'pilot4': 2, 'pilot1': 1}

# ВАШ КОД:

def count_missions(filepath):

    pilots_dict = json_reader(filepath)

    pilot_missions_num = {}

    for pilot in pilots_dict.keys():

        pilot_missions_num[pilot] = len(pilots_dict[pilot]["missions"])

    pilot_missions_num = dict(sorted(pilot_missions_num.items(), key=lambda pilot: pilot[1]))

    return pilot_missions_num

# TODO 2-2) Получите и выведите список всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: внутри print используйте str.join(), чтобы соединить элементы списка (множества)

# РЕЗУЛЬТАТ:
# Полеты совершались на дронах следующих моделей: DJI Mavic 2 Pro, DJI Mavic 3, DJI Inspire 2, DJI Mavic 2 Zoom, DJI Mavic 2 Enterprise Advanced

# ВАШ КОД:
def take_drones_models(filepath):

    pilots_dict = json_reader(filepath)

    drones_names = []

    for pilot_dict in pilots_dict.values():
        for mission in pilot_dict["missions"]:
            drone_name = mission["drone"]
            if not drone_name in drones_names:
                drones_names.append(drone_name)

    return drones_names


# вывод результата (допишите код)
# print(f'Полеты совершались на дронах следующих моделей: {", ".join(take_drones_models(filepath))}')

# TODO 2-3) Получите список миссий для каждой модели дронов, которые были в файле pilot_path.json,
# и выведите на экран модель дрона и количество миссий, которые он отлетал

# РЕЗУЛЬТАТ:
# Дрон DJI Inspire 2 отлетал 6 миссий
# Дрон DJI Mavic 2 Pro отлетал 6 миссий
# Дрон DJI Mavic 2 Enterprise Advanced отлетал 10 миссий
# Дрон DJI Mavic 3 отлетал 4 миссий
# Дрон DJI Mavic 2 Zoom отлетал 9 миссий

# ВАШ КОД:
def count_missions_for_drone(filepath):

    pilots_dict = json_reader(filepath)

    drones_missions_count = {}

    for pilot_dict in pilots_dict.values():
        for mission in pilot_dict["missions"]:
            drone_name = mission["drone"]
            if not drone_name in drones_missions_count:
                drones_missions_count[drone_name] = 1
            else:
                drones_missions_count[drone_name] += 1

    return drones_missions_count



# вывод результата (допишите код)
# drones_miss_num = count_missions_for_drone(filepath)

# for drone, missions_num in drones_miss_num.items():
#     print(f'Дрон {drone} отлетал {missions_num} миссий')

# =====================================
# ЗАДАНИЕ 3: Создание классов
# =====================================
# Для вас уже написаны заготовки классов Aircraft и UAV
# TODO 3-1) Добавьте в класс UAV защищенный атрибут _=_missions (тип - список списков [[], []]), куда вы будете сохранять все миссии, которые отлетал беспилотник
# TODO 3-2) При помощи декоратора @property сделайте возможность чтения и записи миссий в этот атрибут (лекция 8)
# TODO 3-3) Создайте в классе UAV публичный метод count_missions, который возвращает количество миссий (лекция 7)
# TODO 3-4) Создайте класс MultirotorUAV - наследник классов Aircraft и UAV (лекция 7)

# ВАШ КОД (дополните то, что нужно в классах):
class Aircraft:
	def __init__(self, weight):
		self._weight = weight

class UAV:
    def __init__(self):
        self._has_autopilot = True
        self._missions = []

    @property
    def missions(self):
        return self._missions

    @missions.setter
    def missions(self, mission):
        self._missions.append(mission)

    def count_missions(self):
        return len(self._missions)


class MultirotorUAV(Aircraft, UAV):
    def __init__(self, weight, model, brand):
        super().__init__(weight)
        UAV.__init__(self)
        self._model = model
        self._brand = brand

    def get_info(self):

        print(
            f"Model :\n\t",
            f"vendor {self._brand} model {self._model}\n\t",
            f"weight {self._weight}\n\t",
            f"missions num {len(self._missions)}"
        )

    def get_model(self):
        return self._model

# =====================================
# ЗАДАНИЕ 4: Работа с экземплярами классов
# =====================================
# TODO 4-1) Создайте экземпляры класса MultirotorUAV для всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: созданные экземпляры класса MultirotorUAV сохраните в список для последующего использования
# TODO 4-2) При создании каждого экземпляра задайте ему как приватные атрибуты массу и производителя из справочника дронов drone_catalog в соответствии с моделью дрона
# TODO 4-3) А также добавьте ему миссии, найденные для этой модели дрона на шаге 2-3
# Напоминание: миссии находятся в атрибуте missions (с декоратором, и поэтому он публично доступен) в классе UAV

# каталог дронов уже готов для вас:
drone_catalog = {
	"DJI Mavic 2 Pro": {"weight":903, "brand":"DJI"},
	"DJI Mavic 2 Zoom": {"weight":900, "brand":"DJI"},
	"DJI Mavic 2 Enterprise Advanced": {"weight":920, "brand":"DJI"},
	"DJI Inspire 2": {"weight":1500, "brand":"DJI"},
	"DJI Mavic 3": {"weight":1000, "brand":"DJI"}
}

# ВАШ КОД:
drones = {
    name: MultirotorUAV(chars['weight'], name, chars["brand"])
    for name, chars in drone_catalog.items()
}




# TODO 4-4
# Напишите код, который выводит информацию по заданной модели дрона. Состав информации: масса, производитель, количество отлетанных миссий
# (название модели пользователь вводит с клавиатуры в любом регистре, но без опечаток)
# Подсказка: для этого вам необходимо вернуться в ЗАДАНИЕ 3 и добавить в класс два публичных метода: get_info(), который выводит нужную информацию,
# и get_model, который позволит получить название модели дрона

# РЕЗУЛЬТАТ:
# Информация о дроне DJI Mavic 2 Pro: масса 903, производитель DJI, количество миссий 6

# ВАШ КОД:
# user_unput = input("Введите модель дрона (полностью) в любом регистре\n")

# drone = drones[user_unput]

# print(
#     drone.get_info()
# )