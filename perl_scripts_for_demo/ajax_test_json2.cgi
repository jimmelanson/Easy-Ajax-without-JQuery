#!/usr/bin/perl

#Deliver a JSON list of objects

my $test_json = qq~[
  {"lname": "Solo",
	"fname": "Han",
	"badge": "55555"
  },
  {"lname": "Boop",
	"fname": "Betty",
	"badge": "44444"
  },
  {"lname": "Kabible",
	"fname": "Ish",
	"badge": "33333"
  }
]~;

print "Content-type: application/json\n\n$test_json";
exit;
