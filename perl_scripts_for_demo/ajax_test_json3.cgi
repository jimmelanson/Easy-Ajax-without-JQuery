#!/usr/bin/perl

#Deliver a JSON object with nested objects

my $test_json = qq~{
    "response1":
        {
            "badge":"55555",
            "name": {"fname":"Jim","lname":"Melanson"},
            "platoon":"A01"
        },
    "response2":
        {
            "badge":"44444",
            "name": {"fname":"Betty","lname":"Boop"},
            "platoon":"B02"
        },
    "response3":
        {
            "badge":"33333",
            "name": {"fname":"Ish","lname":"Kabible"},
            "platoon":"C03"
        },
    "response4":
        {
            "badge":"22222",
            "name": {"fname":"Normy","lname":"Newguy"},
            "platoon":"D04"
        }
}~;

print "Content-type: application/json\n\n$test_json";
exit;
