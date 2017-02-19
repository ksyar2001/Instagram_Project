import csv as csvClass
from StringIO import StringIO

class CSVWriter():
    def __init__( self ):
        self.output = StringIO()
        self.writer = csvClass.writer( self.output )

    def writeRow( self, listOfStrings ):
        self.writer.writerow( listOfStrings )

    def getString( self ):
        self.output.getvalue()

    def close( self ):
        self.output.close()
    