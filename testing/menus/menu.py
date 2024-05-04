from consolemenu import *
from consolemenu.items import *

menu = ConsoleMenu("VirusTotal Bulk Hash Lookup Tool", "Subtitle")

menu_item = MenuItem("Menu Item")

menu.append_item(menu_item)

menu.show()
