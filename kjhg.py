#1
def custom_sort_list(my_list):
    if sum(my_list) / len(my_list) > 0:
        pivot = len(my_list) * 2 // 3
        first_part = sorted(my_list[:pivot])
        second_part = my_list[pivot:][::-1]
    else:
        pivot = len(my_list) // 3
        first_part = sorted(my_list[:pivot])
        second_part = my_list[pivot:][::-1]

    sorted_list = first_part + second_part
    return sorted_list

# Пример использования:
my_list = [2, -5, 1, 3, 0, -4, 8, 6, -7, 10]
sorted_result = custom_sort_list(my_list)
print(sorted_result)
#2
def display_grades(grades):
    print("Оценки студента:", grades)


def retake_exam(grades):
    index = int(input("Введите номер оценки для пересдачи (от 1 до 10): "))
    new_grade = int(input("Введите новую оценку (от 1 до 12): "))

    if 1 <= index <= 10 and 1 <= new_grade <= 12:
        grades[index - 1] = new_grade
        print("Оценка успешно изменена.")
    else:
        print("Неправильный ввод. Попробуйте снова.")


def check_scholarship(grades):
    average_grade = sum(grades) / len(grades)
    if average_grade >= 10.7:
        print("Вы имеете право на стипендию!")
    else:
        print("Увы, стипендия вам не положена.")


def sort_grades(grades, reverse=False):
    sorted_grades = sorted(grades, reverse=reverse)
    print("Отсортированные оценки:", sorted_grades)


grades = []
for i in range(10):
    grade = int(input(f"Введите оценку {i + 1} (от 1 до 12): "))
    grades.append(grade)

while True:
    print("\nМеню:")
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Проверка стипендии")
    print("4. Отсортировать оценки (по возрастанию)")
    print("5. Отсортировать оценки (по убыванию)")
    print("6. Выход")

    choice = int(input("Выберите действие: "))

    if choice == 1:
        display_grades(grades)
    elif choice == 2:
        retake_exam(grades)
    elif choice == 3:
        check_scholarship(grades)
    elif choice == 4:
        sort_grades(grades)
    elif choice == 5:
        sort_grades(grades, reverse=True)
    elif choice == 6:
        print("Программа завершена.")
        break
    else:
        print("Некорректный ввод. Попробуйте снова.")
        #3
def bubble_sort_optimized(arr):
    n = len(arr)
    swapped = True

    while swapped:
        swapped = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True

        if not swapped:
            break

    return arr

# Пример использования сортировки
lst = [64, 34, 25, 12, 22, 11, 90]
sorted_lst = bubble_sort_optimized(lst)
print("Отсортированный список:", sorted_lst)