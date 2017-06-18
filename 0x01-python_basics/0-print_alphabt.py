#!/usr/bin/python3
''' Print ascii value range of alphabet in lowercase'''
for i in range(97, 123):
    if i != 101 or i != 113:
        print(chr(i), end='')
