import os
import json
import datetime
import traceback
from typing import List


class DataObject(object):
  
  def __init__(self, data: dict = {}):
    self.data = data

  def __str__(self):
    return f"<DataObject - name: {self.name}>"


class InMemoryDatabase(object):

  def __init__(self, name: str = "database.db"):
    self.data: List[DataObject] = []
    self.name: str = name


  def __str__(self):
    return f"<InMemoryDatabase: {self.name}>"


  def get_all(self) -> list:
    return list(map(lambda x: x.data, self.data))

  
  def get_length(self) -> int:
    return len(self.data)


  def add(self, data: DataObject) -> None:
    self.data.append(data)
    return None


  def find(self, index: int) -> DataObject:
    try:
      return self.data[index]

    except:
      raise IndexError(f"Database has no data with '{index}' index")

  
  def update(self, index: int, new_data: dict = {}) -> None:
    self.data[index].data = new_data
    return None


  def delete(self, index: int) -> None:
    self.data.pop(index)
    return None

  
  def __serialize(self) -> list:
    serialized_data: list = list(map(
      lambda x: json.dumps(x.data),
      self.data 
    ))

    return serialized_data

  
  def __is_database_exists(self, path) -> bool:
    return self.name in os.listdir(os.path.join(path))


  def save_as(self, path) -> None:
    def callback(err = None) -> None:
      if err == None:
        print("Database has been saved to local")
      else:
        print("Error occured")
    
    try:
      if self.__is_database_exists(path):
        os.remove(os.path.join(path, self.name))

      serialized_data = self.__serialize()
      with open(os.path.join(path, self.name), "a") as database:
        database.write("Saved at: " + str(datetime.datetime.now()))
        database.write("\n")
        
        for item in serialized_data:
          database.write(item)
          database.write("\n")

      callback()
  
    except Exception as e:
      callback(err = e)
      traceback.print_exc()