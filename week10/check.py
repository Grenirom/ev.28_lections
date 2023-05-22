# class Dog:
#     def voice(self):
#         print('Гав')

# class Cat:
#     def voice(self):
#         print('Мяу')

# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik)
# to_pet(rex)

# todo = {}
# todo.pop()


# class CreateMixin:
#     def create(self, todo, key):
#         self.todos[key] = todo
#         print(self.todos)
    
# class DeleteMixin:
#     def delete(self, key):
#         self.todos.pop(key)
#         print(f'удалили {key} задачу')

# class UpdateMixin:
#     def update(self, key, new_value):
#         self.todos.update(key, new_value)
#         print





# class ToDo(CreateMixin):
#     todos = {}

#     # def set_deadline(self, date)
        

# obj = CreateMixin()
# print(obj.create('dz', 1))

        
#-----------------------
class CreateMixin: 
    def create(self, key, todo): 
        if key in self.todos.keys(): 
            return 'Задача под таким ключём уже существует' 
        self.todos[key] = todo 
        return self.todos 
    

class DeleteMixin: 
    def delete(self, key): 
        delete_ = self.todos.pop(key, 'нет такого ключа') 
        if 'нет такого ключа' == delete_: 
            return delete_ 
        return delete_ 
    

class UpdateMixin: 
    def update(self, key, new_value): 
        self.todos[key] = new_value 
        return self.todos 
    

class ReadMixin: 
    def read(self): 
        res = [x for x in self.todos.items()] 
        return sorted(res) 
    
    
class ToDo(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin): 
    todos = {} 
    def set_deadline(self, deadline): 
        import datetime # 
        time_ = datetime.datetime.now().strftime('%d/%m/%Y') 
        deadline = deadline.split('/') # 
        time_ = time_.split('/') 
        deadline = list(map(int, deadline)) # 
        time_ = list(map(int, time_)) # 
        time_ = sum((time_[0], time_[1]*30, time_[2]*365)) 
        deadline = datetime.date(deadline[2], deadline[1], deadline[0]) 
        time_ = datetime.date.today() 
        return (deadline - time_).days 
task = ToDo() 
print(task.set_deadline('31/12/2022')) 
print(task.create(1, 'todo')) 
print(task.delete(3)) 
print(task.update(1, 'todo')) 
print(task.read()) 
print(task.create(1, 'Do housework')) 
print(task.create(1, 'Do housework')) 
print(task.create(2, 'Go for a walk')) 
print(task.update(1, 'Do homework')) 
print(task.delete(2)) 
print(task.read()) 
print(task.set_deadline('31/12/2021'))