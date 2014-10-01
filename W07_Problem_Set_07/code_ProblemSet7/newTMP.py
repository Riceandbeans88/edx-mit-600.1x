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
            if j.evaluate(i):
                stories_list.append(i)
    return stories_list