import unreal

def main():
    menu = unreal.ToolMenus.get()
    mainMenu = menu.find_menu("LevelEditor.MainMenu")
    customMenu = mainMenu.add_sub_menu("Custom Menu", "Python Automation", "StartingProjName", "Starting Project Folders")
    menu.refresh_all_widgets()

    newFolders = CreateProjectFolders()
    newFolders.init_entry(
        owner_name = customMenu.menu_name,
        menu = customMenu.menu_name,
        section = "Create Folders",
        name = "Create Project Folders",
        label = "Create Project Folders",
        tool_tip = "Custom Script Entry"
    )
    newFolders.register_menu_entry()
    



@unreal.uclass()
class CreateProjectFolders(unreal.ToolMenuEntryScript):
    @unreal.ufunction(override = True)
    def execute(self, context):
        assetLibrary = unreal.EditorAssetLibrary()
        myFiles = "/Game/_MyFiles"

        assetLibrary.make_directory(myFiles)

        assetFolder = "/Game/_MyFiles/Assets"
        bpFolder = "/Game/_MyFiles/Blueprints"
        levelFolder = "/Game/_MyFiles/Levels"
        matFolder = "/Game/_MyFiles/Materials"

        assetLibrary.make_directory(assetFolder)
        assetLibrary.make_directory(bpFolder)
        assetLibrary.make_directory(levelFolder)
        assetLibrary.make_directory(matFolder)


main()


# -------------------------- This function was used to find label names and print them out, if you want to put the starting folders
# -------------------------- tool somewhere else, you can run this to find a new name for the mainMenu = menu.find_menu("Put new name here")

# def ListMenu(num = 1000):
#     menuList = set()
#     for i in range(num):
#         obj = unreal.find_object(None, "/Engine/Transient.ToolMenus_0:RegisteredMenu_%s" % i)
#         if not obj:
#             obj = unreal.find_object(None, f"/Engine/Transient.ToolMenus_0:ToolMenu_{i}") # for backwards compatibility

#             if not obj:
#                 continue

#         menuName = str(obj.menu_name)
#         if menuName == "None":
#             continue

#         menuList.add(menuName)

#     return list(menuList)

# print(ListMenu())