class Time( object ):
    def __init__(self, hour=0, minute=0, second=0):
        """ Construct a Clock using three integers. """
        self.__hour = hour
        self.__minute = minute
        self.__second = second
    
    def __repr__(self):
        """ Return a string as the formal representation a Clock."""
        return f"Class Time: {self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
    
    def __str__(self):
        """ Return a string (hh:mm:ss) to represent a Clock. """
        return f"{self.__hour:02d}:{self.__minute:02d}:{self.__second:02d}"
    
    def from_str(self, time_str):
        """ Convert a string (hh:mm:ss) into a Clock. """
        hour, minute, second = [int(n) for n in time_str.split(':')]
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def from_iso(self, time_str):
        """ Convert a string (hh-mm-ss) into a Clock. """
        hour, minute, second = [int(n) for n in time_str.split('-')]
        self.__hour = hour
        self.__minute = minute
        self.__second = second

def main():
    A = Time( 12, 25, 30 )

    print( A )
    print( repr( A ) )
    print( str( A ) )
    print()

    B = Time( 2, 25, 3 )

    print( B )
    print( repr( B ) )
    print( str( B ) )
    print()

    C = Time( 2, 25 )

    print( C )
    print( repr( C ) )
    print( str( C ) )
    print()

    D = Time()

    print( D )
    print( repr( D ) )
    print( str( D ) )
    print()

    D.from_str( "03:09:19" )

    print( D )
    print( repr( D ) )
    print( str( D ) )

if __name__ == "__main__":
    main()