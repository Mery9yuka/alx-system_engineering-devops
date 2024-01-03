#!/usr/bin/env ruby
# regular expression that look for the str hbt 
# and must be followed by the letter t at least 1 time ending with n

print ARGV[0].scan(/hbt{1,}n/).join
