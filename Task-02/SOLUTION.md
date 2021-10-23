pwd
   92  mkdir Coordinates_location
   93  cd Coodinates_location
   94  cd Coordinates_location
   95  mkdir North
   96  cd North
   97  cat > Ndegree.txt
   98  cat > Nminute.txt
   99  cat > Nsecond.txt
  100  cat Ndegree.txt Nminute.txt Nsecond.txt > Ncoordinate.txt
  101  cp /home/hemanth/Coordinates_location/North/Ncoordinate.txt /home/hemanth/Coordinates_location
  102  cd Coordinates_location
  103  cd ..
  104  rm -rf North
  105  mv Ncoordinate.txt North.txt
  106  mkdir East
  107  cd East
  108  cat > Edegree.txt
  109  cat > Eminute.txt
  110  cat > Esecond.txt
  111  cat Edegree.txt Eminute.txt Esecond.txt > Eastcoordinate.txt
  112  cp /home/hemanth/Coordinates_location/East/Eastcoordinate.txt /home/hemanth/Coordinates_location
  113  rm -rf East
  114  cd ..
  115  rm -rf East
  116  mv Eastcoordinate.txt East.txt
  117  cat North.txt East.txt > Location Coordinate.txt
  118  cat North.txt East.txt . Location-Coordinate.txt
  119  mv Location.txt Loaction_Coordinate.txt
  120  mv Location.txt Loction_Coordinate.txt
  121  mv Loction_coordinate.txt Location_Coordinate.txt
  122  cat SOLUTION.md
  123  touch SOLUTION.md
  124  history

