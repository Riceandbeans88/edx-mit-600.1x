# 6.00.1x Problem Set 7
# RSS Feed Filter
import string
import time
from Tkinter import *

from W07_Problem_Set_07.code_ProblemSet7 import feedparser
from project_util import translate_html


#-----------------------------------------------------------------------
#
# Problem Set 7

#======================
# Code for retrieving and parsing RSS feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        summary = translate_html(entry.summary)
        try:
            subject = translate_html(entry.tags[0]['term'])
        except AttributeError:
            subject = ""
        newsStory = NewsStory(guid, title, subject, summary, link)
        ret.append(newsStory)
    return ret
#======================

#======================
# Part 1
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory(object):
    '''
    A general class <--

    '''
    def __init__(self, guid, title, subject, summary, link):
        assert type(guid) and type(title) and type(subject) and type(summary) and type(link) == str
        self.guid = guid
        self.title = title
        self.subject = subject
        self.summary = summary
        self.link = link

    def getGuid(self):
        return self.guid

    def getTitle(self):
        return self.title

    def getSubject(self):
        return self.subject

    def getSummary(self):
        return self.summary

    def getLink(self):
        return self.link

#======================
# Part 2
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        raise NotImplementedError

# Whole Word Triggers
# Problems 2-5

# TODO: WordTrigger
class WordTrigger(Trigger):
    '''
    My class tba
    '''
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, hit_word):
        '''
        Return true when hit_word found
        '''
        hit_word = hit_word.lower()
        for punChar in string.punctuation:
            hit_word = hit_word.replace(punChar, ' ')
        hit_word_list = [e for e in hit_word.split(' ') if len(e) > 0]
        return self.word in hit_word_list


class TitleTrigger(WordTrigger):
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getTitle())


class SubjectTrigger(WordTrigger):
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getSubject())


class SummaryTrigger(WordTrigger):
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getSummary())


# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
class NotTrigger(Trigger):
    def __init__(self, trigger):
        self.trigger = trigger

    def evaluate(self, news_story_obj):
        return not self.trigger.evaluate(news_story_obj)

# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self, trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, news_story_obj):
        return self.trigger1.evaluate(news_story_obj) and self.trigger2.evaluate(news_story_obj)

# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,trigger1, trigger2):
        self.trigger1 = trigger1
        self.trigger2 = trigger2

    def evaluate(self, news_story_obj):
        return self.trigger1.evaluate(news_story_obj) or self.trigger2.evaluate(news_story_obj)





# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, news_story_obj):
        return self.phrase in news_story_obj.getSubject() or self.phrase in news_story_obj.getTitle() or self.phrase in news_story_obj.getSummary()

#======================
# Part 3
# Filtering
#======================

def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering)
    stories_list = []
    for i in stories:
        for j in triggerlist:
            if j.evaluate(i) == True:
                stories_list.append(i)
                break
    stories = stories_list
    return stories


#======================
# Part 4
# User-Specified Triggers
#======================

def makeTrigger(triggerMap, triggerType, params, name):
    """
    Takes in a map of names to trigger instance, the type of trigger to make,
    and the list of parameters to the constructor, and adds a new trigger
    to the trigger map dictionary.

    triggerMap: dictionary with names as keys (strings) and triggers as values
    triggerType: string indicating the type of trigger to make (ex: "TITLE")
    params: list of strings with the inputs to the trigger constructor (ex: ["world"])
    name: a string representing the name of the new trigger (ex: "t1")

    Modifies triggerMap, adding a new key-value pair for this trigger.

    Returns a new instance of a trigger (ex: TitleTrigger, AndTrigger).
    """
    # TODO: Problem 11
    # 4. Making triggers
def makeTrigger(triggerMap, triggerType, params, name):
    if triggerType == 'TITLE':
        myTrigger = TitleTrigger("".join(params))
    elif triggerType == 'SUBJECT':
        myTrigger = SubjectTrigger("".join(params))
    elif triggerType == 'SUMMARY':
        myTrigger = SummaryTrigger("".join(params))
    elif triggerType == 'PHRASE':
        myTrigger = PhraseTrigger(" ".join(params))
    elif triggerType == 'NOT':
        myTrigger = NotTrigger(triggerMap["".join(params)])
    elif triggerType == 'AND':
        myTrigger = AndTrigger(triggerMap["".join(params[0])], triggerMap["".join(params[1])])
    elif triggerType == 'OR':
        myTrigger = OrTrigger(triggerMap["".join(params[0])], triggerMap["".join(params[1])])

    triggerMap[name] = myTrigger

    return triggerMap[name]

    #else:
    #    raise ValueError

def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")

        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                  linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                triggers.append(triggerMap[name])

    return triggers
    
import thread

SLEEPTIME = 60 #seconds -- how often we poll


def main_thread(master):
    # A sample trigger list - you'll replace
    # this with something more configurable in Problem 11
    try:
        # These will probably generate a few hits...
        t1 = TitleTrigger("Obama")
        t2 = SubjectTrigger("Romney")
        t3 = PhraseTrigger("Election")
        t4 = OrTrigger(t2, t3)
        triggerlist = [t1, t4]
        
        # TODO: Problem 11
        # After implementing makeTrigger, uncomment the line below:
        # triggerlist = readTriggerConfig("triggers.txt")

        # **** from here down is about drawing ****
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)
        
        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)

        # Gather stories
        guidShown = []
        def get_cont(newstory):
            if newstory.getGuid() not in guidShown:
                cont.insert(END, newstory.getTitle()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.getSummary())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.getGuid())

        while True:

            print "Polling . . .",
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://rss.news.yahoo.com/rss/topstories"))

            # Process the stories
            stories = filterStories(stories, triggerlist)

            map(get_cont, stories)
            scrollbar.config(command=cont.yview)


            print "Sleeping..."
            time.sleep(SLEEPTIME)

    except Exception as e:
        print e


if __name__ == '__main__':

    root = Tk()
    root.title("Some RSS parser")
    thread.start_new_thread(main_thread, (root,))
    root.mainloop()

