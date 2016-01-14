#!/bin/bash -x

host='http://localhost:8080'
person='camilla'
enemy='graham'
nobody=''

case $1 in
  1) curl -v --data "person=$person" "$host/";;
  2) curl -v "$host/$person";;
  3) curl -v -X "DELETE" "$host/$person";;
  4) curl -v --data "person=$enemy" "$host/";;
  5) curl -v "$host/$enemy";;
  6) curl -v -X "DELETE" "$host/$enemy";;
  7) curl -v --data "person=$nobody" "$host/";;
  8) curl -v "$host/$nobody";;
  9) curl -v -X "DELETE" "$host/$nobody";;
  *) echo "enter test to run [1-9]";;
esac

