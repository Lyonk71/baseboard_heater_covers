from lumber import Lumber
import cuts

baseboard_lumber = Lumber(60, False)

adjusted_length = cuts.calculate_adjusted_length(
    baseboard_lumber.exact_length,
    baseboard_lumber.corner_cut,
    baseboard_lumber.mid_foot_width,
)
num_sections = cuts.calculate_num_sections(adjusted_length)
(
    topshelf_midpiece_length,
    topshelf_endpiece_length,
    topshelf_cornerpiece_length,
    crossbar_length,
) = cuts.calculate_variable_cut_lengths(adjusted_length, num_sections)

(
    topshelf_midpiece_count,
    topshelf_endpiece_count,
    topshelf_cornerpiece_count,
    crossbar_count,
    end_foot_count,
    mid_foot_count,

) = cuts.calculate_number_of_each_cut(num_sections, baseboard_lumber.corner_cut)

cuts.generate_cut_lengths(
    topshelf_midpiece_count,
    topshelf_endpiece_count,
    topshelf_cornerpiece_count,
    crossbar_count,
    end_foot_count,
    mid_foot_count,
    topshelf_midpiece_length,
    topshelf_endpiece_length,
    topshelf_cornerpiece_length,
    crossbar_length
)
