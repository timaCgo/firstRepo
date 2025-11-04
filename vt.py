class Students:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade=None):
        if grade is None:
            return "Не указаны оценки"

        grade = [g for g in grade if 0 <= g <= 5]
        if not grade:
            return "Ни одна оценка не была добавлена — неверный диапазон"

        if not isinstance(grade, list):
            grade = [grade]

        self.grades.extend(grade)

        if len(grade) == 1:
            msg = f"Оценка {grade[0]} успешно добавлена"
        else:
            msg = f"Оценки {', '.join(map(str, grade))} успешно добавлены"

        return f"{msg}\nСредний балл: {self.avg()}"

    def avg(self):
        if len(self.grades) == 0:
            return "Еще нету"
        return sum(self.grades) / len(self.grades) 
    
    def show_all_grades(self):
        if len(self.grades) == 0:
            return f"Оценок у {self.name} еще нету"
        return f"Оценки {self.name}: {self.grades}"
    
    def remove_grade(self, grade):
        try:
            self.grades.remove(grade)
            return f"Успешно удаленно\nСредний балл: {self.avg()}"
        except:
            return "Где-то ошибка!"
        
    def clear_grades(self):
        self.grades.clear()
        return "Оценки успешно удаленны"
    
    def __str__(self):
        return f"Имя: {self.name}, Средняя оценка: {self.avg()}"
    


s = Students("Alice")
print(s.add_grade(5))
print(s.add_grade(4))
print(s.add_grade([5, 4]))

