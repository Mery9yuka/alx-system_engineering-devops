#!/usr/bin/env ruby
# regular expression that match one occurence of b and t 
# using the n? quantifier method

puts ARGV[0].scan(/hb?t?n/).join
