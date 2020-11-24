struct Point  {
  int x;
  int y;
};

struct Line {
  Point start;
  Point end;
  double length;
};

/*

The length is defined by the start and end points: change one of the
points and the length changes. It’s better to make the length a calculated
field:
*/