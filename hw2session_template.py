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
    # fill in your code!!!
    # and remove the following line
    return None

  # this removes a file "file_name" from the current working directory
  # it should report errors when:
  #   * file_name does not exist
  #   * file_name is a irectory
  def rm(self, file_name):
    # fill in your code!!!
    # and remove the following line
    return None

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
  #
  def dump_fsimage(self):
    # fill in your code!!!
    # and remove the following line
    return None