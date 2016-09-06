#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, __name, __score):
        self.__name = __name
        self.__score = __score

    def printScore(self):
        print('%s: %s' % (self.__name, self.__score))

    def printGrade(self):
        if(self.__score > 90):
            print("A")
        elif(self.__score < 60):
            print("C")
        elif():
            print("B")


bart = Student("bart", 91)
bart.printScore()
bart.printGrade()
print(type(bart))
print(type("type"))
print(isinstance(bart, Student))
# print(bart.__name) # printError , private val cannot call by out method
