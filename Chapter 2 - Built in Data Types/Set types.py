# two set types
# set is mutable
# frozenset is immutable

# mutable
small_primes = set()                # empty set
small_primes.add(2)                 # adding one element at a time
small_primes.add(3)
small_primes.add(5)

print small_primes

small_primes.add(1)                 # look what i've done, 1 is not a prime!
print small_primes

small_primes.remove(1)              # so lets remove it
print small_primes

3 in small_primes                   # membership test

small_primes.add(3)                 # trying to add 3 again
print small_primes                  # no change duplication is not allowed


bigger_primes = set([5, 7, 11, 13])     # faster creation
print 'b = ', bigger_primes

print small_primes | bigger_primes      # union operator |

print small_primes & bigger_primes      # intersection operator &

print small_primes - bigger_primes      # difference operator -

small_primes = {2, 3, 5, 5, 3}
print '\n', small_primes


# immutable
small_primes = frozenset([2, 3, 5, 7])
bigger_primes = frozenset([5, 7, 11])

# small_primes.add(11)                    # we cannot add to a frozenset    AttributeError: 'frozenset' object has no attribute 'add'
# small_primes.remove(2)                  # neither can we remove           AttributeError: 'frozenset' object has no attribute 'remove'
print small_primes & bigger_primes        # intersect, union etc allowed
