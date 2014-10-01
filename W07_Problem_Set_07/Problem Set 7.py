__author__ = 'AE'

# Enter your code for NewsStory in this box
class NewsStory(object):
    '''
    A general class

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

#PART II: WORD TRIGGERS

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, and SummaryTrigger in this box
# TODO: WordTrigger
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


#PART II: COMPOSITE TRIGGERS

# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
# TODO: WordTrigger
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, hit_word):
        hit_word = hit_word.lower()
        for punChar in string.punctuation:
            hit_word = hit_word.replace(punChar, ' ')
        hit_word_list = [e for e in hit_word.split(' ') if len(e) > 0]
        return self.word in hit_word_list


class TitleTrigger(WordTrigger):
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getTitle())

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

#PART II: PHRASE TRIGGERS

class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, hit_word):
        hit_word = hit_word.lower()
        for punChar in string.punctuation:
            hit_word = hit_word.replace(punChar, ' ')
        hit_word_list = [e for e in hit_word.split(' ') if len(e) > 0]
        return self.word in hit_word_list


class TitleTrigger(WordTrigger):
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getTitle())

class SummaryTrigger(WordTrigger):
    ''' blah
    '''
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getSummary())

class SubjectTrigger(WordTrigger):
    ''' blah
    '''
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getSubject())

class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def evaluate(self, news_story_obj):
        return self.phrase in news_story_obj.getSubject() or self.phrase in news_story_obj.getTitle()

#PART III: FILTERING

# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and
# filterStories in this box
class WordTrigger(Trigger):
    def __init__(self, word):
        self.word = word.lower()

    def isWordIn(self, hit_word):
        hit_word = hit_word.lower()
        for punChar in string.punctuation:
            hit_word = hit_word.replace(punChar, ' ')
        hit_word_list = [e for e in hit_word.split(' ') if len(e) > 0]
        return self.word in hit_word_list


class TitleTrigger(WordTrigger):
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getTitle())

class SummaryTrigger(WordTrigger):
    ''' blah
    '''
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getSummary())

class SubjectTrigger(WordTrigger):
    ''' blah
    '''
    def evaluate(self, news_story_obj):
        return self.isWordIn(news_story_obj.getSubject())

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

#PART IV: USER-SPECIFIED TRIGGERS
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