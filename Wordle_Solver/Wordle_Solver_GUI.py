#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Dr. Will Pisani
@email: wapisani@mtu.edu

This script will help you solve the Wordle of the day. 
The English dictionary JSON was created from a larger
dictionary from https://github.com/dwyl/english-words/.
When loaded into the script, it's a dictionary where each
key is a five letter word (crate, for example) and the value
is the number of unique letters.

Program usage:
    Run this from the command line or terminal with python 3.8+.
    Can also be run from an IDE like Spyder

Requirements:
    Python 3.8+
    PySimpleGUI (If Anaconda Python: conda install -c conda-forge pysimplegui)
    Wordle_Solver_Function.py (in same directory as this script)
    words_dictionary_five_letters.json (in same directory as this script)
"""

from Wordle_Solver_Function import solveWordle
import PySimpleGUI as sg

sg.theme('Dark Blue 3')   # Add a touch of color
# All the stuff inside your window.
layout = [  [sg.Text('Enter your guesses below.', font='Courier 18')],
            [sg.InputText(font='Courier 18',size=(28,5),key='guess1')],
            [sg.InputText(font='Courier 18',size=(28,5),key='guess2')],
            [sg.InputText(font='Courier 18',size=(28,5),key='guess3')],
            [sg.InputText(font='Courier 18',size=(28,5),key='guess4')],
            [sg.InputText(font='Courier 18',size=(28,5),key='guess5')],
            [sg.Text('Enter yellow letters below, as one string.\nRemove yellow letters from this box \nonce they turn green.',font='Courier 18')],
            [sg.InputText(font='Courier 18',size=(28,5),key='yellow')],
            [sg.Text('Enter green letters below in position.',font='Courier 18')],
            [sg.Text('  1  ',font='Courier 18'),sg.Text('  2  ',font='Courier 18'),sg.Text('  3  ',font='Courier 18'),sg.Text('  4  ',font='Courier 18'),sg.Text('  5  ',font='Courier 18')],
            [sg.InputText(font='Courier 18',size=(5,5),key='green1'),sg.InputText(font='Courier 18',size=(5,5),key='green2'),sg.InputText(font='Courier 18',size=(5,5),key='green3'),sg.InputText(font='Courier 18',size=(5,5),key='green4'),sg.InputText(font='Courier 18',size=(5,5),key='green5')],
            [sg.Output(font='Courier 18',size=(30,8))],
            [sg.Button('Run',font='Courier 18'), sg.Button('Cancel',font='Courier 18'), sg.Button('Reset',font='Courier 18') ]]

# Create the Window
window = sg.Window("Will Pisani's Wordle Assistant", layout,finalize=True)
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    
    if event == 'Run':
        guesses = [values['guess1'],values['guess2'],values['guess3'],values['guess4'],values['guess5']]
        letters = [l for l in values['yellow']]
        correct_letters = {}
        correct_positions = [values['green1'],values['green2'],values['green3'],values['green4'],values['green5']]
        # Determine the positions of letters that were in the guesses
        # that are indeed in the word (these are the yellow letters)
        for guess in guesses:
            for index,l in enumerate(guess):
                if l in letters:
                    if l not in correct_letters:
                        correct_letters[l] = [index+1]
                    else:
                        correct_letters[l].append(index+1)
        solveWordle(guesses,correct_letters,correct_positions)
    
    if event == 'Reset':
        window['guess1'].update('')
        window['guess2'].update('')
        window['guess3'].update('')
        window['guess4'].update('')
        window['guess5'].update('')
        window['yellow'].update('')
        window['green1'].update('')
        window['green2'].update('')
        window['green3'].update('')
        window['green4'].update('')
        window['green5'].update('')
                
window.close()


