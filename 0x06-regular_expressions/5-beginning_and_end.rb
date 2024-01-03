#!/usr/bin/env ruby
# using quantifier ^ we specify that we are looking for a str that beging with h
# using the quantifier $ we specify that the str must end with h
# using "." in between means that theres a single character

print ARGV[0].scan(/^h.n$/).join
