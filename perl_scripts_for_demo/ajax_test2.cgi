#!/usr/bin/perl

#Deliver a JavaScript array.

my $test_list = qq~Blue,Red,Green,Yellow,Cyan,Aubergine (Purple),Ochre~;

print "Content-type: text/html\nCache-control: no-cache\n\n$test_list";
exit;
