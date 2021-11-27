import unittest
from database import InMemoryDatabase, DataObject


class TestInMemoryDatabase(unittest.TestCase):
  db = InMemoryDatabase()

  def test_get_all(self):
    get_all = self.db.get_all()
    self.assertIsInstance(get_all, list)


  def test_get_length(self):
    length = len(self.db.data)
    database_length = self.db.get_length()
    self.assertEqual(length, database_length)


  def test_add(self):
    length = len(self.db.data)
    data_obj = DataObject(data = {"test": "test-data"})
    self.db.add(data = data_obj)
    self.assertEqual(len(self.db.data), length + 1)


  def test_find(self):
    data_obj = self.db.find(index = 0)
    self.assertIsInstance(data_obj, DataObject)

  
  def test_update(self):
    test_data = {"test": "test-data"}
    obj = DataObject(data = test_data)

    self.db.add(obj)
    updated_test_data = {"test": "test-data-2"}
    self.db.update(index = -1, new_data = updated_test_data)

    updated_data_object = self.db.find(index = -1)

    self.assertNotEqual(test_data, updated_data_object.data)

  
  def test_delete(self):
    length = self.db.get_length()
    data_obj = DataObject(data = {"test": "test-data"})
    self.db.add(data = data_obj)
    
    obj = self.db.find(index = -1)
    self.db.delete(object = obj)
    after_delete_length = self.db.get_length()

    self.assertEqual(length, after_delete_length)


if __name__ == "__main__":
  unittest.main()