
import speech_to_text
import merge
import eel
import wx
import sys
eel.init('web')
import pyttsx3
engine = pyttsx3.init()
import warnings

warnings.filterwarnings("ignore")


@eel.expose
def pythonFunction(wildcard="*"):

        app = wx.App(None)
        global path
        style = wx.FD_OPEN | wx.FD_FILE_MUST_EXIST
        dialog = wx.FileDialog(None, 'Open', wildcard=wildcard, style=style)
        if dialog.ShowModal() == wx.ID_OK:
            path = dialog.GetPath()
        else:
            path = None
        dialog.Destroy()
        engine.say("Please Press The Begin Button To proceed Further")
        engine.setProperty('rate', 250)
        engine.setProperty('volume', 0.9)
        engine.runAndWait()
        return True

@eel.expose
def getAgenda(agenda):

    global agenda1
    agenda1=agenda

@eel.expose
def getNum_usr(num_usr):
    global count
    count=int(num_usr)


@eel.expose
def operation():



        audio_file_name=path
        print(audio_file_name)
        transcript = speech_to_text.google_transcribe(audio_file_name,count)

        print(transcript)
        print("==================== Summery ==============")
        merge.merge_summary(transcript,agenda1)
        done()

@eel.expose
def voice():

    engine.say("Welcome To The Smart Meeting Assistant!! Please Read The Instructions Carefully")
    #engine.say("Please Read The Instructions Carefully")
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()
@eel.expose
def begin_voice():
    engine.say("Please Wait, We Are Processing Your Audio File")
    # engine.say("Please Read The Instructions Carefully")
    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()
@eel.expose
def thank_voice():
    engine.say("Thank You For the patience, Your Document Has been generated")

    engine.setProperty('rate', 120)
    engine.setProperty('volume', 0.9)
    engine.runAndWait()

@eel.expose
def done():
    return True


eel.start('index.html', size=(1500, 750))



