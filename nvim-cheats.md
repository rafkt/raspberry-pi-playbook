# Neovim / Lazyvim shortcuts and cheatsheet
# This cheatsheet ommits the most basic shortcuts

CTL-H / CTL-L : switch back/forth to NeoTree or open windows
H / L : switch back/forth to NeoTree or open tab within the window

## TERMINAL

<CTL>-/ : will open a floating terminal
<space> <f> <T> : will open a floating terminal

## WORD JUMPS

e / b : in NORMAL mode move at word end

## INSERT

A : jump at the end of the line and INSERT
I : INSERT at the start of the line
i : INSERT in front of the cursor
a : INSERT at the end of the cursor
O : INSERT in a new line above
o : INSERT in a new line below

## LINE JUMPS

$ : NORMAL jump at the end of the line
^ : NORMAL jump at the start of the line

## BLOCK VISUAL

CTL-v: visual block mode.
I : after visual block mode to insert at the start
A : to append at the end
X : to delete the block mode selection
d : to cut it

## LAZYVIM
<Leader> is space in my current Lazyvim configuratin

## SPECTRE Search & Replace

<space> s r : Find & Replace using Spectre. Note you would need glob paths with wildcards. In this mode you can always use <Leader> to preview your options

## TAB Management

<space> <tab> : To get to tab functionalities
<space> <tab> \[ : Previous tab (ommit backslash, only for escaping special char)
<space> <tab> \] : Next tab (ommit backslash, only for escaping special char)

## Window Management
<CTL>-w : window management 
w : Cycle clock wise the windows
W : Cycle anti-clock wise the windows

## SAVE with custom command e.g. to achieve sudo SAVE
:w !sudo tee %
:wa, will save all open buffers 

