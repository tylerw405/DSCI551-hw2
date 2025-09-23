from filesystem import Session

class HW2Session(Session):
  def __init__(self, fs):
    super().__init__(fs)

  # you can add any helper function here, if needed

  # This removes the directory dir_name from the current working directory
  # It should report errors when
  #   * dir_name does not exist
  #   * dir_name is not empty
  #   * dir_name is not a directory
  def rmdir(self, dir_name):
    dir = None
    for d in self.curr_dir.children:
      if d.name == dir_name:
        dir = d
        break
    
    if dir is None:
      print(f'{dir_name} does not exist')
      return False
    
    if dir.children:
      print(f'{dir_name} is not empty')
      return False
    
    if dir.node_type != 'directory':
      print(f'{dir_name} is not a directory')
      return False
    
    self.curr_dir.children.remove(dir)
    dir.parent = None
    return True

  # this removes a file "file_name" from the current working directory
  # it should report errors when:
  #   * file_name does not exist
  #   * file_name is a irectory
  def rm(self, file_name):
    file = None
    for f in self.curr_dir.children:
      if f.name == file_name:
        file = f
        break
      
    if file is None:
      print(f'{file_name} does not exist')
      return False
    
    if file.node_type == 'directory':
      print(f'{file_name} is a directory')
      return False
    
    self.curr_dir.children.remove(file)
    file.parent = None
    return True

  # This emulates the hdfs oiv (offline image viewer) command to print the
  # entire namespace of file system. In other words, it lists all file system
  # objects (file or directory), one line at a time. For each object,
  # it shows the path to the object and the type of object, seperated by comma.
  # For example,
  #           /,directory
  #           /home,directory
  #           /home/john,directory
  #           /home/john/hw1.py,file
  #           ...
  def dump_fsimage(self):
    if self.root is None:
        return ''

    def abs_path(node):
        if node.parent is None:
            return '/'
        parts = []
        while node.parent is not None:
            parts.append(node.name)
            node = node.parent
        parts.reverse()
        return '/' + '/'.join(parts)

    paths = []
    def tree(node):
        paths.append(f'{abs_path(node)},{node.node_type}')
        for child in node.children:
            tree(child)

    tree(self.root)
    result = '\n'.join(paths)
    print(result)