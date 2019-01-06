import os


class Todo():

    def __init__(self):
        self.tasks = []
        self.screenWelcome()

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def screenError(self, error):
        self.clear()
        print(f"\n\n{'*'*60}")
        input(f"\n\t{error}")

    def screenWelcome(self):
        self.clear()
        print("\n\t\t\tWelcome")
        print("*"*60)
        print("""
                1.) Add Task
                2.) See Task
                3.) Exist System
        """)
        print("*"*60)
        self.option(1, input())

    def exit(self):
        self.clear()
        print("*"*60)
        print("\n\t\t\tBye\n")
        print("*"*60)
        exit()

    def option(self, types, value, arg=""):
        if types == 1:
            option = {
                "1": self.screenAdd,
                "2": self.screenSeeTask,
                "3": self.exit
            }
        elif types == 2:
            option = {
                "1": self.updateTask,
                "2": self.deleteTask,
                "3": self.screenWelcome
            }
        try:
            if arg != "":
                print(option[value](arg))
            else:
                print(option[value]())
        except KeyError:
            self.screenError("You must select a valid option")
            if types == 1:
                self.screenWelcome()
            if types == 2:
                self.screenSeeTask()

    def screenAdd(self):
        self.clear()
        print("\n\t\t\tAdd Task ")
        print("*"*60)
        name = ""
        while name == "":
            name = input("\nName Of Task: \t")
        new_task = {
            "name": name,
            "ready": False
        }
        self.saveTask(new_task)
        input("Successfully Saved Task")
        self.screenSeeTask()

    def screenSeeTask(self):
        self.clear()
        print("\n\t\t\tSee Task ")
        print("*"*60)
        if len(self.tasks) != 0:
            for index, task in enumerate(self.tasks):
                pk = task.get("pk")
                name = task.get("name")
                ready = bool(task.get("ready"))
                print(
                    f"\n{index+1}.) id: {pk} Name: {name} Ready: {'Yes' if ready else 'No'}")
            print("\n1.) Ready \t 2.) Delete \t 3.) Return")
            option = input()
            if option == "3":
                self.option(2, option)
            else:
                pk = ""
                while pk == "":
                    try:
                        pk = int(input("enter task id: \t"))
                        self.option(2, option, pk)
                    except Exception:
                        pass
        else:
            self.screenError("There aren't registered task")
            self.screenWelcome()

    def updateTask(self, pk):
        for task in self.tasks:
            if task.get('pk') == pk:
                task['ready'] = True
        input("\n\t\tEnd Task")
        self.screenSeeTask()

    def deleteTask(self, pk):
        for index, task in enumerate(self.tasks):
            if task.get('pk') == pk:
                del self.tasks[index]
        input("\n\t\tDelete Task")
        self.screenSeeTask()

    def saveTask(self, data):
        data['pk'] = len(self.tasks) + 1
        self.tasks.append(data)


# if __name__ == "__main__":
#     Todo()
