# drone_list = ["DJI Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro", "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2", "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

# drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

# vendors_names = ["DJI", "Autel", "Parrot", "Ryze", "Eachine"]

#в drone по очереди попадает каждый дрон из списка drone_list

#TODO1
#выведите все дроны производителя, название которого введет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. правильный вариант названия: DJI, Autel

#TODO2
#подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine

#TODO3
#выведите все дроны из списка, которые нужно регистрировать (масса больше 150 г), и подсчитайте их количество. 
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь

#TODO4
#для каждого дрона из списка выведите, нудно ли согласовывать полет при следующих условиях:
#высота 100 м - не надо, flight_type = 0 
# полет над населенным пунктом - надо, flight_type = 1 
# вне закрытых зон - не надо, flight_type = 2 
# в прямой видимости  - не надо,  flight_type = 3
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

#TODO5*
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine


def create_vendor_product_dict(drone_list, vendors_list):
    vendors_dict ={
        vendor.lower():{"name":vendor, "products":[]} 
        for vendor in vendors_list    
    }

    for drone_name in drone_list:
        for vendor in vendors_list:
            if vendor.lower() in drone_name.lower():
                drone_name_list = drone_name.split(" ")
                drone_name_list[0] = vendor
                new_drone_name = " ".join(part for part in drone_name_list)

                vendors_dict[vendor.lower()]["products"].append(new_drone_name)

    return vendors_dict



def task1(vendors_asks, drone_list, vendors_list):

    vendors_asks = [vendor.lower() for vendor in vendors_asks]
    vendors_asks = list(set(vendors_asks))
    vendors_product_dict = create_vendor_product_dict(drone_list, vendors_list)

    for vendor in vendors_asks:

        vendor = vendor.lower()
        if vendor in vendors_product_dict:
            products = vendors_product_dict[vendor]["products"]
            vendor_name = vendors_product_dict[vendor]["name"]
            print(f"Vendor {vendor_name} have {len(products)} products \n")
            for product in products:
                print("\t", product, "\n")



def task2(drone_list, vendors_list):

    vendors_product_dict = create_vendor_product_dict(drone_list, vendors_list)

    for vend_dict in vendors_product_dict.values():

        name = vend_dict["name"]
        products_num = len(vend_dict["products"])
        print(f"Vendor {name} have {products_num} products") 


def task3(drone_list, drone_weights):

    products_map = zip(drone_list, drone_weights)
    must_be_registered = []
    mustnt_be_registered = []

    for product in products_map:
        if product[1]>150:
            print(f"Drone {product[0]}, with weight {product[1]} must be registered")
            must_be_registered.append(product)
        else:
            print(f"Drone {product[0]}, with weight {product[1]} can be not registered")
            mustnt_be_registered.append(product)

    # return must_be_registered, mustnt_be_registered


def task4(drone_list, drone_weights, flight_mode):

    products_map = zip(drone_list, drone_weights)
    must_be_registered = []
    mustnt_be_registered = []

    for product in products_map:
        if product[1]>150 and flight_mode==1:
            print(f"Drone {product[0]}, with weight {product[1]} must be registered in flight mode {flight_mode}")
            must_be_registered.append(product)
        else:
            print(f"Drone {product[0]}, with weight {product[1]} can be not registered in flight mode {flight_mode}")
            mustnt_be_registered.append(product)



def create_vendor_product_dict_no_vend(drone_list, vendors_list):
    vendors_dict ={
        vendor.lower():{"name":vendor, "products":[]} 
        for vendor in vendors_list    
    }

    for drone_name in drone_list:
        for vendor in vendors_list:
            if vendor.lower() in drone_name.lower():
                drone_name_list = drone_name.split(" ")
                del drone_name_list[0]
                new_drone_name = " ".join(part for part in drone_name_list)

                vendors_dict[vendor.lower()]["products"].append(new_drone_name)

    return vendors_dict


def task5(vendors_asks, drone_list, vendors_list):

    vendors_asks = [vendor.lower() for vendor in vendors_asks]
    vendors_asks = list(set(vendors_asks))
    vendors_product_dict = create_vendor_product_dict_no_vend(drone_list, vendors_list)

    for vendor in vendors_asks:

        vendor = vendor.lower()
        if vendor in vendors_product_dict:
            products = vendors_product_dict[vendor]["products"]
            vendor_name = vendors_product_dict[vendor]["name"]
            print(f"Vendor {vendor_name} have {len(products)} products \n")
            for product in products:
                print("\t", product, "\n")