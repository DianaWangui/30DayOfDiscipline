from abc import ABC, abstractmethod

class University:
  """Instantiating the university attributes"""
  def __init__(self, uni_name):
    self._uni_name = uni_name

  @abstractmethod
  def get_uni_name(self):
    return self._uni_name
