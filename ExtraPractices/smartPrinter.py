from collections import deque

class SmartPrinter:
  def __init__(self):
    self.urgent = deque()
    self.normal = deque()


