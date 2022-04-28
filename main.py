class TextEditor:
  def __init__(self):
    self.text = ''
    self.cursor = 0
    self.copied = ''
    self.clipboard = [None, None]
    self.selected = False
    self.history = []
  
  def backup(self):
    self.history.append((self.text, self.cursor))
  
  def removeSelected(self):
    self.text = self.text[:self.clipboard[0]] + self.text[self.clipboard[1]:]
    # check whether to put cursor at the end of the text?
    self.cursor = self.clipboard[0]
    self.selected = False

  def append(self, text):
    self.backup()
    if self.selected:
      self.removeSelected()
    if not text:
      return self.text
    self.text = list(self.text)
    self.text = self.text[:self.cursor] + list(text) + self.text[self.cursor:]
    self.text = ''.join(self.text)
    self.cursor += len(text)
    return self.text
  
  def move(self, position):
    self.backup()
    if self.selected:
      self.selected = False
    if position < 0:
      position = 0
    elif position > len(self.text):
      position = len(self.text)
    self.cursor = position
    return self.text
  
  def backspace(self):
    self.backup()
    if self.selected:
      self.removeSelected()
      return self.text
    if len(self.text):
      self.text = self.text[:-1]
      self.cursor -= 1
    return self.text

  def select(self, left, right):
    self.backup()
    if left < 0:
      left = 0
    if right < 0:
      right = 0
    if left > len(self.text):
      left = len(self.text)
    if right > len(self.text):
      right = len(self.text)
    self.selected = True
    self.clipboard = [left, right]
    if left == right:
      self.cursor = left
    return self.text

  def copy(self):
    self.backup()
    self.copied = self.text[self.clipboard[0]:self.clipboard[1]]
    return self.text