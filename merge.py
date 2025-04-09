import re
from summa import summarizer
import speech_to_text
import doc
def merge_summary(transcript,agenda):
        speakers=set()
        speaker_count=3

        text = transcript

        for word in text.split():
            if(re.match(r'Speaker[0-9]:*$', word)):
                #print(word+"   yes")
                speakers.add(word)
        #print("speakers are")
        #for e in speakers:
            #print(e)



        result=re.findall(r'\b(\S+):([^:\[\]]+?)\n?(\[[^:]+?\]\n?)?(?=\b\S+:|$)', text)
        #print(result)
        summery=""
        count=0
        speaker_all_text=[]*speaker_count
        speaker_all_count=[]*speaker_count
        speaker_original=[]*speaker_count
        summary_all=[]*speaker_count
        #print(speaker_1[2])
        for e in speakers:
            sendText=''
            for i in range(0,len(result)):
                if(e == result[i][0]+':'):

                    sendText=sendText+result[i][1]

            speaker_all_count.append(e)
            speaker_all_text.append(sendText)
            speaker_original.append(e+sendText)
            #Sending text to summarizer


            summary_all.append(e+summarizer.summarize(sendText))
        final_summary_sperator = '\n'
        final_summary = final_summary_sperator.join(summary_all)
        print(final_summary)
        doc.docu(final_summary,agenda)





