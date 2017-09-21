#!/usr/bin/perl

#Deliver a JSON object with nested objects

my $test_json = qq~{
    "response1":
        {
            "badge":"55555",
            "name": {"fname":"Vito","lname":"Corleone"},
            "platoon":"A01"
        },
    "response2":
        {
            "badge":"44444",
            "name": {"fname":"Michael","lname":"Corleone"},
            "platoon":"B02"
        },
    "response3":
        {
            "badge":"33333",
            "name": {"fname":"Sonny","lname":"Corleone"},
            "platoon":"C03"
        },
    "response4":
        {
            "badge":"22222",
            "name": {"fname":"Tom","lname":"Hagen"},
            "platoon":"D04"
        },
    "response5":
        {
            "badge":"11111",
            "name": {"fname":"Apollonia","lname":"Vitelli-Corleone"},
            "platoon":"E05"
        },
    "response6":
        {
            "badge":"66666",
            "name": {"fname":"Luca","lname":"Brasi"},
            "platoon":"F06"
        },
    "response7":
        {
            "badge":"777777",
            "name": {"fname":"Peter","lname":"Clemenze"},
            "platoon":"G07"
        }
}~;

print "Content-type: application/json\n\n$test_json";
exit;
