import unreal

def ListMenu(num = 1000):
    menuList = set()
    for i in range(num):
        obj = unreal.find_object(None, "/Engine/Transient.ToolMenus_0:RegisteredMenu_%s" % i)
        if not obj:
            obj = unreal.find_object(None, f"/Engine/Transient.ToolMenus_0:ToolMenu_{i}") # for backwards compatibility

            if not obj:
                continue

        menuName = str(obj.menu_name)
        if menuName == "None":
            continue

        menuList.add(menuName)

    return list(menuList)

print(ListMenu())