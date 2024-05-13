"""
@big_name:restful_must	
@file_name:cls_test	
@data:2024/5/10	
@developers:handsome_lxh
"""

class foo1:
    def __init__(self):
        print("sjddd")

    @classmethod
    def room(cls):
            print(cls())
class Foo(foo1):
        pass
Foo.room()