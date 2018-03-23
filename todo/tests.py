from django.test import TestCase
from models import TodoList

# Create your tests here.
class YourTestClass(TestCase):

    def test_empty_list(self):
        #arrange
        
        #act
        todoList = TodoList()
        #assert
        self.assertTrue(todoList.isEmpty())
        
    def test_add_task(self):
        #arrange
        todoList = TodoList()
        
        #act
        todoList.add_task('afeitar al gato')
        
        #assert
        self.assertFalse(todoList.isEmpty())
        self.assertEquals('afeitar al gato', todoList.first_task())
        