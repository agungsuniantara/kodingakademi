class Event:
    """A new calendar event."""

    def _init_(self, start_time: int, end_time: int, event_name: str) -> None:
        """Initialize a new event that starts at start_time, ends at end_time,
        and is named name.

        Precondition: 0 <= start_time < end_time <= 23

        >>> e = Event(12, 13, 'Lunch')
        >>> e.start_time
        12
        >>> e.end_time
        13
        >>> e.name
        'Lunch'
        """
        self.start_time = start_time
        self.end_time = end_time
        self.name = event_name

    def _str_(self) -> str:
        """Return a string representation of this event.

        >>> e = Event(6, 7, 'Run')
        >>> str(e)
        'Run: from 6 to 7'
        """
        return '{0}: from {1} to {2}'.format(self.name, self.start_time,
                                             self.end_time)

    def overlaps(self, other: "Event") -> bool:
        """Return True iff this event overlaps with event other.

        >>> e1 = Event(6, 7, 'Run')
        >>> e2 = Event(0, 7, 'Sleep')
        >>> e1.overlaps(e2)
        True
        """
        return not (other.end_time <= self.start_time or other.start_time >= self.end_time)


class Day:
    """A calendar day and its events."""

    def _init_(self, day: int, month: str, year: int) -> None:
        """Initialize a day on the calendar with day, month, and year,
        and no events.

        >>> d = Day(5, 'April', 2014)
        >>> d.day
        5
        >>> d.month
        'April'
        >>> d.year
        2014
        >>> d.events
        []
        """
        self.day = day
        self.month = month
        self.year = year
        self.events = []

    def schedule_event(self, new_event: "Event") -> bool:
        """Schedule new_event on this day.

        >>> d = Day(26, 'March', 2013)
        >>> e = Event(11, 12, 'Meeting')
        >>> d.schedule_event(e)
        True
        >>> d.events[0] == e
        True
        """
        self.events.append(new_event)
        return True