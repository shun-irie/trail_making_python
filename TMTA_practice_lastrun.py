#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.1.4),
    on 6月 09, 2021, at 16:20
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard


"set the number (optional)"
"#1,#8は固定。他は無作為に変更する"
pos1=(-3.87, 0.69)
pos2=(5.95, -3.4)
pos3=(3.69, 7.48)
pos4=(0.28, 1.79)
pos5=(0.92, -4.11)
pos6=(-3.86,-6.13 )
pos7=(-8.47, 1.17)
pos8=(0, 4.61)

POS=[]
POS.append(pos2)
POS.append(pos3)
POS.append(pos4)
POS.append(pos5)
POS.append(pos6)
POS.append(pos7)
import random
order=[random.random() for i in range(0,6)]
order2=np.array(order).argsort()

Pos=[POS[order2[i]] for i in range(0,6)]



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.1.4'
expName = 'TMTA_practice'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath= 'C:\\Users\\User\\Documents\\TMTA_practice_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
polygon_1 = visual.Polygon(
    win=win, name='polygon_1',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=pos1,
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=0.0, interpolate=True)
polygon_2 = visual.Polygon(
    win=win, name='polygon_2',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[0],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-1.0, interpolate=True)
polygon_3 = visual.Polygon(
    win=win, name='polygon_3',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[1],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
polygon_4 = visual.Polygon(
    win=win, name='polygon_4',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[2],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
polygon_5 = visual.Polygon(
    win=win, name='polygon_5',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[3],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
polygon_6 = visual.Polygon(
    win=win, name='polygon_6',units='cm', 
    edges=90, size=(2,2),
    ori=0.0, pos=Pos[4],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
polygon_7 = visual.Polygon(
    win=win, name='polygon_7',units='cm', 
    edges=90, size=(2,2),
    ori=0.0, pos=Pos[5],
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-6.0, interpolate=True)
polygon_8 = visual.Polygon(
    win=win, name='polygon_8',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=pos8,
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-7.0, interpolate=True)
text_guide1 = visual.TextStim(win=win, name='text_guide1',
    text='はじめ',
    font='Open Sans',
    units='cm', pos=(-3.87, 2.69), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-8.0);
text_guide2 = visual.TextStim(win=win, name='text_guide2',
    text='おわり',
    font='Open Sans',
    units='cm', pos=(0, 6.61), height=1.0, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
text_1 = visual.TextStim(win=win, name='text_1',
    text='1',
    font='Open Sans',
    units='cm', pos=pos1, height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
text_2 = visual.TextStim(win=win, name='text_2',
    text='2',
    font='Open Sans',
    units='cm', pos=Pos[0], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);
text_3 = visual.TextStim(win=win, name='text_3',
    text='3',
    font='Open Sans',
    units='cm', pos=Pos[1], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-12.0);
text_4 = visual.TextStim(win=win, name='text_4',
    text='4',
    font='Open Sans',
    units='cm', pos=Pos[2], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-13.0);
text_5 = visual.TextStim(win=win, name='text_5',
    text='5',
    font='Open Sans',
    units='cm', pos=Pos[3], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-14.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text='6',
    font='Open Sans',
    units='cm', pos=Pos[4], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-15.0);
text_7 = visual.TextStim(win=win, name='text_7',
    text='7',
    font='Open Sans',
    units='cm', pos=Pos[5], height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-16.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='8',
    font='Open Sans',
    units='cm', pos=pos8, height=1.0, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-17.0);
# Set experiment start values for variable component button_func1
button_func1 = 0
button_func1Container = []
# Set experiment start values for variable component button_func2
button_func2 = 0
button_func2Container = []
# Set experiment start values for variable component button_func3
button_func3 = 0
button_func3Container = []
# Set experiment start values for variable component button_func4
button_func4 = 0
button_func4Container = []
# Set experiment start values for variable component button_func5
button_func5 = 0
button_func5Container = []
# Set experiment start values for variable component button_func6
button_func6 = 0
button_func6Container = []
# Set experiment start values for variable component button_func7
button_func7 = 0
button_func7Container = []
# Set experiment start values for variable component button_func8
button_func8 = 0
button_func8Container = []
button1 = visual.ButtonStim(win, 
   text=None, font='Open Sans',
   pos=pos1,units='cm',
   letterHeight=1.0,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color='black', colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button1')
button1.buttonClock = core.Clock()
button2 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=Pos[0],units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button2')
button2.buttonClock = core.Clock()
button3 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=Pos[1],units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button3')
button3.buttonClock = core.Clock()
button4 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=Pos[2],units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button4')
button4.buttonClock = core.Clock()
button5 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=Pos[3],units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button5')
button5.buttonClock = core.Clock()
button6 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=Pos[4],units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button6')
button6.buttonClock = core.Clock()
button7 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=Pos[5],units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button7')
button7.buttonClock = core.Clock()
button8 = visual.ButtonStim(win, 
   text=None, font='Arvo',
   pos=pos8,units='cm',
   letterHeight=0.05,
   size=(2,2), borderWidth=0.0,
   fillColor=None, borderColor=None,
   color=None, colorSpace='rgb',
   opacity=None,
   bold=True, italic=False,
   padding=None,
   anchor='center',
   name='button8')
button8.buttonClock = core.Clock()
polygon_1_red = visual.Polygon(
    win=win, name='polygon_1_red',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=pos1,
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-34.0, interpolate=True)
polygon_2_red = visual.Polygon(
    win=win, name='polygon_2_red',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[0],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-35.0, interpolate=True)
polygon_3_red = visual.Polygon(
    win=win, name='polygon_3_red',units='cm', 
    edges=90, size=(2,2),
    ori=0.0, pos=Pos[1],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-36.0, interpolate=True)
polygon_4_red = visual.Polygon(
    win=win, name='polygon_4_red',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[2],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-37.0, interpolate=True)
polygon_5_red = visual.Polygon(
    win=win, name='polygon_5_red',units='cm', 
    edges=90, size=(2,2),
    ori=0.0, pos=Pos[3],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-38.0, interpolate=True)
polygon_6_red = visual.Polygon(
    win=win, name='polygon_6_red',units='cm', 
    edges=90, size=(2,2),
    ori=0.0, pos=Pos[4],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-39.0, interpolate=True)
polygon_7_red = visual.Polygon(
    win=win, name='polygon_7_red',units='cm', 
    edges=90, size=(2, 2),
    ori=0.0, pos=Pos[5],
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-40.0, interpolate=True)
polygon_8_red = visual.Polygon(
    win=win, name='polygon_8_red',units='cm', 
    edges=90, size=(2,2),
    ori=0.0, pos=pos8,
    lineWidth=3.0,     colorSpace='rgb',  lineColor='red', fillColor=None,
    opacity=None, depth=-41.0, interpolate=True)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "trial"-------
continueRoutine = True
# update component parameters for each repeat
button_func2 = 0  # Set routine start values for button_func2
button_func3 = 0  # Set routine start values for button_func3
button_func4 = 0  # Set routine start values for button_func4
button_func5 = 0  # Set routine start values for button_func5
button_func6 = 0  # Set routine start values for button_func6
button_func7 = 0  # Set routine start values for button_func7
button_func8 = 0  # Set routine start values for button_func8
# keep track of which components have finished
trialComponents = [polygon_1, polygon_2, polygon_3, polygon_4, polygon_5, polygon_6, polygon_7, polygon_8, text_guide1, text_guide2, text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, button1, button2, button3, button4, button5, button6, button7, button8, polygon_1_red, polygon_2_red, polygon_3_red, polygon_4_red, polygon_5_red, polygon_6_red, polygon_7_red, polygon_8_red]
for thisComponent in trialComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "trial"-------
while continueRoutine:
    # get current time
    t = trialClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=trialClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon_1* updates
    if polygon_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_1.frameNStart = frameN  # exact frame index
        polygon_1.tStart = t  # local t and not account for scr refresh
        polygon_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_1, 'tStartRefresh')  # time at next scr refresh
        polygon_1.setAutoDraw(True)
    
    # *polygon_2* updates
    if polygon_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_2.frameNStart = frameN  # exact frame index
        polygon_2.tStart = t  # local t and not account for scr refresh
        polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
        polygon_2.setAutoDraw(True)
    
    # *polygon_3* updates
    if polygon_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_3.frameNStart = frameN  # exact frame index
        polygon_3.tStart = t  # local t and not account for scr refresh
        polygon_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3, 'tStartRefresh')  # time at next scr refresh
        polygon_3.setAutoDraw(True)
    
    # *polygon_4* updates
    if polygon_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_4.frameNStart = frameN  # exact frame index
        polygon_4.tStart = t  # local t and not account for scr refresh
        polygon_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_4, 'tStartRefresh')  # time at next scr refresh
        polygon_4.setAutoDraw(True)
    
    # *polygon_5* updates
    if polygon_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_5.frameNStart = frameN  # exact frame index
        polygon_5.tStart = t  # local t and not account for scr refresh
        polygon_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5, 'tStartRefresh')  # time at next scr refresh
        polygon_5.setAutoDraw(True)
    
    # *polygon_6* updates
    if polygon_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_6.frameNStart = frameN  # exact frame index
        polygon_6.tStart = t  # local t and not account for scr refresh
        polygon_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6, 'tStartRefresh')  # time at next scr refresh
        polygon_6.setAutoDraw(True)
    
    # *polygon_7* updates
    if polygon_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_7.frameNStart = frameN  # exact frame index
        polygon_7.tStart = t  # local t and not account for scr refresh
        polygon_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_7, 'tStartRefresh')  # time at next scr refresh
        polygon_7.setAutoDraw(True)
    
    # *polygon_8* updates
    if polygon_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        polygon_8.frameNStart = frameN  # exact frame index
        polygon_8.tStart = t  # local t and not account for scr refresh
        polygon_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_8, 'tStartRefresh')  # time at next scr refresh
        polygon_8.setAutoDraw(True)
    
    # *text_guide1* updates
    if text_guide1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_guide1.frameNStart = frameN  # exact frame index
        text_guide1.tStart = t  # local t and not account for scr refresh
        text_guide1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_guide1, 'tStartRefresh')  # time at next scr refresh
        text_guide1.setAutoDraw(True)
    
    # *text_guide2* updates
    if text_guide2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_guide2.frameNStart = frameN  # exact frame index
        text_guide2.tStart = t  # local t and not account for scr refresh
        text_guide2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_guide2, 'tStartRefresh')  # time at next scr refresh
        text_guide2.setAutoDraw(True)
    
    # *text_1* updates
    if text_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_1.frameNStart = frameN  # exact frame index
        text_1.tStart = t  # local t and not account for scr refresh
        text_1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_1, 'tStartRefresh')  # time at next scr refresh
        text_1.setAutoDraw(True)
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *text_4* updates
    if text_4.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        text_4.frameNStart = frameN  # exact frame index
        text_4.tStart = t  # local t and not account for scr refresh
        text_4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
        text_4.setAutoDraw(True)
    
    # *text_5* updates
    if text_5.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        text_5.frameNStart = frameN  # exact frame index
        text_5.tStart = t  # local t and not account for scr refresh
        text_5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
        text_5.setAutoDraw(True)
    
    # *text_6* updates
    if text_6.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        text_6.frameNStart = frameN  # exact frame index
        text_6.tStart = t  # local t and not account for scr refresh
        text_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
        text_6.setAutoDraw(True)
    
    # *text_7* updates
    if text_7.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        text_7.frameNStart = frameN  # exact frame index
        text_7.tStart = t  # local t and not account for scr refresh
        text_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
        text_7.setAutoDraw(True)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    
    # *button1* updates
    if button1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        button1.frameNStart = frameN  # exact frame index
        button1.tStart = t  # local t and not account for scr refresh
        button1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button1, 'tStartRefresh')  # time at next scr refresh
        button1.setAutoDraw(True)
    if button1.status == STARTED:
        # check whether button1 has been pressed
        if button1.isClicked:
            if not button1.wasClicked:
                button1.timesOn.append(globalClock.getTime()) # store time of first click
                button1.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button1.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button1.wasClicked:
                button_func1+=1
            button1.wasClicked = True  # if button1 is still clicked next frame, it is not a new click
        else:
            button1.wasClicked = False  # if button1 is clicked next frame, it is a new click
    else:
        button1.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button1.wasClicked = False  # if button1 is clicked next frame, it is a new click
    
    # *button2* updates
    if button2.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        button2.frameNStart = frameN  # exact frame index
        button2.tStart = t  # local t and not account for scr refresh
        button2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button2, 'tStartRefresh')  # time at next scr refresh
        button2.setAutoDraw(True)
    if button2.status == STARTED:
        # check whether button2 has been pressed
        if button2.isClicked:
            if not button2.wasClicked:
                button2.timesOn.append(globalClock.getTime()) # store time of first click
                button2.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button2.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button2.wasClicked:
                button_func2+=1
            button2.wasClicked = True  # if button2 is still clicked next frame, it is not a new click
        else:
            button2.wasClicked = False  # if button2 is clicked next frame, it is a new click
    else:
        button2.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button2.wasClicked = False  # if button2 is clicked next frame, it is a new click
    
    # *button3* updates
    if button3.status == NOT_STARTED and button_func2==1:
        # keep track of start time/frame for later
        button3.frameNStart = frameN  # exact frame index
        button3.tStart = t  # local t and not account for scr refresh
        button3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button3, 'tStartRefresh')  # time at next scr refresh
        button3.setAutoDraw(True)
    if button3.status == STARTED:
        # check whether button3 has been pressed
        if button3.isClicked:
            if not button3.wasClicked:
                button3.timesOn.append(globalClock.getTime()) # store time of first click
                button3.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button3.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button3.wasClicked:
                button_func3+=1
            button3.wasClicked = True  # if button3 is still clicked next frame, it is not a new click
        else:
            button3.wasClicked = False  # if button3 is clicked next frame, it is a new click
    else:
        button3.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button3.wasClicked = False  # if button3 is clicked next frame, it is a new click
    
    # *button4* updates
    if button4.status == NOT_STARTED and button_func3==1:
        # keep track of start time/frame for later
        button4.frameNStart = frameN  # exact frame index
        button4.tStart = t  # local t and not account for scr refresh
        button4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button4, 'tStartRefresh')  # time at next scr refresh
        button4.setAutoDraw(True)
    if button4.status == STARTED:
        # check whether button4 has been pressed
        if button4.isClicked:
            if not button4.wasClicked:
                button4.timesOn.append(globalClock.getTime()) # store time of first click
                button4.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button4.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button4.wasClicked:
                button_func4+=1
            button4.wasClicked = True  # if button4 is still clicked next frame, it is not a new click
        else:
            button4.wasClicked = False  # if button4 is clicked next frame, it is a new click
    else:
        button4.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button4.wasClicked = False  # if button4 is clicked next frame, it is a new click
    
    # *button5* updates
    if button5.status == NOT_STARTED and button_func4==1:
        # keep track of start time/frame for later
        button5.frameNStart = frameN  # exact frame index
        button5.tStart = t  # local t and not account for scr refresh
        button5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button5, 'tStartRefresh')  # time at next scr refresh
        button5.setAutoDraw(True)
    if button5.status == STARTED:
        # check whether button5 has been pressed
        if button5.isClicked:
            if not button5.wasClicked:
                button5.timesOn.append(globalClock.getTime()) # store time of first click
                button5.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button5.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button5.wasClicked:
                button_func5+=1
            button5.wasClicked = True  # if button5 is still clicked next frame, it is not a new click
        else:
            button5.wasClicked = False  # if button5 is clicked next frame, it is a new click
    else:
        button5.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button5.wasClicked = False  # if button5 is clicked next frame, it is a new click
    
    # *button6* updates
    if button6.status == NOT_STARTED and button_func5==1:
        # keep track of start time/frame for later
        button6.frameNStart = frameN  # exact frame index
        button6.tStart = t  # local t and not account for scr refresh
        button6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button6, 'tStartRefresh')  # time at next scr refresh
        button6.setAutoDraw(True)
    if button6.status == STARTED:
        # check whether button6 has been pressed
        if button6.isClicked:
            if not button6.wasClicked:
                button6.timesOn.append(globalClock.getTime()) # store time of first click
                button6.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button6.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button6.wasClicked:
                button_func6+=1
            button6.wasClicked = True  # if button6 is still clicked next frame, it is not a new click
        else:
            button6.wasClicked = False  # if button6 is clicked next frame, it is a new click
    else:
        button6.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button6.wasClicked = False  # if button6 is clicked next frame, it is a new click
    
    # *button7* updates
    if button7.status == NOT_STARTED and button_func6==1:
        # keep track of start time/frame for later
        button7.frameNStart = frameN  # exact frame index
        button7.tStart = t  # local t and not account for scr refresh
        button7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button7, 'tStartRefresh')  # time at next scr refresh
        button7.setAutoDraw(True)
    if button7.status == STARTED:
        # check whether button7 has been pressed
        if button7.isClicked:
            if not button7.wasClicked:
                button7.timesOn.append(globalClock.getTime()) # store time of first click
                button7.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button7.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button7.wasClicked:
                button_func7+=1
            button7.wasClicked = True  # if button7 is still clicked next frame, it is not a new click
        else:
            button7.wasClicked = False  # if button7 is clicked next frame, it is a new click
    else:
        button7.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button7.wasClicked = False  # if button7 is clicked next frame, it is a new click
    
    # *button8* updates
    if button8.status == NOT_STARTED and button_func7==1:
        # keep track of start time/frame for later
        button8.frameNStart = frameN  # exact frame index
        button8.tStart = t  # local t and not account for scr refresh
        button8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(button8, 'tStartRefresh')  # time at next scr refresh
        button8.setAutoDraw(True)
    if button8.status == STARTED:
        # check whether button8 has been pressed
        if button8.isClicked:
            if not button8.wasClicked:
                button8.timesOn.append(globalClock.getTime()) # store time of first click
                button8.timesOff.append(globalClock.getTime()) # store time clicked until
            else:
                button8.timesOff[-1] = globalClock.getTime() # update time clicked until
            if not button8.wasClicked:
                button_func8+=1
            button8.wasClicked = True  # if button8 is still clicked next frame, it is not a new click
        else:
            button8.wasClicked = False  # if button8 is clicked next frame, it is a new click
    else:
        button8.buttonClock.reset() # keep clock at 0 if button hasn't started / has finished
        button8.wasClicked = False  # if button8 is clicked next frame, it is a new click
    
    # *polygon_1_red* updates
    if polygon_1_red.status == NOT_STARTED and button_func1==1:
        # keep track of start time/frame for later
        polygon_1_red.frameNStart = frameN  # exact frame index
        polygon_1_red.tStart = t  # local t and not account for scr refresh
        polygon_1_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_1_red, 'tStartRefresh')  # time at next scr refresh
        polygon_1_red.setAutoDraw(True)
    
    # *polygon_2_red* updates
    if polygon_2_red.status == NOT_STARTED and button_func2==1:
        # keep track of start time/frame for later
        polygon_2_red.frameNStart = frameN  # exact frame index
        polygon_2_red.tStart = t  # local t and not account for scr refresh
        polygon_2_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_2_red, 'tStartRefresh')  # time at next scr refresh
        polygon_2_red.setAutoDraw(True)
    
    # *polygon_3_red* updates
    if polygon_3_red.status == NOT_STARTED and button_func3==1:
        # keep track of start time/frame for later
        polygon_3_red.frameNStart = frameN  # exact frame index
        polygon_3_red.tStart = t  # local t and not account for scr refresh
        polygon_3_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_3_red, 'tStartRefresh')  # time at next scr refresh
        polygon_3_red.setAutoDraw(True)
    
    # *polygon_4_red* updates
    if polygon_4_red.status == NOT_STARTED and button_func4==1:
        # keep track of start time/frame for later
        polygon_4_red.frameNStart = frameN  # exact frame index
        polygon_4_red.tStart = t  # local t and not account for scr refresh
        polygon_4_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_4_red, 'tStartRefresh')  # time at next scr refresh
        polygon_4_red.setAutoDraw(True)
    
    # *polygon_5_red* updates
    if polygon_5_red.status == NOT_STARTED and button_func5==1:
        # keep track of start time/frame for later
        polygon_5_red.frameNStart = frameN  # exact frame index
        polygon_5_red.tStart = t  # local t and not account for scr refresh
        polygon_5_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_5_red, 'tStartRefresh')  # time at next scr refresh
        polygon_5_red.setAutoDraw(True)
    
    # *polygon_6_red* updates
    if polygon_6_red.status == NOT_STARTED and button_func6==1:
        # keep track of start time/frame for later
        polygon_6_red.frameNStart = frameN  # exact frame index
        polygon_6_red.tStart = t  # local t and not account for scr refresh
        polygon_6_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_6_red, 'tStartRefresh')  # time at next scr refresh
        polygon_6_red.setAutoDraw(True)
    
    # *polygon_7_red* updates
    if polygon_7_red.status == NOT_STARTED and button_func7==1:
        # keep track of start time/frame for later
        polygon_7_red.frameNStart = frameN  # exact frame index
        polygon_7_red.tStart = t  # local t and not account for scr refresh
        polygon_7_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_7_red, 'tStartRefresh')  # time at next scr refresh
        polygon_7_red.setAutoDraw(True)
    
    # *polygon_8_red* updates
    if polygon_8_red.status == NOT_STARTED and button_func8==1:
        # keep track of start time/frame for later
        polygon_8_red.frameNStart = frameN  # exact frame index
        polygon_8_red.tStart = t  # local t and not account for scr refresh
        polygon_8_red.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(polygon_8_red, 'tStartRefresh')  # time at next scr refresh
        polygon_8_red.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "trial"-------
for thisComponent in trialComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon_1.started', polygon_1.tStartRefresh)
thisExp.addData('polygon_1.stopped', polygon_1.tStopRefresh)
thisExp.addData('polygon_2.started', polygon_2.tStartRefresh)
thisExp.addData('polygon_2.stopped', polygon_2.tStopRefresh)
thisExp.addData('polygon_3.started', polygon_3.tStartRefresh)
thisExp.addData('polygon_3.stopped', polygon_3.tStopRefresh)
thisExp.addData('polygon_4.started', polygon_4.tStartRefresh)
thisExp.addData('polygon_4.stopped', polygon_4.tStopRefresh)
thisExp.addData('polygon_5.started', polygon_5.tStartRefresh)
thisExp.addData('polygon_5.stopped', polygon_5.tStopRefresh)
thisExp.addData('polygon_6.started', polygon_6.tStartRefresh)
thisExp.addData('polygon_6.stopped', polygon_6.tStopRefresh)
thisExp.addData('polygon_7.started', polygon_7.tStartRefresh)
thisExp.addData('polygon_7.stopped', polygon_7.tStopRefresh)
thisExp.addData('polygon_8.started', polygon_8.tStartRefresh)
thisExp.addData('polygon_8.stopped', polygon_8.tStopRefresh)
thisExp.addData('text_guide1.started', text_guide1.tStartRefresh)
thisExp.addData('text_guide1.stopped', text_guide1.tStopRefresh)
thisExp.addData('text_guide2.started', text_guide2.tStartRefresh)
thisExp.addData('text_guide2.stopped', text_guide2.tStopRefresh)
thisExp.addData('text_1.started', text_1.tStartRefresh)
thisExp.addData('text_1.stopped', text_1.tStopRefresh)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
thisExp.addData('text_3.started', text_3.tStartRefresh)
thisExp.addData('text_3.stopped', text_3.tStopRefresh)
thisExp.addData('text_4.started', text_4.tStartRefresh)
thisExp.addData('text_4.stopped', text_4.tStopRefresh)
thisExp.addData('text_5.started', text_5.tStartRefresh)
thisExp.addData('text_5.stopped', text_5.tStopRefresh)
thisExp.addData('text_6.started', text_6.tStartRefresh)
thisExp.addData('text_6.stopped', text_6.tStopRefresh)
thisExp.addData('text_7.started', text_7.tStartRefresh)
thisExp.addData('text_7.stopped', text_7.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
thisExp.addData('button_func2.routineEndVal', button_func2)  # Save end routine value
thisExp.addData('button_func3.routineEndVal', button_func3)  # Save end routine value
thisExp.addData('button_func4.routineEndVal', button_func4)  # Save end routine value
thisExp.addData('button_func5.routineEndVal', button_func5)  # Save end routine value
thisExp.addData('button_func6.routineEndVal', button_func6)  # Save end routine value
thisExp.addData('button_func7.routineEndVal', button_func7)  # Save end routine value
thisExp.addData('button_func8.routineEndVal', button_func8)  # Save end routine value
thisExp.addData('button1.started', button1.tStartRefresh)
thisExp.addData('button1.stopped', button1.tStopRefresh)
thisExp.addData('button1.numClicks', button1.numClicks)
if button1.numClicks:
   thisExp.addData('button1.timesOn', button1.timesOn)
   thisExp.addData('button1.timesOff', button1.timesOff)
else:
   thisExp.addData('button1.timesOn', "")
   thisExp.addData('button1.timesOff', "")
thisExp.addData('button2.started', button2.tStartRefresh)
thisExp.addData('button2.stopped', button2.tStopRefresh)
thisExp.addData('button2.numClicks', button2.numClicks)
if button2.numClicks:
   thisExp.addData('button2.timesOn', button2.timesOn)
   thisExp.addData('button2.timesOff', button2.timesOff)
else:
   thisExp.addData('button2.timesOn', "")
   thisExp.addData('button2.timesOff', "")
thisExp.addData('button3.started', button3.tStartRefresh)
thisExp.addData('button3.stopped', button3.tStopRefresh)
thisExp.addData('button3.numClicks', button3.numClicks)
if button3.numClicks:
   thisExp.addData('button3.timesOn', button3.timesOn)
   thisExp.addData('button3.timesOff', button3.timesOff)
else:
   thisExp.addData('button3.timesOn', "")
   thisExp.addData('button3.timesOff', "")
thisExp.addData('button4.started', button4.tStartRefresh)
thisExp.addData('button4.stopped', button4.tStopRefresh)
thisExp.addData('button4.numClicks', button4.numClicks)
if button4.numClicks:
   thisExp.addData('button4.timesOn', button4.timesOn)
   thisExp.addData('button4.timesOff', button4.timesOff)
else:
   thisExp.addData('button4.timesOn', "")
   thisExp.addData('button4.timesOff', "")
thisExp.addData('button5.started', button5.tStartRefresh)
thisExp.addData('button5.stopped', button5.tStopRefresh)
thisExp.addData('button5.numClicks', button5.numClicks)
if button5.numClicks:
   thisExp.addData('button5.timesOn', button5.timesOn)
   thisExp.addData('button5.timesOff', button5.timesOff)
else:
   thisExp.addData('button5.timesOn', "")
   thisExp.addData('button5.timesOff', "")
thisExp.addData('button6.started', button6.tStartRefresh)
thisExp.addData('button6.stopped', button6.tStopRefresh)
thisExp.addData('button6.numClicks', button6.numClicks)
if button6.numClicks:
   thisExp.addData('button6.timesOn', button6.timesOn)
   thisExp.addData('button6.timesOff', button6.timesOff)
else:
   thisExp.addData('button6.timesOn', "")
   thisExp.addData('button6.timesOff', "")
thisExp.addData('button7.started', button7.tStartRefresh)
thisExp.addData('button7.stopped', button7.tStopRefresh)
thisExp.addData('button7.numClicks', button7.numClicks)
if button7.numClicks:
   thisExp.addData('button7.timesOn', button7.timesOn)
   thisExp.addData('button7.timesOff', button7.timesOff)
else:
   thisExp.addData('button7.timesOn', "")
   thisExp.addData('button7.timesOff', "")
thisExp.addData('button8.started', button8.tStartRefresh)
thisExp.addData('button8.stopped', button8.tStopRefresh)
thisExp.addData('button8.numClicks', button8.numClicks)
if button8.numClicks:
   thisExp.addData('button8.timesOn', button8.timesOn)
   thisExp.addData('button8.timesOff', button8.timesOff)
else:
   thisExp.addData('button8.timesOn', "")
   thisExp.addData('button8.timesOff', "")
thisExp.addData('polygon_1_red.started', polygon_1_red.tStartRefresh)
thisExp.addData('polygon_1_red.stopped', polygon_1_red.tStopRefresh)
thisExp.addData('polygon_2_red.started', polygon_2_red.tStartRefresh)
thisExp.addData('polygon_2_red.stopped', polygon_2_red.tStopRefresh)
thisExp.addData('polygon_3_red.started', polygon_3_red.tStartRefresh)
thisExp.addData('polygon_3_red.stopped', polygon_3_red.tStopRefresh)
thisExp.addData('polygon_4_red.started', polygon_4_red.tStartRefresh)
thisExp.addData('polygon_4_red.stopped', polygon_4_red.tStopRefresh)
thisExp.addData('polygon_5_red.started', polygon_5_red.tStartRefresh)
thisExp.addData('polygon_5_red.stopped', polygon_5_red.tStopRefresh)
thisExp.addData('polygon_6_red.started', polygon_6_red.tStartRefresh)
thisExp.addData('polygon_6_red.stopped', polygon_6_red.tStopRefresh)
thisExp.addData('polygon_7_red.started', polygon_7_red.tStartRefresh)
thisExp.addData('polygon_7_red.stopped', polygon_7_red.tStopRefresh)
thisExp.addData('polygon_8_red.started', polygon_8_red.tStartRefresh)
thisExp.addData('polygon_8_red.stopped', polygon_8_red.tStopRefresh)
# the Routine "trial" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
