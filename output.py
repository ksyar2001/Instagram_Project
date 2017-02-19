from webpage.models import *
from CSVWriter import CSVWriter

def generatePhotoCSV( username ):
    string = "date,comments,likes\\n"
    for photo in InstagramAccount.objects.get(username=username).photo.all():
        csv = CSVWriter()        
        list = []
        #list.apend( photo.pk )
        list.append( photo.time )
        list.append( photo.comments.all().count() )
        list.append( photo.likes )
        #list.append( photo.tag.all().count() )
        

        csv.writer.writerow( list )
        string += csv.output.getvalue() + "\\n"
    csv.close()        
    return string

def generateAccountCSV( username ):
    num_likes = 0

    string = ""
    for photo in InstagramAccount.objects.get(username=username).photo.all():
        csv = CSVWriter()        
        list = []
        #list.apend( photo.pk )
        list.append( photo.comments.all().count() )
        list.append( photo.likes )
        #list.append( photo.tag.all().count() )
        list.append( photo.time )

        csv.writer.writerow( list )
        string += csv.output.getvalue()
    csv.close()        
    return string