#!/bin/bash
# Takes in a URL, sends a POST request to that URL, and displays the body of the response
curl -sX POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
