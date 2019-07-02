import pickle


# Method to pickle any instance
def save_instance(instance=None, path_where_to_save=None) -> pickle:
    """
    instance : object, any python object
    path_where_to_save : string, path along with file name where to save instance
    return : None
    """
    with open(path_where_to_save, "wb") as file:
        pickle.dump(instance, file, protocol=pickle.HIGHEST_PROTOCOL)


# Method to load any pickled instance
def load_instance(path_where_to_look=None) -> pickle:
    """
    path_where_to_look : string, path along with file name where to save instance
    return : pickled loaded instance
    """
    with open(path_where_to_look, "rb") as file:
        instance = pickle.load(file)
    return instance


def write_file(file_content=None, path_where_to_write=None) -> None:
    """
    :param file_content: string, name of file
    :param path_where_to_write: string, path where to write
    :return: None
    """
    with open(path_where_to_write, "w") as file:
        file.write(file_content)


def read_file(path_where_to_look=None):
    """
    :param path_where_to_look: string, path where to write
    :return: file contents
    """
    with open(path_where_to_look, "r") as file:
        content = file.read()
    return content




