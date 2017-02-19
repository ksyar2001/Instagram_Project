# communicates with Watson API

from watson_developer_cloud import PersonalityInsightsV3, ToneAnalyzerV3
import json

class WatsonAPI():
    def __init__( self ):
        self.PI = Personality()
        self.TA = Tone()
    
    def getPersonalityInsights( self, text ):
        return self.PI.profile( 
            text = text, # input to be analyzed
            raw_scores = True, # raw_scores in addition to percentile
        )

    def getToneAnalysis( self, text ):
        return self.TA.tone( 
            text = text # input to be analyzed
        )


# Sends text to Watson's Personality Insigts service
# then receive analysis.

class Personality():
    default_username = 'cd3e87ef-1985-46b1-8726-b41d4f935973'
    default_password = 'aHcW3DV4nWyk'

    def __init__( self, username = default_username, password = default_password ):
        self.personality_insights = PersonalityInsightsV3(
            username = username,
            password = password
        )

    def profile( self, text, raw_scores ):
        return self.personality_insights.profile( 
            text = text,
            raw_scores = raw_scores
        )

class Tone():
    default_username = "2638a3bc-0207-4aeb-aa8f-232c1db2ec74"
    default_password = "qOUkOykTwwlu"

    def __init__( self, username = default_username, password = default_password ):
        self.tone_analyzer = ToneAnalyzerV3(
            username = username,
            password = password,
            version = '2016-05-19'
        )

    def tone( self, text ):
        return self.tone_analyzer.tone( 
            text = text 
        )


test = WatsonAPI()
print( json.dumps( test.getToneAnalysis( "I love you" ), indent = 2 ) )