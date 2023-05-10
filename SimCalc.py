# -*- coding: utf-8 -*-
"""
Simple Calculator
Only include 4 main operators +, - ,* and /
It can receive keyboard input
        keyboard actions are as follows:
            numerical keys act as pressing a number button
            operational keys act as pressing an operation button
            ESC, c, and C act as pressing C button (clear)
            Enter, e, and E act as pressing = button
            x, X act as closing the window


Ver.5  
5/11/2023    
Mahdi Balali

"""


import customtkinter as ctk
import math

def number_of_digigits(number):
    if (float(number) == int(number)):
        number = int(number)
    number_string = str(number)
    floating_point_check = False
    digits_count = 0
    floatings_count = 0
    for c in number_string:
        if c == '.':
            floating_point_check = True
            continue
        if floating_point_check:
            floatings_count +=1
        else:
            digits_count += 1
    return [digits_count,floatings_count]
            
    

class Number_button(ctk.CTkButton):
    '''
    The Number_button class is inherited from CTkButton
    It has all of its features, but is especially designed to cover the
    requirements of a button in a calculator which must handle numerical values
    The main difference is its command vlaue. It will pass a proper function,
    regarding to the button number value, as the button response event
    '''

    def __init__(self, parent, number, function, width=10, height=10):
        super().__init__(parent, text=str(number), width=width,
                         height=height, command=lambda: function(number))


class Operator_button(ctk.CTkButton):
    '''
    The Operator_button class is inherited from CTkButton
    It has all of its features, but is especially designed to cover the
    requirements of a button in a calculator which must handle operational actions
    The main difference is its command vlaue. It will pass a proper function,
    regarding to the button operator , as the button response event
    '''

    def __init__(self, parent, opr, function, width=10, height=10):
        super().__init__(parent, text=opr, width=width,
                         height=height, command=lambda: function(opr))


class SimpleCalculator():
    def __init__(self):
        self.current_number = 0
        self.last_number = 0
        self.floating = False
        self.last_operator = '+'
        self.two_argument_operator_list = ['+', '-', '*', '/', '^']
        self.functional_operator_list = ['=', 'C']
        self.operator_list = self.two_argument_operator_list
        # sizes of buttons and screen are set here
        self.size_dict = {
            'button': (60, 60),
            'screen': (320, 60)
        }

        # The value could be light, dark System
        ctk.set_appearance_mode("light")
        # The value could be 'dark-blue, dark, green, etc.
        ctk.set_default_color_theme("dark-blue")

        self.main_form = ctk.CTk()       # a customtkinter form is created
        self.main_form.title("Simple Calculator")

        # The screen is created and arranged
        self.screen = ctk.CTkEntry(
            self.main_form, width=self.size_dict['screen'][0], height=self.size_dict['screen'][1], placeholder_text="0")
        self.screen.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        # The numeric buttons are created and arranged in a specific fram
        self.numeric_buttons_frame = ctk.CTkFrame(self.main_form)
        self.numeric_buttons_frame.grid(row=1, column=0, padx=10, pady=10)

        self.numeric_buttons = []  # The numeric button objects are stored in this array
        # The numeric button objects positions are stored in this array
        self.numberic_buttons_positions = []
        # The numeric button positions are set here
        for row in range(2, -1, -1):
            for col in range(3):
                self.numberic_buttons_positions.append((row, col))
        self.numberic_buttons_positions.insert(0, (3, 0))

        # The numerica button values are created
        for i in range(0, 10):
            posx = self.numberic_buttons_positions[i][0]
            posy = self.numberic_buttons_positions[i][1]
            self.numeric_buttons.append(Number_button(self.numeric_buttons_frame, i,
                                                      width=self.size_dict['button'][0],
                                                      height=self.size_dict['button'][1],
                                                      function=self.press_numberic_buttons))
            if (i == 0):
                self.numeric_buttons[-1].grid(row=posx,
                                              column=posy + 1, padx=1, pady=1)
            else:
                self.numeric_buttons[-1].grid(row=posx,
                                              column=posy, padx=1, pady=1)

        # The operator buttons are created and arranged in a specific fram

        self.operator_buttons_frame = ctk.CTkFrame(self.main_form)
        self.operator_buttons_frame.grid(row=1, column=1, padx=5, pady=1)

        # The operator button positions
        self.operators_buttons_positions = [(3, 0), (2, 0), (1, 0), (0, 0)]
        self.operators_buttons = []
        # The operator button objects are created in a list
        for i, pos in enumerate(self.operators_buttons_positions):
            posx = pos[0]
            posy = pos[1]
            self.operators_buttons.append(Operator_button(self.operator_buttons_frame,
                                                          self.operator_list[i], width=self.size_dict['button'][0],
                                                          height=self.size_dict['button'][1], function=self.press_operator_buttons))
            self.operators_buttons[-1].grid(row=posx,
                                            column=posy, padx=1, pady=1)

        # equal button is created and located
        self.equal_button = Operator_button(
            self.operator_buttons_frame, opr='=', width=self.size_dict['button'][0],
            height=self.size_dict['button'][1], function=self.press_operator_buttons)
        self.equal_button.grid(row=0, column=1, padx=1, pady=1)

        # clear button is created and located
        self.clear_button = Operator_button(
            self.operator_buttons_frame, opr='C', width=self.size_dict['button'][0],
            height=self.size_dict['button'][1], function=self.press_operator_buttons)
        self.clear_button.grid(row=1, column=1, padx=1, pady=1)

        # floating point
        self.floating_dot = Operator_button(
            self.numeric_buttons_frame, opr='.', width=self.size_dict['button'][0],
            height=self.size_dict['button'][1], function=self.press_operator_buttons)
        self.floating_dot.grid(row=3, column=2, padx=1, pady=1)

        # few reserved buttons are created and located for future usage
        self.reserved_button1 = ctk.CTkButton(
            self.numeric_buttons_frame, width=self.size_dict['button'][0], height=self.size_dict['button'][1], text='')
        self.reserved_button1.grid(row=3, column=0, padx=1, pady=1)

        self.reserved_button3 = ctk.CTkButton(
            self.operator_buttons_frame, width=self.size_dict['button'][0], height=self.size_dict['button'][1], text='')
        self.reserved_button3.grid(row=2, column=1, padx=1, pady=1)

        self.reserved_button4 = ctk.CTkButton(
            self.operator_buttons_frame, width=self.size_dict['button'][0], height=self.size_dict['button'][1], text='')
        self.reserved_button4.grid(row=3, column=1, padx=1, pady=1)
        self.main_form.bind('<KeyPress>',self.on_key_pressed)
        self.main_form.bind('<KeyRelease>',self.on_key_released)
        self.main_form.mainloop()
        

    def on_key_pressed(self,event):
        character = event.char
        if character.isnumeric():
            self.press_numberic_buttons(int(character))
        elif character in self.operator_list:
            self.press_operator_buttons(character)
        elif character in ['c','C','\x1b']:
            self.press_clear_button()
        elif character in ['.']:
            self.press_dot_button()
        elif character in ['\r','e','E']:
            self.press_equal_button()
        elif character in ['x','X']:
            self.main_form.destroy()
            

    def on_key_released(self,event):
        pass
    
    
    
    def press_numberic_buttons(self, number):
        '''
        Parameters
        ----------
        number : Numerical
            This is the digit, which the user pressed its related button.

        Returns
        -------
            This function returns None

        Operation
        ---------
            This function is called whenever the user press a numeric button
            It will update the value of the current number

        '''
        [digits_count ,floating_count] = number_of_digigits(self.current_number)
        if self.floating:
            self.current_number += number * (math.pow(10,-(floating_count+1)))
        else:
            self.current_number = 10 * self.current_number + number
        self.update_screen()

    def assign_opreator_function(self, operator):
        '''    

        Parameters
        ----------
        operator : string
            this argument's value specifies the operation selected by the user.
            It could be +, -, *, /, =,

        Returns
        -------
        function 
            this function returns a function based on the operation selected by the
            user.
        Operation
        ---------
            This function is called whenever the user press an operation button
            It will return the proper function for the selected operation

        '''
        if operator == '+':
            return lambda x, y: x+y
        if operator == '-':
            return lambda x, y: x-y
        if operator == '*':
            return lambda x, y: x*y
        if operator == '/':
            return lambda x, y: x/y

    def press_operator_buttons(self, operator):
        '''


        Parameters
        ----------
        operator : string
            this argument's value specifies the operation selected by the user.
            It could be +, -, *, /, =,.

        Returns
        -------
        int
            0: indicates that the selected operation has been =
            1: indicates that the selected operation has been Clear button
            2: indicates that the selected operation has been any of the +,-,*,/
        Operation
        ---------
            This function is called whenever the any of the operation buttons are
            pressed. It will handle the proper operation using assign_opreator_function
            and press_equal_button or press_clear_button functions
            The returned value is not used, and is for future usage

        '''
        if operator == '=':
            self.press_equal_button()
            return 0
        if operator == 'C':
            self.press_clear_button()
            return 0
        if operator == '.':
            if self.floating:
                return 0
            else:
                self.press_dot_button()
                return 0
        function = self.assign_opreator_function(self.last_operator)
        self.last_number = function(self.last_number, self.current_number)
        self.current_number = self.last_number
        self.update_screen()
        self.current_number = 0
        self.last_operator = operator
        self.floating = False
        return 0

    def press_equal_button(self):
        '''


        Returns
        -------
        None.
        Operation
        ---------
            This function is called whenever the user pressed equal button
            It will do the last operation and reset the current_number value
            and the last_operation value


        '''
        function = self.assign_opreator_function(self.last_operator)
        self.last_number = function(self.last_number, self.current_number)
        self.current_number = self.last_number
        self.update_screen()
        self.current_number = 0
        self.last_operator = '+'
        self.floating = False

    def press_clear_button(self):
        '''
        Returns
        -------
        None.

        Operation
        ---------
            This function is called whenever the user pressed Clear button (C)
            It will reset the current_number and last_number values
            and also the last_operation value

        '''
        self.last_number = 0
        self.current_number = 0
        self.update_screen()
        self.last_operator = '+'
        self.floating = False

    def press_dot_button(self):
        self.floating = True

    def update_screen(self):
        '''    
        Returns
        -------
        None.
        Operation
        ---------
            This function is called whenever any change in the screen text must be
            implemented.


        '''
        self.screen.delete(0, ctk.END)
        self.screen.insert(0, self.current_number)


calculator = SimpleCalculator()
