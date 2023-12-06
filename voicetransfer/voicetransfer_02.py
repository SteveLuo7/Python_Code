from win32com.client import Dispatch

speaker = Dispatch('SAPI.SpVoice')
speaker.Speak('Hello Everyone')
del speaker