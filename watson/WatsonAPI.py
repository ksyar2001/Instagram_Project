# communicates with Watson API

from watson_developer_cloud import PersonalityInsightsV3

# Sends text to Watson's Personality Insigts service
# then receive analysis.

class WatsonAPI():
    default_username = 'cd3e87ef-1985-46b1-8726-b41d4f935973'
    default_password = 'aHcW3DV4nWyk'
    personality_insights = None

    def __init__( self, username=default_username, password=default_password):
        self.personality_insights = PersonalityInsightsV3(
            username = username,
            password = password
        )
    
    def getPersonalityInsights( self, text ):
        return self.personality_insights.profile( 
            text = text, # input to be analyzed
            raw_scores = True, # raw_scores in addition to percentile
        )

test = WatsonAPI()
test.getPersonalityInsights( """

""" )


# this is to check git