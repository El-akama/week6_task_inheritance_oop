
# task1
# class ContactList(list):

#     def search_by_name(self, name):
#         some_list = []
#         for n in self:
#             if n == name:
#                 some_list.append(n)
#             else:
#                 continue
#             return some_list

# all_contacts = ContactList(['name1', 'name2', 'name3', 'name4'])

# a = all_contacts.search_by_name('name2')
# print(a)


# task2
# class User:

#     first_name = 'Samy'
#     last_name = "Well"
#     age = "25"
#     password = "2468"
    
#     def describe_user(self):
#         self.first_name
#         self.last_name
#         self.age
#         self.password

#     def greet_user(self):
#         print(f'Hello {self.first_name} {self.last_name}')


# class Admin(User):
#     privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

#     def show_privileges(self):
#         return f"у админа такие привилегии {Admin.privileges}"

# u = User()
# u.describe_user()
# u.greet_user()
# admin = Admin()
# admin.first_name = 'Admin'
# a = admin.show_privileges()
# admin.describe_user()
# admin.greet_user()
# print(a)


# task#3
# class House:
#     type_house = '2-х этажный'
#     area_house = 40
#     ost_area = 0
#     meb_list = {"кровать": 5, "шкаф": 3, "стол": 2}

#     area = 0
#     for a in meb_list.values():
#         area += a
#     ost_area = area_house - area

#     def info_hause(self):
#         print(f"Тип дома {self.type_house}")
#         print(f"Общая площадь дома {self.area_house} км2")
#         print(f"Оставшаяся площадь дома {self.ost_area}")
#         print(f"Мебель в доме {self.meb_list}")

# h = House()
# h.info_hause()


# task4
# def funnyString(s):
#     res = s[::-1]
#     for i in range(0, len(s)):
#         if abs(ord(s[i]) - ord(s[i-1])) != abs(ord(res[i]) - ord(res[i-1])):
#             return "Not Funny"
    
#     return "Funny"

# print(funnyString("zscg"))