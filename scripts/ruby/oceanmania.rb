#!/usr/bin/env ruby

# only a test for a function tha create all the possibilities of one combination of letters, it's used for oceanmania ;-))) 

a=['m','a','e','r','l','c']
a.each{|v|(a-[v]).each{|w|(a-[v,w]).each{|x|(a-[v,w,x]).each{|y|(a-[ v, w, x, y ]).each{|z|(a-[v,w,x,y,z]).each{|u| puts v+w+x+y+z+u}}}}}}