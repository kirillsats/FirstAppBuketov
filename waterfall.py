tasks = []


def add_task(task):
    tasks.append(task)


def remove_task(task_name):
    if task_name in tasks:
        tasks.remove(task_name)
        print("Ülesanne " + task_name + " on kustutatud.")
    else:
        print("Ülesannet " + task_name + " ei leitud.")


def show_tasks():
    if tasks:
        print("Ülesanded:")
        for task in tasks:
            print("- " + task)
    else:
        print("Ülesandeid ei ole.")


def main():
    while True:
        print('1 - Lisa ülesanne \n2 - Kustuta ülesanne \n3 - Ülevaade ülesannetest \n4 - Välju')
        user_input = input("Mida sa tahad teha? ")

        if user_input == '1':
            task = input("Sisesta ülesande: ")
            add_task(task)
        elif user_input == '2':
            task = input("Sisesta ülesande nimi, mida soovid kustutada: ")
            remove_task(task)
        elif user_input == '3':
            show_tasks()
        elif user_input == '4':
            print("Väljumine")
            break
        else:
            print("Sa sisestasid midagi vale")

main()
