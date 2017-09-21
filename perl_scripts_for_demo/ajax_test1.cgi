#!/usr/bin/perl

#Deliver a simple string.

%qs = ();
my @qs_pairs = split(/\&/, $ENV{'QUERY_STRING'});
foreach my $qs_pair (@qs_pairs) {
    my($qs_key, $qs_value) = split(/\=/, $qs_pair);
    $qs{$qs_key} = $qs_value;
}
undef @qs_pairs;

my $test_list;
if($qs{id} eq '55555') {
    $test_list = qq~55555 Solo, Han A01~;
}
elsif($qs{id} eq '44444') {
    $test_list = qq~44444 Boop, Betty B02~;
} else {
    $test_list = 'Error';
}

print "Content-type: text/html\nCache-control: no-cache\n\n$test_list";
exit;
