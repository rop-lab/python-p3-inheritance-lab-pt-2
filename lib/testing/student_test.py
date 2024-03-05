#!/usr/bin/env python3

from student import Student, ChattyStudent

import io
import sys

class TestStudent:
    '''Class Student in student.py'''
    
    def test_says_hello(self):
        '''says a brief greeting.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.hello()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hey there! I'm so excited to learn stuff.\n")

    def test_raises_hand(self):
        '''respectfully tries to get the teacher's attention.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        student = Student()
        student.raise_hand()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Pick me!\n")

class TestChattyStudent:
    '''Class ChattyStudent in student.py'''
    
    def test_says_hello(self):
        '''says a brief greeting, then tries to spoil a TV show.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.hello()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Hey there! I'm so excited to learn stuff.\n" +
            "How are you doing today? I'm okay, but I'm kind of tired. Did you watch The Walking Dead last night? You didn't?! Oh man, it was so crazy! What, you don't want any spoilers? Okay well let me just tell you who died...\n")

    def test_raises_hand(self):
        '''respectfully tries to get the teacher's attention ten times.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        chatty_student = ChattyStudent()
        chatty_student.raise_hand()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "Pick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\nPick me!\n")