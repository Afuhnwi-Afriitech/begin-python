menu = list()
menu.append(["egg", "spam", "bacon"])
menu.append(["egg", "sussage", "bacon"])
menu.append(["egg", "spam"])
menu.append(["egg", "bacon", "spam"])
menu.append(["egg", "bacon", "sussage", "spam"])
menu.append(["spam", "bacon", "sussage", "spam"])
menu.append(["spam", "egg", "spam", "spam", "bacon", "spam"])
menu.append(["span", "egg", "sussage", "spam"])
# print(menu)

for meal in menu:
    if "spam" not in meal:
        print(meal)
        for item in meal:
            print(item, end=" ")
