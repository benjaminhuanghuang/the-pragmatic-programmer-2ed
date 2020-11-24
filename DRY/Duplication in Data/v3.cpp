struct Point
{
  int x;
  int y;
  double distanceTo(Point &other);
};

class Line
{
private:
  double length;
  Point start;
  Point end;


  void calculateLength()
  {
    length = start.distanceTo(end);
  }

public:
  Line(Point start, Point end) : start(start), end(end)
  {
    calculateLength();
  }
  // public
  void setStart(Point p)
  {
    start = p;
    calculateLength();
  }
  void setEnd(Point p)
  {
    end = p;
    calculateLength();
  }
  Point getStart() { return start; }
  Point getEnd() { return end; }
  double getLength() { return length; }
};

/*

*/