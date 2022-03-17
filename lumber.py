class Lumber:
    """
    All measurements for baseboard heaters listed below are in inches
    """

    def __init__(self,
                 exact_length: float,
                 corner_cut: bool,
                 end_foot_width: float = 3.0,
                 mid_foot_width: float = 1.5,
                 foot_height: float = 7.5,
                 crossbar_width: float = 5.5,
                 top_width: float = 4.5):
        self.exact_length = exact_length
        self.corner_cut = corner_cut
        self.end_foot_width = end_foot_width
        self.mid_foot_width = mid_foot_width
        self.foot_height = foot_height
        self.crossbar_width = crossbar_width
        self.top_width = top_width
