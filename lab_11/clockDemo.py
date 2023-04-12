
import lab11b

A = lab11b.Time( 12, 25, 30 )

print( A )
print( repr( A ) )
print( str( A ) )
print()

B = lab11b.Time( 2, 25, 3 )

print( B )
print( repr( B ) )
print( str( B ) )
print()

C = lab11b.Time( 2, 25 )

print( C )
print( repr( C ) )
print( str( C ) )
print()

D = lab11b.Time()

print( D )
print( repr( D ) )
print( str( D ) )
print()

D.from_str( "03:09:19" )

print( D )
print( repr( D ) )
print( str( D ) )