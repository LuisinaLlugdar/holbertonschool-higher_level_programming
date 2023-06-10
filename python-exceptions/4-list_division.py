#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = 0
            result = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except (ZeroDivisionError, ValueError):
            print("division by 0")
        finally:
            new_list.append(result)
    return new_list
