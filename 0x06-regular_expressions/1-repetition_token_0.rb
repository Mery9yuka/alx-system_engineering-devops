#!/usr/bin/env ruby
# regular expression that match "t" 2 and 5 times

puts ARGV[0].scan(/hbt{2,5}n/).join
