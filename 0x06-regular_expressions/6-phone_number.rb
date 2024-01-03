#!/usr/bin/env ruby
# using the \d to find a digit and {} to speciafy 
# the number of digit we have to find

puts ARGV[0].scan(/^\d{10}$/).join