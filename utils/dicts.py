def get_val(collection, key, default=None):
    """
    Функция возвращает значения из словаря по переданному ключу, если ключ существует.
    В ином случае возвращается default.
    :param collection: исходный словарь.
    :param key: ключ извлекаемого элемента.
    :param default: значение по умолчанию.
    :return: значение ключа.
    """
    if key not in collection:
        return default

    return collection[key]