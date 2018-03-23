from django.test import TestCase
from models import TodoList

# Create your tests here.
class YourTestClass(TestCase):

    def test_empty_list(self):
        #given
        
        #when
        todoList = TodoList()
        #then
        self.assertTrue(todoList.is_empty())
        
    def test_add_task(self):
        #given
        todoList = TodoList()
        
        #when
        todoList.add_task('afeitar al gato')
        
        #then
        self.assertFalse(todoList.is_empty())
        self.assertEquals('afeitar al gato', todoList.first_task())
        
        
    def test_list_tasks(self):
        #given
        todoList = TodoList()
        todoList.add_task('afeitar al gato')
        
        #when
        
    
        #then
        self.assertTrue(False)
    
    def test_add_many_tasks(self):
        #given
        todoList = TodoList()
        todoList.add_task('afeitar al gato')
    
        #when
        todoList.add_task('Afeitar al perro')
        todoList.add_task('Peinar la mugneca')
    
        #then
        self.assertEqual(3, todoList.length())
        self.assertTrue(todoList.contains('afeitar al gato'))
        self.assertTrue(todoList.contains('Afeitar al perro'))
        self.assertTrue(todoList.contains('Peinar la mugneca'))
        