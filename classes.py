#
class Measurements:
    """
    All measurements for baseboard heaters listed below are in inches
    """
    end_foot_width = 3.0
    mid_foot_width = 1.5
    foot_height = 7.5
    crossbar_width= 5.5
    top_width = 4.5

    def __init__(self, exact_length, corner_cut):
        self.exact_length = exact_length
        self.corner_cut = corner_cut

    def _calculate_adjusted_length(self):
        """
        2*mid_foot_width is subtracted from self.adjusted_length to
        account for the extra 1.5 inches on each end foot width.
        """
        if self.corner_cut == 'yes':
            self.adjusted_length = self.exact_length-4.5
        elif self.corner_cut == 'no':
            self.adjusted_length = self.exact_length

        self.adjusted_length = self.adjusted_length - (2*self.mid_foot_width)

    def _calculate_num_sections(self):
        """
        Calculate the number of sections that need to be cut.
        """
        self._calculate_adjusted_length()
        self.num_sections = round(self.adjusted_length/36.0)

    def _calculate_variable_cut_lengths(self):
        """
        Calculates the topshelf and crossbar lengths which vary for every wall.

        1/8 is removed between each section to account for the slight gap
        caused by installation.

        1/8 is also removed between each crossbar to allow easier installation.
        """
        self._calculate_num_sections()
        self.adjusted_length = self.adjusted_length - self.num_sections * (1/8)

        self.topshelf_midpiece_length = self.adjusted_length/self.num_sections
        self.topshelf_endpiece_length = self.topshelf_midpiece_length + 1.5
        self.topshelf_cornerpiece_length = self.topshelf_endpiece_length + 4.5
        
        self.crossbar_length = self.topshelf_midpiece_length - (3 + 1/8) 

    def _calculate_number_of_each_cut(self):
        """
        Calculates the number of fixed and variable cuts:

        Variable Cuts:
        Topshelf Midpiece
        Topshelf Endpiece
        Topshelf Cornerpiece
        Crossbar

        Fixed Cuts:
        End foot 
        Mid foot 
        """
        # fix me ------------------------------------------
        self._calculate_variable_cut_lengths()
        self.topshelf_midpiece_count = self.num_sections - 2
        if self.corner_cut == 'yes':
            self.topshelf_endpiece_count = 1
            self.topshelf_cornerpiece_count = 1
        elif self.corner_cut == 'no':
            self.topshelf_endpiece_count = 2
            self.topshelf_cornerpiece_count = 0

        self.crossbar_count = self.num_sections

        self.end_foot_count = 2
        self.mid_foot_count = self.num_sections * 2 - 2

        # fix me ------------------------------------------

    def generate_cut_lengths(self):
        """
        Generate counts and lengths for each of the cuts:
        Topshelf Midpiece
        Topshelf Endpiece
        Topshelf Cornerpiece
        Crossbar
        End foot 
        Mid foot 
        """
        self._calculate_number_of_each_cut() 
        output_list = [
        f'{self.topshelf_endpiece_count} - 1x5 @ {round(self.topshelf_endpiece_length, 3)}" - topshelf endpiece',
        f'{self.crossbar_count} - 1x6 @ {round(self.crossbar_length, 3)}" - crossbar',
        '',
        f'{self.mid_foot_count} - 1x2 @ 7.5" - topshelf mid foot',
        f'{self.end_foot_count} - 1x3 @ 7.5" - topshelf end foot',
        ]
        
        if self.topshelf_midpiece_count > 0:
            output_list.insert(0,
                    f'{self.topshelf_midpiece_count} - 1x5 @ {round(self.topshelf_midpiece_length, 3)}" - topshelf midpiece'
                    )
        else:
            pass

        if self.topshelf_cornerpiece_count > 0:
            output_list.insert(2,
                    f'{self.topshelf_cornerpiece_count} - 1x5 @ {round(self.topshelf_cornerpiece_length, 3)}" - topshelf cornerpiece',
                    )


        for i in output_list:
            print(i)
        print('\nnote - only accurate for lengths >= 62')
        print('this is the inflection point for when topshelf midpiece goes from negative to 0')
        print('Is the reeeeeson for the error that the negative length is added to the total length?')
        

#
p1 = Measurements(62, 'yes')
p1.generate_cut_lengths()

#
