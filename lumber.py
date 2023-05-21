from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Lumber:
    """
    All measurements for baseboard heaters listed below are in inches
    """

    exact_length: float
    corner_cut: bool
    length_adjustment: float = 4.5
    mid_foot_adjustment: float = 2.0
    division_factor: float = 36.0
    section_adjustment: float = 1 / 8
    topshelf_length_adjustment: float = 3
    cornerpiece_adjustment: float = 4.5
    crossbar_length_adjustment: float = 3 + 1 / 8
    end_foot_width: float = 3.0
    mid_foot_width: float = 1.5
    foot_height: float = 7.5
    crossbar_width: float = 5.5
    top_width: float = 4.5

    def calculate_adjusted_length(self) -> float:
        """
        Calculate the adjusted length based on whether a corner cut is present.
        """
        adjusted_length = (
            self.exact_length - self.length_adjustment
            if self.corner_cut
            else self.exact_length
        )
        adjusted_length -= 2 * self.mid_foot_adjustment

        return adjusted_length

    def calculate_num_sections(self, adjusted_length: float) -> int:
        """
        Calculate the number of sections based on the adjusted length.
        """
        return round(adjusted_length / self.division_factor)

    def calculate_variable_cut_lengths(
        self, adjusted_length: float, num_sections: int
    ) -> Tuple[float, float, float, float]:
        """
        Calculate various cut lengths based on the adjusted length and the number of sections.
        """
        adjusted_length -= num_sections * self.section_adjustment

        topshelf_midpiece_length = adjusted_length / num_sections
        topshelf_endpiece_length = (
            topshelf_midpiece_length + self.topshelf_length_adjustment
            if num_sections > 1
            else topshelf_midpiece_length + self.cornerpiece_adjustment
        )

        topshelf_cornerpiece_length = (
            topshelf_endpiece_length + self.cornerpiece_adjustment
        )
        crossbar_length = topshelf_midpiece_length - self.crossbar_length_adjustment

        return (
            topshelf_midpiece_length,
            topshelf_endpiece_length,
            topshelf_cornerpiece_length,
            crossbar_length,
        )

    def calculate_number_of_each_cut(
        self, num_sections: int
    ) -> Tuple[int, int, int, int, int, int]:
        """
        Calculate the number of each cut based on whether a corner cut is present and the number of sections.
        """
        topshelf_midpiece_count = num_sections - 2
        topshelf_endpiece_count = 2 if num_sections > 1 else 1
        topshelf_cornerpiece_count = 0

        if self.corner_cut:
            topshelf_endpiece_count = 1
            if num_sections > 1:
                topshelf_cornerpiece_count = 1

        crossbar_count = num_sections
        end_foot_count = 2
        mid_foot_count = num_sections * 2 - 2

        return (
            topshelf_midpiece_count,
            topshelf_endpiece_count,
            topshelf_cornerpiece_count,
            crossbar_count,
            end_foot_count,
            mid_foot_count,
        )

    def generate_cut_lengths(
        self,
        topshelf_midpiece_count: int,
        topshelf_endpiece_count: int,
        topshelf_cornerpiece_count: int,
        crossbar_count: int,
        end_foot_count: int,
        mid_foot_count: int,
        topshelf_midpiece_length: float,
        topshelf_endpiece_length: float,
        topshelf_cornerpiece_length: float,
        crossbar_length: float,
    ) -> List[str]:
        """
        Generate a list of cut lengths based on various parameters.
        """
        output_list = [
            f'{topshelf_endpiece_count} - 1x5 @ {round(topshelf_endpiece_length, 3)}" - topshelf endpiece',
            f'{crossbar_count} - 1x6 @ {round(crossbar_length, 3)}" - crossbar',
            "",
            f'{mid_foot_count} - 1x2 @ {self.foot_height}" - topshelf mid foot',
            f'{end_foot_count} - 1x3 @ {self.foot_height}" - topshelf end foot',
        ]

        if topshelf_midpiece_count > 0:
            output_list.insert(
                0,
                f'{topshelf_midpiece_count} - 1x5 @ {round(topshelf_midpiece_length, 3)}" - topshelf midpiece',
            )

        if topshelf_cornerpiece_count > 0:
            output_list.insert(
                2,
                f'{topshelf_cornerpiece_count} - 1x5 @ {round(topshelf_cornerpiece_length, 3)}" - topshelf cornerpiece',
            )

        output_list.append("\nnote - only accurate for lengths >= 62")
        output_list.append(
            "this is the inflection point for when topshelf midpiece goes from negative to 0"
        )
        output_list.append(
            "Is the reason for the error that the negative length is added to the total length?"
        )

        return output_list
