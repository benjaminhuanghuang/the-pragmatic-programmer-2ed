struct Point
{
  int x;
  int y;
  double distanceTo(Point &other);
};

struct Line
{
  Point start;
  Point end;
  double length() { return start.distanceTo(end); }
};


/*

*/