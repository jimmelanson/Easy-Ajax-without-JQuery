#!/usr/bin/perl

#Deliver a JSON list with one element which is an object

my $test_json = qq~[{"lname":"Solo","fname":"Han","badge":"55555"}]~;


print "Content-type: text/html\nCache-control: no-cache\n\n$test_json";
exit;
