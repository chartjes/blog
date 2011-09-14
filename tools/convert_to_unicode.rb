#!/usr/bin/env ruby
require 'fileutils'

markdown_files = Dir["*.yml"]

markdown_files.each do |m|
    puts "Converting #{m}"
    f = File.new(m)
    post_contents = f.read
    content = post_contents.encode("UTF-8")
    new_file = File.new(m + "-new", "w+")
    new_file.write(content)
    FileUtils.mv(m + "-new", m)
end

