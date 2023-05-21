from lumber import Lumber

baseboard_lumber = Lumber(60, False)

adjusted_length = baseboard_lumber.calculate_adjusted_length()
num_sections = baseboard_lumber.calculate_num_sections(adjusted_length)

(
    topshelf_midpiece_length,
    topshelf_endpiece_length,
    topshelf_cornerpiece_length,
    crossbar_length,
) = baseboard_lumber.calculate_variable_cut_lengths(adjusted_length, num_sections)

(
    topshelf_midpiece_count,
    topshelf_endpiece_count,
    topshelf_cornerpiece_count,
    crossbar_count,
    end_foot_count,
    mid_foot_count,
) = baseboard_lumber.calculate_number_of_each_cut(num_sections)

cut_list = baseboard_lumber.generate_cut_lengths(
    topshelf_midpiece_count,
    topshelf_endpiece_count,
    topshelf_cornerpiece_count,
    crossbar_count,
    end_foot_count,
    mid_foot_count,
    topshelf_midpiece_length,
    topshelf_endpiece_length,
    topshelf_cornerpiece_length,
    crossbar_length,
)

for line in cut_list:
    print(line)

