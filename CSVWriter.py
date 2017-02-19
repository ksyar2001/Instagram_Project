import csv
from StringIO import StringIO

class CSVWriter():
    def __init__( self ):
        self.output = StringIO()
        self.writer = csv.writer( self.output )

    def writeRow( self, listOfStrings ):
        self.writer.writerow( listOfStrings )

    def getString( self ):
        self.output.getvalue()

csv = CSVWriter()
list = ["hey", "dude", "yay"]
list.append( 'b' )
csv.writeRow( list )

print( csv.output.getvalue() )