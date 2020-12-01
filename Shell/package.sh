
# list of all the unique package names explicitly imported by your Java code
grep '^import ' *.java |
sed -e's/^import *//' -e's/;.*$//' |
sort -u >list



