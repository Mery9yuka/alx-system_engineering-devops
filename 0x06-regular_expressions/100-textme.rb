#!/usr/bin/env ruby
# script to exctract infos from a specific pattern,
# using scan to find all occurence in the between (),
# (.*?) capture all characters except newline,
# using join to concatenate the the values together with a ","

print ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(",")
